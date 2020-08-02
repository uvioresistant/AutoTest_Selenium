#!/bin/sh
################################
#             自动化测试
#验证步骤：
# 0、登录用户，获取认证token
## 1、清理作业流实例信息
## 2、导入作业流配置
# 3、作业流A暂停翻牌
# 4、作业挂起---挂起A流作业JOB1，并发送JOB1外部文件事件
# 5、就绪作业解挂---解挂JOB1
# 6、运行中作业挂起和杀死 挂起JOB2、杀死JOB5 验证JOB2作业状态最终运行成功，但处于挂起状态，JOB5作业状态已终止
# 7、失败作业强制成功 强制成功JOB3
# 8、解挂JOB2 验证JOB4作业状态
# 9、终止态作业强制成功 JOB5强制成功
# 10、作业流暂停翻牌验证 --检查作业流A状态是否为暂停翻牌状态
# 11、作业流解除暂停翻牌验证 --检查作业流A是否翻牌到下一天，作业流B是否处于运行中
# 12、作业流B翻牌检查 --检查作业流B是否完成翻牌
# 13、作业流重新实例化验证 --检查作业流A是否重新完成实例化
#
# 说明：作业流A有5个作业：JOB1，JOB2，JOB3，JOB4，JOB5；作业流B有2个作业：JOB6，JOB7；
# 其中：
# JOB1依赖外部事件，
# JOB2、JOB3、JOB5依赖JOB1，
# JOB4依赖JOB2、JOB3；
# JOB6依赖JOB1和时间；
# JOB7依赖JOB3
###################################BEGIN：不同环境需要修改的信息字段###########################################
#登录用户名 --不同环境要修改此用户名称
userName="greenlight"
#干预地址
lubanUrl="http://128.196.108.10:8686"
#流同步url -- 前端ip地址
flowSynUrl="http://128.196.108.10:8080"
#域名
fieldName="NH"
#租户名称
tenantName="CCB"
#数据库信息
dbuser="schedule"
dbpwd="schedule"
dbsid="consvcf"
#######################################END:不同环境需要修改的信息字段###########################################

#环境信息
SQL_FILE=$HOME/tmp/chk_sql_tmp_file.log

#作业信息
flowName_A="jenkins_auto_call_jobflow_A"
flowName_B="jenkins_auto_call_jobflow_B"

auto_test_flow_a_id=
auto_test_flow_a_tenantid=
auto_test_flow_a_projectid=
auto_test_flow_b_id=
auto_test_flow_b_tenantid=
auto_test_flow_b_projectid=

flowInstId_A=""
flowInstId_B=""
flowId_A=""
flowId_B=""

jobId_JOB1=""
jobId_JOB2=""
jobId_JOB3=""
jobId_JOB4=""
jobId_JOB5=""
jobId_JOB6=""
jobId_JOB7=""

eventName="job1_jenkins_auto_call_jobflow_A_inputX"
reventCmd="schedule_re_event.sh -event job1_jenkins_auto_call_jobflow_A_inputX ${bizDate} ${batchNo} ${fieldName} ${tenantName}"
bizDate="20200720"
batchNo="0001"
nextDate=`date -d "${bizDate} +1 day" + "%Y%m%d"`

# 认证json串
authJson="{\"fieldId\":\"16BFABAAA8B0005\",\"loginAccount\":\"huangli4.zh\",\"loginPwd\":\"5f4dcc3b5aa765d61d8327deb882cf99\",\"tenantNameEn\":\"p9VT\"}"


parse_json()
{
	echo $1 | sed 's/.*'$2':\([^,]*\).*/\1/'
}

send_json_to_service()
		{
				local sendJson=$1
				local tarUrl=$2
				local flag=$3
				local ask_tmfile=$HOME/tmp/ask_tmpfile.$$
				
				# 发送命令串为
				curlcmd="curl -s -H 'content-type:application/json' -X POST -d '${sendJson}' ${tarUrl}"
				echo "[INFO] 提交到服务请求的执行命令为: ${curlcmd}"
				
				# echo "开始执行命令"
				sh -c "$curlcmd" >${ask_tmfile}
				if [ $? -ne 0 ]
				then
						echo "[ERROR] 提交json到服务请求失败"
						exit -1
				fi
				askret=`cat ${ask_tmfile}|sed s/[[:space:]]//g`
				rm -f ${ask_tmfile}
				
				if [ "$flag"x == ""x ]
				then
						askstatus=$(parse_json  $askret '"returnCode"' | sed 's/\"//g')
						returnMsg=$(parse_json  $askret '"returnMsg"' | sed 's/\"//g')
						successFlag=``echo ${askret}|grep -Po 'errorMessage[":]+\K[^"]+'`
				else
						askstatus=$(parse_json  $askret '"responseCode"' | sed 's/\"//g')
						returnMsg=$(pase_json $askret '"errorMessage"' | sed 's/\"//g')
						token=`echo ${askret}|grep -Po 'errorMessage[":]+/K[^"]+'`
						echo "token=[$stoken]"
				fi
				#echo "$askret"
				#ehoc "askstatus{$askstatus}"
				#echo "returnMsg{$returnMsg}"
				if [ "$askstatus"x == "200x" ] || ["$askstatus"x == "0"x ] || [ "askstatus"x == "00"x ] || [ "${successFlag}"x == "true"x ]
				then
						echo -e "[INFO] 提交curl请求成功! 请求状态[$askstatus] 返回消息:[${askret}] \n"
						return 0
				else
						echo -e "[] 提交json到服务请求返回异常，请求状态[$askstatus] 返回消息:${askret}\n"
						exit 1
				fi
		}
		
##数据库操作
#sql语句执行公共函数
oracle_excute_sql_func()
{
				echo "调用oracle公共执行函数"
				local sql="$1"
				local input_file="$2"
				
				#echo "sql=${sql}"
				#echo "input_file=${input_file}"
				
				if [ "input_file"x = ""x ]
				then
						input_file=$TMP_SQL_FILE
				fi
				
				sqlplus -s ${dbuser}/${dbpwd}@s{dbsid} 1>${input_file} 2>&1 <<EOF
				set head off;
				set linesize 5000;
				set pagesize 2000;
				set term off;
				${sql}
EOF
	if [ $? -ne 0 ]
	then
		echo "执行[${sql}]失败"
		delete;
		return 01;
	else
			# 删除空行
			# cat ${input_file}
		sed -i '/^$/d' ${input_file}
		sed -i '/selected/d' ${iinput_file}
			# 删除空格
			sed -i 's/[[:space:]]//g' ${input_file}
			echo "执行[${sql}] 成功"
		return 0;
	fi
	
}

mysql_excute_sql_func()
{
		echo "调用mysql公共执行函数"
}

pub_sql_exec_func()
{
	if [ "${dbType}"x = ""x ]
	then
		oracle_excute_sql_func "$1" $2"
		else
				mysql-excute_sql_func "$1" "$2"
	fi
}

#0.获取用户认证
get_aut_token()
{
	#认证接口
	local targtUrl="${lubanUrl}/thirdJobControl/login "
	local tmpSqlFile="$HOME/tmp/loginAccout.log.$$"
	local execSql="select '{\"tenantNameEn\":\"'||t2.tenant_name_en||'\", '||'\"fieldId\":\"'||t1.field_Id||'\",'||'\"fieldName\":\"'||t3.field_name||'\", '||'\"loginAccount\":"'||t1.LOGIN_ACCOUNT||'\",\"loginPwd\":\"'||t1.LOGIN_PWD'/"}' from sys_user_info t1, cfg_tenant_info t2, cfg_schedule_field t3 where t1.login_account='${userName}' and t1.tenant_id=t2.tenant_id and t1.field_id=t2.field_id and t2.field_id=t3.field_id;"
	echo "exec: ${execSql}"
	echo "...步骤0.获取用户认证token..."
	
	pub_sql_exec_func "${execSql}" "${tmpSqlFile}"
	authJson=`cat ${tmpSqlFile}|awk '{print $1}'`
	echo "authJson=[${authJson}]"
	send_json_to_service $(authJson) $(targtUrl) auth
	if [ $? -eq 0 ]
	then
		echo "获取用户认证token 【成功】"
	else
		echo "获取用户认证token 【失败】"
		exit -1
	fi
}

#1.清理实例信息
clean_jobflow_instance_info()
{
		return 0
}


#2.导入作业流配置
jobflow_cfg_install()
{
		echo "...步骤2、导入作业流配置..."
		return 0
}


#获取作业流信息
get_flow_info()
{
	#此处sleep是为了防止程序执行过快而实例未插入表里
	sleep 5
	getSql="select t1.flow_name|| '|' ||t2.job_name || '|' || t1.flow_id || '|' ||t2.job_id from dts_flow t1, dts_job t2 where t1.flow_name in ('${flowName_A}', '${flowName_B}') and t1.flow_id=t2.flow_id order by t2.job_name asc;"
	tmpSqlFile="$HOME/lhd/get_flow_info.log.$$"
	
	echo "...SETP1.开始你获取作业流信息..."
	pub_sql_exec_func "${getSql}" "${tmpSqlFile}"
	if [ $? -eq 0 ]
	then
		cat ${tmpSqlFile}
		flowId_A=`grep ${flowName_A} ${tmpSqlFile}|head -l|awk -F '|' '{print $3}'`
		flowId_B=`grep ${flowName_B} ${tmpSqlFile}|head -l|awk -F '|' '{print $3}'`
		jobId_JOB1=`grep job1_jenkins_auto_call_jobflow_A ${tmpSqlFile}|awk -F '|' '{print $4}'`
		jobId_JOB2=`grep job2_jenkins_auto_call_jobflow_A ${tmpSqlFile}|awk -F '|' '{print $4}'`
		jobId_JOB3=`grep job3_jenkins_auto_call_jobflow_A ${tmpSqlFile}|awk -F '|' '{print $4}'`
		jobId_JOB4=`grep job4_jenkins_auto_call_jobflow_A ${tmpSqlFile}|awk -F '|' '{print $4}'`
		jobId_JOB5=`grep job5_jenkins_auto_call_jobflow_A ${tmpSqlFile}|awk -F '|' '{print $4}'`
		jobId_JOB6=`grep job6_jenkins_auto_call_jobflow_B ${tmpSqlFile}|awk -F '|' '{print $4}'`
		jobId_JOB7=`grep job7_jenkins_auto_call_jobflow_B ${tmpSqlFile}|awk -F '|' '{print $4}'`
		echo "获取作业流信息成功"
		echo "flowId_A=[${flowId_A}] flowId_B=[${flowId_B}] jobId_JOB1=[$(jobId_JOB1] jobId_JOB2=[$(jobId_JOB2] jobId_JOB3=[$(jobId_JOB3] jobId_JOB4=[$(jobId_JOB4] jobId_JOB5=[$(jobId_JOB5] jobId_JOB6=[$(jobId_JOB6] jobId_JOB7=[$(jobId_JOB7]"
		rm -f ${tmpSqlFile}
	else
		echo "获取作业信息失败！！！"
	fi
	echo "...STEP2.获取作业流实例信息..."
	getSql_2="select flow_instid||'|'||flow_id from dts_flow_inst where biz_date=to_date('${bizDate}', 'yyyy/mm/dd') and batch_no='${batchNo}' adn flow_id in ('${flowId_A}', '${flowId_B}');"
	pub_sql_exec_func "${getSql_2}" "${tmpSqlFile}"
	
	if [ $? -eq 0 ]
	then
		cat ${tmpSqlFile}
		flowInstId_A=`grep ${flowId_A} ${tmpSqlFile}|awk -F '|' '{print $1}'`
		flowInstId_B=`grep ${}flowId_B ${tmpSqlFile}|awk -F '|' '{print $2}'`
		echo "获取作业流信息成功！"
		rm -f ${tmpSqlFile}
	else
		echo "获取作业信息失败！！！"
		exit -1
	fi
	
	return 0
}


#3.作业流A暂停翻牌
jobflow_stop_draw()
{
		#干预接口
		local tgtUrl="${lubanUrl}/flowinterpose/stopDrawJobFlow?token=$token"
		#sql检验语句
		local checkSql="SELECT HOLD_FLAG FROM DTS_FLOW_INST WHERE FLOW_ID='${flowId_A}' and biz_date=to_date('${bizDate}', 'yyyy/mm/dd') and batch_no='${batchNo}';"
		#暂停翻牌的json格式串
		local sendJson="{\"flowList\":[{\"flowInstId\":\"${flowInstId_A}\", \"flowId\":\"${flowId_A}\", \"biz_date\":\"${bizDate}\",\"batchNo\":\"${batchNo}\"}],\"userName\":\"admin\"}"
		local tmpSqlFile="$HOME/tmp/jobflow_stop_draw.log.$$"
		
		echo -e "\n【...步骤3、step1.作业流A暂停翻牌...】"
		echo "调用作业流暂停翻牌干预接口"
		
		send_json_to_service "${sendJson}" "${tgtUrl}"
		if [ $? -eq 0 ]
		then
				echo "调用作业流暂停翻牌干预接口【成功】"
		else
				echo "调用作业流暂停翻牌干预接口【失败】！！！"
				exit -1
		fi
		
		echo "...step2.检查作业流B是否完成暂停翻牌..."
		pub_sql_exec_func "${checkSql}" "${tmpSqlFile}"
		result=`cat ${tmpSqlFile}|awk '{print $1}'`
		if [ ${result} -eq 1 ]
		then
				rm -f ${tmpSqlFile}
				echo "检测作业流A暂停翻牌成功."
		else
				echo "检测作业流A暂停翻牌失败！！！"
				exit -2
		fi
}

#4.作业挂起 挂起A流作业JOB1，并发送JOB1外部文件事件
job_Hang_Up()
{
		tgtUrl=${lubanUrl}/jobinterpose/jobHangUp?token=${$token}
		sendJson="{\"jobList\":[{\"flowInstId\":\"{flowInstId_A}\", \"jobId\":\"${jobId_JOB1}\",\"biz_date\":\"${bizDate}\", \"batchNo\":\"${batchNo}\"}], \"userName\":\"admin\"}"
		checkSql="select count(1) from dts_job_inst where job_id='${jobId_JOB1}' and biz_date=to_date('${bizDate}', 'yyyy/mm/dd') and batch_no='${batchNo}' and is_hangup='1';"
		local tmpSqlFile="$HOME/tmp/job_Hang_Up.log.$$"
		
		# sleep 10
		echo -e "\n【...步骤4、step1 作业挂起---挂起A流作业JOB1...】"
		echo "调用作业挂起干预接口"
		send_json_to_service ${sendJson} ${tgtUrl}
		if [ $? -eq 0 ]
		then
				echo "调用干预接口挂起作业成功"
		else
				echo "调用干预接口挂起作业失败！！！"
				exit -1
		fi
		echo "...step2.检查作业JOB1是否挂起成功..."
		pub_sql_exec_func "${checkSql}" "${tmpSqlFile}"
		result=`cat ${tmpSqlFile}|awk '{print $1}'`
		if [ "${result}"x == "1"x ]
		then
				rm -f ${tmpSqlFile}
			echo "检查成功,作业挂起成功。"
		else
			echo "检查失败,作业挂起ERROR!!!"
			exit -2
		fi
			echo "step3.对JOB1发送事件"
			eventCmd="sh schedule_re_event.sh -event ${eventName} ${bizDate} ${batchNo} ${fieldName} ${tenantName}"
			echo "${eventCmd}"
			sh -c "${eventCmd}"
			if [ $? -ne 0 ]
		then
			echo "[ERROR] 发送事件失败"
			exit -1
		else
			echo "发送事件成功"
		fi
		echo "step4.检查JOB1是否处于就绪状态"
		checkSql2="select status from dts_job_inst where flow_instid='${flowInstId_A}' and job_id='${jobId_JOB1}' and biz_date=to_date('bizDate', 'yyyy/mm/dd') and batch_no='${batchNo}' and status !='0';"
		pub_sql_exec_func "${checkSql2}" "${tmpSqlFile}"
		result=`cat ${tmpSqlFile}|awk '{print $1}'`
		if [ "${result}"x != "0"x ]
		then
			echo "检查成功，作业处于事件就绪状态"
			return 0
		else
			echo "检查失败，作业处于事件未就绪状态！！！"
			exit -2
		fi
}

#5.就绪作业解挂---解挂JOB1
job_Rm_HangUp()
{
	tgtUrl=${lubanUrl}/jobinterpose/jobHangUp?token=${token}
	sendJson="{\"jobList\":[{\"flowINIstId\":\"${flowInstId_A}\", \"jobId\":\"${jobId_JOB1}\", \"biz_date\":\"${bizDate}\", \"batchNo\":\"${batchNo}\"}], \"userName\":\"admin\"}"
	checkSql="select is_hangup from "
}


















