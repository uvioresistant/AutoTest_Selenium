#!bin/sh
#set -x
#############################################
## 管控配置文件入库自动化测试脚本
#############################################


###############################
## 数据库信息
###############################
DB_USER=schedule
DB_PWD=schedule
DB_SID=consvcf


##调度VT
#DB_USER=schedule
#DB_PWD=schedule
#DB_SID=128.196.126.97:11521/lubandb

common_url="http://128.196.108.10"

###############################
##登录用户信息
###############################
user="gk_admin"
password=000000
password=`echo -n $password|md5sum|cut -d " " -f 1`
tenantname="CCB"

fieldid="NH"
monserviceUrl="$common_url:8080" ##128.196.108.10
del_JobFlow_url="$common_url:8686"

retryCnt=1
######################################
##接口信息
######################################
##登录接口
loginUrl=$monserviceUrl/thirdJobControl/login
##配置文件
#configdir="$HOME/file/lgr/test"
curdir=`pwd`
configdir="$curdir/$fieldid"

echo "$configdir"

######################################
##配置文件信息
######################################
##逻辑资源量
resNum=100
##作业流数
flow_count=2
##逻辑资源名
resName="T-GREEN_TEST_A_RES"
##节点组
groupName="T-GREEN_TEST_A_GROUP"
#groupName="T_GREEN_TEST_A_GROUP"

if [ "$fieldid" == "NH" ];then
	#组件A B
	module_nameA=T-NH_GREEN_TEST_A
	module_nameB=T-NH_GREEN_TEST_B
	
	##工单号
	WIPNO_A_ADD="WIP_NO-99900010"
	WIPNO_B_ADD="WIP_NO-99900011"
	WIPNO_B_EDIT="WIP_NO-99900012"
	WIPNO_A_EDIT="WIP_NO-99900013"
	WIPNO_A_DEL_FLOW="WIP_NO-99900014"
	WIPNO_B_DEL_FLOW="WIP_NO-99900015"
	WIPNO_A_DEL_INFO="WIP_NO-99900016"
	WIPNO_B_DEL_INFO="WIP_NO-99900017"
	WIPNO_A_DEL="WIP_NO-99900018"
	WIPNO_B_DEL="WIP_NO-99900019"

	#配置文件名
	FILENAME_A_ADD="20200309.cctlCfgProject.P_0000102625.gz"
	FILENAME_B_ADD="20200309.cctlCfgProject.P_0000102625.gz"
	FILENAME_A_EDIT="20200309.cctlCfgProject.P_0000102627.gz"
	FILENAME_B_EDIT="20200309.cctlCfgProject.P_0000102628.gz"
	FILENAME_A_DEL_FLOW="20200309.cctlCfgProject.P_0000102629.gz"
	FILENAME_B_DEL_FLOW="20200310.cctlCfgProject.P_0000102651.gz"
	FILENAME_A_DEL_INFO="20200309.cctlCfgProject.P_0000102630.gz"
	FILENAME_B_DEL_INFO="20200310.cctlCfgProject.P_0000102631.gz"
	FILENAME_A_DEL="20200309.cctlCfgProject.P_0000102632.gz"
	FILENAME_B_DEL="20200309.cctlCfgProject.P_0000102633.gz"
elif [ "$fieldid" == "YQ" ];then
	##组件A B
	module_nameA=T-YQ_GREEN_TEST_A
	module_nameB=T-YQ_GREEN_TEST_B
	
	##YQ配置
	##工单号
	WIPNO_A_ADD="WIP_NO-99900000"
	WIPNO_B_ADD="WIP_NO-99900001"
	WIPNO_B_EDIT="WIP_NO-99900002"
	WIPNO_A_EDIT="WIP_NO-99900003"
	WIPNO_A_DEL_FLOW="WIP_NO-99900004"
	WIPNO_B_DEL_FLOW="WIP_NO-99900005"
	WIPNO_A_DEL_INFO="WIP_NO-99900006"
	WIPNO_B_DEL_INFO="WIP_NO-99900007"
	WIPNO_A_DEL="WIP_NO-99900008"
	WIPNO_B_DEL="WIP_NO-99900009"

	#配置文件名
	FILENAME_A_ADD="20200309.cctlCfgProject.P_0000102613.gz"
	FILENAME_B_ADD="20200309.cctlCfgProject.P_0000102614.gz"
	FILENAME_A_EDIT="20200309.cctlCfgProject.P_0000102615.gz"
	FILENAME_B_EDIT="20200309.cctlCfgProject.P_0000102616.gz"
	FILENAME_A_DEL_FLOW="20200309.cctlCfgProject.P_0000102617.gz"
	FILENAME_B_DEL_FLOW="20200310.cctlCfgProject.P_0000102618.gz"
	FILENAME_A_DEL_INFO="20200309.cctlCfgProject.P_0000102619.gz"
	FILENAME_B_DEL_INFO="20200310.cctlCfgProject.P_0000102620.gz"
	FILENAME_A_DEL="20200309.cctlCfgProject.P_0000102621.gz"
	FILENAME_B_DEL="20200309.cctlCfgProject.P_0000102622.gz"
else
	echo "未配置测试域"
fi

##配置文件名(全路径)
	FILENAME_A_ADD="${configdir}/${FILENAME_A_ADD}"
	FILENAME_B_ADD="${configdir}/${FILENAME_B_ADD}"
	FILENAME_A_EDIT="${configdir}/${FILENAME_A_EDIT}"
	FILENAME_B_EDIT="${configdir}/${FILENAME_B_EDIT}"
	FILENAME_A_DEL_FLOW="${configdir}/${FILENAME_A_DEL_INFO}"
	FILENAME_B_DEL_FLOW="${configdir}/${FILENAME_B_DEL_INFO}"
	FILENAME_A_DEL_INFO="${configdir}/${FILENAME_A_DEL_FLOW}"
	FILENAME_B_DEL_INFO="${configdir}/${FILENAME_B_DEL_FLOW}"
	FILENAME_A_DEL="${configdir}/${FILENAME_A_DEL}"
	FILENAME_B_DEL="${configdir}/${FILENAME_B_DEL}"
	
echo "test:$fieldid $monserviceUrl"

step_count=1

token=
g_paramcount=$#
g_param=$@
paramlist=
paramcount=0
selectcount=0

printflag="-print"
my_pid=$$
logpath=$HOME/log/auto_test/`date "+%Y%m%d"`
logname=auto_test_$my_pid
logfile=$logpath/$logname.tmp
chk_tmfile=$logpath/$logname.tmp
sql_file=$logpath/$logname.sql

#失败返回值
err_return_code=80
#参数异常
param_err_ret=90
#提交作业请求超时/超过次数
outime_err_ret=91
#无法识别的返回码
status_err_ret=93

print_log(){
  if [ "$2" = "-print" ]
  then
	echo "[`date +"%Y%m%d-%T"`] $1"
	echo "[`date +"%Y%m%d-%T"`] $1" >> $logfile
  else
	echo "[`date +"%Y%m%d-%T"`] $1" >> $logfile
  fi
}

usage()
{
					echo "[ERROR]输入参数为空或者参数错误，请检查参数[param]为非必写参数"
					echo "===================================================="
					echo "脚本名称:		$0"
					echo "脚本功能:		管控配置文件入库自动化测试"
					echo "脚本调用:		sh $0 -add A -add B -nodeGrpUpd 1 -resUpd 1 -edit A -del A -del B"
					echo "				[-edit]	需要导入的更新配置的组件名称"
					echo "				[-nodeGrpUpd] 1：将组件A的NODEGRP_A 节点组授权给组件B"
					echo "							  0: 将组件A的NODEGRP_A 节点组授权给组件B的权限收回"
					echo "				[-resUpd] 1：将组件A的RES_A 逻辑资源授权给组件B"
					echo "					      0: 将组件A的NODEGRP_A 逻辑资源授权给组件B的权限收回"
					echo "				[-delflow]  需要导入的清理作业作业流配置的组件名称"
					echo "				[-delinfo]  需要导入的清理公共参数信息(节点组，组件参数，逻辑资源)配置的组件名称"
					echo "				[-del]  需要删除的组件名称"
					echo "备注：A代表组件名称A; B代表代表组件名称B"
					echo "备注：没传入任何参数：按照新增组件A，新增组件B，授权节点组，授权逻辑资源，更新组件A，更新组件B，解除授权节点组，解除授权逻辑资源，删除组件A下的作业作业流信息，删除组件B下的作业作业作业流信息，删除组件A下的公共参数信息(节点组，组件参数，逻辑资源)，删除组件B下的公共参数信息(节点组，组件参数，逻辑资源)，删除组件A，删除组件B的流程跑完自动化测试"
}
exitShell()
{
if [ "$logfile" != "" ]
then
		print_log "[INFO] 执行测试命令结束......................." $printflag
		print_log "logfile={$logfile}" $printflag
fi
exit $1
}		

readparam()
{

local breakflag=0
if [ "`expr $g_paramcount % 2`" != "0" ]
then
	usage
	echo "[`date + "%Y%m%d-%T"`] 参数个数[$g_param]不是偶数个，请检查作业参数! "
	exitShell -1
fi

while [ "$breakflag" == "0" ]
do

prefix=$1
prefix=`echo $prefix|tr '[A-Z]' '[a-z]'`
shift
case $prefix in

-add)
paramlist[paramcount]="$prefix,$1"
paramcount=`expr $paramcount \+ 1`
shift
;;

-edit)
paramlist[paramcount]="$prefix,$1"
paramcount=`expr $paramcount \+ 1`
shift
;;

-delflow)
paramlist[paramcount]="$prefix,$1"
paramcount=`expr $paramcount \+ 1`
shift
;;

-nodegrpupd)
paramlist[paramcount]="$prefix,$1"
paramcount=`expr $paramcount \+ 1`
shift
;;

-resupd)
paramlist[paramcount]="$prefix,$1"
paramcount=`expr $paramcount \+ 1`
shift
;;


*}
usage
echo "[`date + "%Y%m%d-%T"`][WARN] 该参数不符合要求，不写入列表"
exitShell -1
;;
esac

if [ "$#" == "0" ]
then
	breakflag=1
fi
then
	breakflag=1
fi
done
}

select_sql()
{
local fun = "select_sql"
local ret
local sql_txt=$1
print_log "[$fun][INFO] 执行的sql:$sql_txt" $printflag
sqlplus -s $DB_USER/$DB_PWD@DB_SID<<EOF
	set head off;
	set feedback off;
	whenever sqlerror exit 9;
	spool ${sql_file};
	$sql_txt
	spool_off;
EOF

ret=`cat $sql_file|grep "ORA-"`
if [ "${ret}"x != ""x]
then
	print_log "[$fun][ERROR] select failed ${ret}." $printflag
	date
	exitShell -1
fi
# selectcount=`cat ${sql_file}|sed '/^$/d|sed 's/ //g'`
# rm ${sql_file}

}

#解析json
parseJson(){
	echo $1 | sed 's/.*'$2':\([[^,}]*\).*/\1/'
}
#解析json 有多个值不含中括号 "dsads, jkk"
parseJson_Mult_values(){
	echo $1 | sed 's/.*'$2':\([^;}]*\).*/\1/'
}
#解析json 有多个值含中括号
parseJson_MIddleBrackets(){
	echo $1 | sed 's/.*'$2':\([\".*\"]\).*/\1'
}
##通过http获取信息
getinfo_from_http(){
	local fun="getinfo_from_http"
	local httpjson=$1
	local locate_url=$2
	curlcmd="curl -H 'content-type:application/json' -X POST -d '${httpjson}' ${locate_url}"
	print_log "[$fun][INFO] curl=$curlcmd " $printflag
	for (( i=0 ; i<= $retryCnt ; i++ ))
do
	sh -C "$curlcmd">${chk_tmfile}
	if [ $? -ne 0 ]
	then
		print_log "[$fun][WARN] 通过http判断状态 失败 " $printflag
		rm ${chk_tmfile}
		return ${outime_err_ret}
	fi
done
return 0

#登录接口
login_info(){
	local fun="login_info"
	local responseStatus
	local errorMessage
	local responseCode
		loginJson="{
			\"loginAccount\":\"${user}\",
			\"loginPwd\":\"${password}\",
			\"tenantNameEn\":\"${tenantName}\",
			\"filedName\":\"${fieldid}\"
		}"
}
	getinfo_from_http "$loginJson" "$loginUrl"
	if [ $? -eq ${outime_err_ret} ]
	then
		print_log "[${fun}][ERROR] return code ${outime_err_ret}" $printflag
		return ${outime_err_ret}
	fi
	print_log "[${fun}][INFO] return code ${outime_err_ret}" $printflag
	chkret=`cat ${chk_tmfile}|sed s/[[:space:]]//g`
	rm ${chk_tmfile}
	responseStatus=$(parseJson $chkret '"responseStatus"' | sed 's/\"//g')
	errorMessage=$(parseJson $chkret '"errorMessage"' | sed 's/\"//g')
	responseCode=$(parseJson $chkret '"responseCode"' | sed 's/\"//g')
	
	responseStatus=`eval echo ${responseStatus}`
	responseCode=`eval echo ${responseCode}`
	errorMessage=`eval echo ${errorMessage}`
	if [[ "${responseStatus}"x == "00x" && "${responseCode}"x == "00x" ]]
	then
		token=$(parseJson $chkret '"token"' | sed 's/\"//g')
		token=`eval echo ${token}`
		print_log "[${fun}[INFO] ${errorMessage}]" $printflag
		return 0
	else
		print_log "[${fun}][ERROR] ${errorMessage}" $printflag
		return ${status_err_ret}
	fi
	return 0
}


del_jobflow(){
	local fun="del_jobflow"
	local httpjson
	##作业流实例删除接口
	local project_name_en=$1
	##调度作业流实例表
	##查询作业流实例数(确认与配置的作业流个数N是否相等)
	print_log "[$fun][INFO] 查询作业流实例数" $printflag
	sql_txt="select count(*) from dts_flow_inst f
	left join cfg_project_info p
	on f.project_id = p.project_id
	left join cfg_tenant_info t
	on p.tenat_id = t.tenant_id
	where p.project_name_en = '${project_name_en}'
	and t.tenant_name_en = '${tenantname}'
	and t.field_id = '${fieldid}';
	"
	select_sql "$sql_txt"
	flowinstcount=`cat ${sql_file}|sed '/^$/d'|sed 's/ //g'`
	rm ${sql_file}
	if [ "$flowinstcount"x == "0"x ]
	then
		print_log "[${fun}][INFO] 查询作业流实例数已清理" $printflag
		return 0
	fi
	print_log "[$fun][INFO] 查询作业流实例数没有清理，执行清理....." $printflag
	##作业流实例删除接口
	sql_txt="select f.flow_instid||'|'||f.flow_id||'|'||f.batch_no||'|'||to_char(f.biz_date, 'YYYYMMDD') from dts_flow_inst failed
	left join cfg_project_info on f.project_id = p.project_id
	left join cfg_tenant_info t on p.tenant_id = p.project_id
	where p.project_name_en = '${project_name_en}'
	and t.tenant_name_en = '${tenantname}'
	and t.field_id = '${fieldid}';
	"
	select_sql "$sql_txt"
	flowList=
	for var in `cat ${sql_file}|sed '/^$/d'|sed 's/ //g'`
	do
		flow_instid=`echo $var |cut -d "|" -f 1`
		flow_id=`echo $var |cut -d "|" -f 2`
		batch_no=`echo $var |cut -d "|" -f 3`
		biz_date=`echo $var |cut -d "|" -f 4`
		if [ "$flowList"x != ""x ]
		then
			flowList="${flowList},"
		fi
		flowList=$flowList"{
		\"flowInstId\":\"${flowinstid}\",
		\"flowId\":\"${flow_id}\",
		\"biz_date\":\"${biz_date}\",
		\"batchNo\":\"${batch_no}\"
		}"
	done
	rm ${sql_file}
	httpjson="{
	\"flowList\": [$flowList],
	\"userName\":\"${user}\"
	}"
	getinfo_from_http "$httpjson" "$DeleteJobFlowUrl"
	if [ $? -eq ${outime_err_ret} ]
	then
		print_log "[${fun}][ERROR] return code ${outime_err_ret}" $printflag
		exit ${outime_err_ret}
	fi
	print_log "[${fun}][ERROR] return code ${outime_err_ret}" $printflag
	chkret=`cat ${chk_tmfile}|sed s/[[:space:]]//g`
	rm ${chk_tmfile}
	returnCode=$(parseJson $chkret '"returnCode"' | sed 's/\"//g')
	msg=
	if [ ${returnCode}x != "0x" ]
	then
		case $returnCode in
		50)
			msg="部分成功"
			;;
		99)
			msg="失败"
			;;
		301)
			msg="实例不存在"
			;;
		303)
			msg="作业流实例中有作业处于运行中"
			;;
		331)
			msg="调用接口失败"
			;;
		334)
			msg="业务日期错误"
			;;
		335)
			msg="批次号错误"
			;;
		354)
			msg="作业流ID错误"
			;;
			*)
				msg="未知返回值"
				;;
		esac
			print_log "[${fun}][ERROR] 作业流实例删除失败，返回码：${returnCode} msg:${msg} " $printflag
			exitShell -1
		else
			print_log "[${fun}][INFO] 作业流实例删除成功" $printflag
			print_log "[${fun}][INFO] 查询作业流实例数清理完成...." $printflag
		fi
}

##上传文件
upload_file(){
#filename 为含全路径的文件名
local fun="upload_file"
local filename=$1
local httpjson="$filename"
local responseStatus
local errorMessage
local responseCode
curlcmd="curl --form \"file=@${httpjson}\" ${upload_file}"
	print_log "[INFO] curl=$curlcmd " $printflag
	for (( i=0 ; i<= $retryCnt ; i++ ))
	do
		sh -C "$curlcmd">${chk_tmfile}
		if [ $? -ne 0 ]
		then 
			print_log "[$fun][WARN] 通过http判断状态 失败" $printflag
			if [ $i -eq $retryCnt ]
			then
				print_log "[$fun][WARN] 3次通过http判断状态 失败" $printflag
				rm ${chk_tmfile}
				exitShell ${outime_err_ret}
			fi
			continue
		else
			break
		fi
	done
	print_log "[$fun][INFO] `cat ${chk_tmfile}`" $printflag
	chkret=`cat ${chk_tmfile}|sed s/[[::space:]]//g`
	rm ${chk_tmfile}
	responseStatus=$(parseJson $chkret '"responseStatus" | sed 's/\"//g'')
	errorMessage=$(parseJson $chkret '"errorMessage" | sed 's/\"//g'')
	responseCode=$(parseJson $chkret '"responseCode" | sed 's/\"//g'')
	responseStatus=`eval echo ${responseStatus}`
	responseCode=`eval echo ${responseCode}`
	if [[ "${responseStatus}"x == "00"x  && "${responseCode}"x == "00"x ]]
	then
		print_log "[$fun][INFO] ${errorMessage}" $printflag
	else
		print_log "[$fun][ERROR] 返回码:$responseCode 信息：${errorMessage}" $printflag
		exitShell -1
	fi
}

##组件文件包确认
confirm_cctlCfgProject(){
local fun="confirm_cctlCfgProject"
local wipNo=$1
local fileList=$2
local responseStatus
local errorMessage
local responseCode
local httpjson="{
	\"wipNo\":\"${wipNo}\",
	\"fileList\":[\"${fileList}\"]
	}"
	getinfo_from_http "$httpjson" "cctlCfgProject"
	if [ $? -eq ${outime_err_ret} ]
	then 
		print_log "[${fun}][ERROR] return code ${outime_err_ret}" $printflag
		exit ${outime_err_ret}
	fi
	print_log "[$fun][INFO] `cat ${chk_tmfile}`" $printflag
	chkret=`cat ${chk_tmfile}|sed s/[[:space:]]//g`
	rm ${chk_tmfile}
	responseStatus=$(parseJson $chkret '"responseStatus"' | sed 's/\"//g')
	errorMessage=$(parseJson $chkret '"errorMessage"' | sed 's/\"//g')
	responseCode=$(parseJson $chkret '"responseCode"' | sed 's/\"//g')
	responseStatus=`eval echo ${responseStatus}`
	respnoseCode=`eval echo ${responseCode}`
	if [[ "${responseStatus}"x == "00"x && "${responseCode}"x == "00"x]]
	then
		print_log "[$fun][INFO] 返回码:${responseCode}, ${errorMessage}" $printflag
	else
		print_log "[$fun][ERROR] 返回码:${responseCode}, ${errorMessage}" $printflag
		exitShell -1
	fi
}
###配置文件数据推送完成接口
confirm_cctlCfgPushFinish(){
	local responseStatus
	local errorMessage
	local responseCode
	local fun="confirm_cctlCfgPushFinish"
	local wipNo=$1
	local fileList=$2
	local httpjson="{
		\"wipNo\":\"${wipNo}\"
		\"fileList\":[\"${fileList}\"]
	}"
	
	getinfo_from_http "$httpjson" "$confirm_cctlCfgPushFinish"
	if [ $? -eq ${outime_err_ret} ]
	then 
		print_log "[${fun}][ERROR] return code ${outime_err_ret}" $print_log
		exit ${outime_err_ret}
	fi
	print_log "[$fun][INFO] `cat ${chk_tmfile}`" $printflag
	chkret=`cat ${chk_tmfile}|sed s/[[:space:]]//g`
	rm ${chk_tmfile}
	responseStatus=$(parseJson $chkret '"responseStatus"' | sed 's/\"//g')
	errorMessage=$(parseJson $chkret '"errorMessage"' | sed 's/\"//g')
	responseCode=$(parseJson $chkret '"responseCode"' | sed 's/\"//g')
	responseStatus=`eval echo ${responseStatus}`
	respnoseCode=`eval echo ${responseCode}`	
	if [[ "${responseStatus}"x == "00"x && "${responseCode}"x == "00"x]]
	then
		print_log "[$fun][INFO] 返回码:${responseCode}, ${errorMessage}" $printflag
	else
		print_log "[$fun][ERROR] 返回码:${responseCode}, ${errorMessage}" $printflag
		exitShell -1
	fi
}

##工单状态查询接口
query_wipInfo_status(){
	local fun="query_wipInfo_status"
	local responseStatus
	local errorMessage
	local responseCode
	local wipNo=$1
	local httpjson="{
		\"wipNo\":\"${wipNo}\"
	}"
	
	getinfo_from_http "$httpjson" "$WipInfoUrl"
	if [ $? -eq ${outime_err_ret} ]
	then 
		print_log "[${fun}][ERROR] return code ${outime_err_ret}" $print_log
		exit ${outime_err_ret}
	fi
	print_log "[$fun][INFO] `cat ${chk_tmfile}`" $printflag
	chkret=`cat ${chk_tmfile}|sed s/[[:space:]]//g`
	rm ${chk_tmfile}
	responseStatus=$(parseJson $chkret '"responseStatus"' | sed 's/\"//g')
	errorMessage=$(parseJson $chkret '"errorMessage"' | sed 's/\"//g')
	responseCode=$(parseJson $chkret '"responseCode"' | sed 's/\"//g')
	responseStatus=`eval echo ${responseStatus}`
	respnoseCode=`eval echo ${responseCode}`	
	case $responseCode in
	00)
		print_log "[$fun][INFO] 工单入库成功，msg:${errorMessage}" $printflag
		return 0
		;;
	01)
		print_log "[$fun][INFO] 工单入库失败，msg:${errorMessage}" $printflag
		return -1
		;;
	02)
		print_log "[$fun][INFO] 工单同步成功，msg:${errorMessage}" $printflag
		return 2
		;;
	03)
		print_log "[$fun][INFO] 工单同步失败，msg:${errorMessage}" $printflag
		return -1
		;;
	04)
		print_log "[$fun][INFO] 工单未处理，msg:${errorMessage}" $printflag
		return 1
		;;
	05)
		print_log "[$fun][INFO] 工单处理中，msg:${errorMessage}" $printflag
		return 1
		;;
	06)
		print_log "[$fun][INFO] 工单不存在，msg:${errorMessage}" $printflag
		exitShell -1
		;;
	07)
		print_log "[$fun][INFO] 工单状态异常，msg:${errorMessage}" $printflag
		exitShell -1
		;;
	*)
		print_log "[$fun][INFO] 工单无法识别，msg:${errorMessage}" $printflag
		exitShell -1
		;;
	esac
	return 0
}
				
###实例计划信息查询接口
query_instPlanInfo(){
	local fun="query_instPlanInfo"
	local project_name_en=$1
	local responseStatus
	local errorMessage
	local responseCode
	local flowCount
	local planInfo
	local httpjson="{
		\"projectNameEn\":[\"${projectNameEn}\"]
	}"
	
	getinfo_from_http "$httpjson" "$query_instPlanInfo"
	if [ $? -eq ${outime_err_ret} ]
	then 
		print_log "[${fun}][ERROR] return code ${outime_err_ret}" $print_log
		exit ${outime_err_ret}
	fi
	print_log "[$fun][INFO] `cat ${chk_tmfile}`" $printflag
	chkret=`cat ${chk_tmfile}|sed s/[[:space:]]//g`
	rm ${chk_tmfile}
	planInfo=$(echo $chkret | sed 's/.*'"flowInstInfo":{"planInfo"':\(\[{\".*\"}\]\).*/\1/')
	responseStatus=$(parseJson $chkret '"responseStatus"' | sed 's/\"//g')
	errorMessage=$(parseJson $chkret '"errorMessage"' | sed 's/\"//g')
	responseCode=$(parseJson $chkret '"responseCode"' | sed 's/\"//g')
	responseStatus=`eval echo ${responseStatus}`
	respnoseCode=`eval echo ${responseCode}`	
	flowCount=`eval echo ${flowCount}`
	if [[ "${responseStatus}"x == "00"x && "${responseCode}"x == "00"x]]
	then
		if [ "$flowCount"x == "$flow_count"x ] 
			print_log "[$fun][INFO] 组件${project_name_en}配置入库测试成功" $printflag
		else
			print_log "[$fun][INFO] 组件${project_name_en}配置入库测试失败,实例数据检测异常 $flowCount:$flow_count $errorMessage" $printflag
			#exitShell -1
		fi
	else
		print_log "[$fun][INFO] 组件${project_name_en}配置入库测试失败,实例数据检测异常 $flowCount:$flow_count $errorMessage" $printflag
		exitShell -1
	fi
}

###确认组件公共参数信息记录数是否为0
confirm_info_table_count(){
local fun="confirm_info_table_count"
local project_name_en=$1

	project_agent_count=0
	project_agent_count_1=0
	agent_grp_count=0
	agent_grp_count_1=0
	agent_cfg_count=0
	agent_cfg_count_1=0
	project_para_count=0
	project_para_count_1=0
	project_res_count=0
	project_res_count_1=0
}

###查询【组件执行器与组关系表】组件执行器与组是否清理
	print_log "[$fun][INFO] 查询 【组件执行器与组关系表】组件执行器与组是否清理" $print_log
	sql_txt="
	select count(*) from CCTL_CFG_PROJECT_AGENT_RELA r 
	left join CCTL_CFG_PROJECT_AGENT_GRP g 
	on g.agent_grp_no = r.agent_grp_no 
	where g.project_no in ('${project_name_en}')
	and g.cluster_no='${fieldid}';
	"
	select_sql "$sql_txt"
	porject_agent_count=`cat ${sql_file}|sed '/^$/d'|sed 's/ //g'`
	rm ${sql_file}
	if [ "${project_agent_count}"x == "0"x ]
	then
		print_log "[$fun][INFO] 组件【组件执行器与组关系表 CCTL_CFG_PROJECT_AGENT_RELA】组件执行器与组已清理" $printflag
	else
		print_log "[$fun][INFO] 组件【组件执行器与组关系表 CCTL_CFG_PROJECT_AGENT_RELA】组件执行器与组没有清理，需清理..." $printflag

	fi
}

###查询【组件执行器组配置表】组件执行器与组是否清理
	print_log "[$fun][INFO] 查询 【组件执行器组配置表】组件执行器与组是否清理" $print_log
	sql_txt="
	select count(*) from CCTL_CFG_PROJECT_AGENT_GRP a 
	where a.project_no in ('${project_name_en}')
	and a.cluster_no='${fieldid}';
	"
	select_sql "$sql_txt"
	agent_grp_count=`cat ${sql_file}|sed '/^$/d'|sed 's/ //g'`
	rm ${sql_file}
	if [ "${project_agent_count}"x == "0"x ]
	then
		print_log "[$fun][INFO] 查询【组件执行器组配置表 CCTL_CFG_PROJECT_AGENT_GRP】组件执行器与组已清理" $printflag
	else
		print_log "[$fun][INFO] 查询【组件执行器组配置表 CCTL_CFG_PROJECT_AGENT_GRP】组件执行器与组没有清理，需清理..." $printflag

	fi
}

###查询【组件执行器配置表】组件执行器是否清理
	print_log "[$fun][INFO] 查询 【组件执行器配置表】组件执行器与组是否清理" $print_log
	sql_txt="
	select count(*) from CCTL_CFG_PROJECT_AGENT a 
	where a.project_no in ('${project_name_en}')
	and a.cluster_no='${fieldid}';
	"
	select_sql "$sql_txt"
	agent_cfg_count=`cat ${sql_file}|sed '/^$/d'|sed 's/ //g'`
	rm ${sql_file}
	if [ "${agent_cfg_count}"x == "0"x ]
	then
		print_log "[$fun][INFO] 查询【组件执行器配置表 】组件执行器已清理" $printflag
	else
		print_log "[$fun][INFO] 查询【组件执行器配置表 】组件执行器没有清理，需清理..." $printflag

	fi
}

###查询【组件节点配置表】组件节点与组是否清理
	print_log "[$fun][INFO] 查询 【组件节点配置表】组件执行器与组是否清理" $print_log
	sql_txt="
	select count(*) from sys_node_info n, cfg_Project_node_rel r, cfg_project_info p, cfg_tenant_info t 
	where n.node_id=r.node_id 
	and r.project_id = p.project_id 
	and p.tenant_id=t.tenant_id
	and p.field_id='${fieldid}'
	and t.tenat_name_en='${tenantname}'
	and p.project_name_en in ('${project_name_en}')
	and r.pertain_type='1';
	"
	select_sql "$sql_txt"
	agent_grp_count=`cat ${sql_file}|sed '/^$/d'|sed 's/ //g'`
	rm ${sql_file}
	if [ "${project_agent_count}"x == "0"x ]
	then
		print_log "[$fun][INFO] 查询【组件节点配置表 sys_node_info】组件节点已清理" $printflag
	else
		print_log "[$fun][INFO] 查询【组件节点配置表 sys_node_info】组件节点没有清理，需清理..." $printflag

	fi
}

###查询【组件执行参数配置表】组件参数是否清理
	print_log "[$fun][INFO] 查询 【组件执行参数配置表】组件参数是否清理" $print_log
	sql_txt="
	select count(*) from CCTL_CFG_PROJECT_PARA a
	where a.project_no in ('${project_name_en}')
	and a.cluster_no='${fieldid}';
	"
	select_sql "$sql_txt"
	project_agent_count=`cat ${sql_file}|sed '/^$/d'|sed 's/ //g'`
	rm ${sql_file}
	if [ "${project_agent_count}"x == "0"x ]
	then
		print_log "[$fun][INFO] 查询【组件执行参数配置表 CCTL_CFG_PROJECT_PARA】组件节点已清理" $printflag
	else
		print_log "[$fun][INFO] 查询【组件执行参数配置表 CCTL_CFG_PROJECT_PARA】组件节点没有清理，需清理..." $printflag
	fi
}

###查询【组件执行参数配置表】组件参数是否清理
	print_log "[$fun][INFO] 查询 【组件执行参数配置表】组件参数是否清理" $print_log
	sql_txt="
	select count(*) from cfg_env_param a, cfg_project_info p, dfg_tenant_info t 
	where a.project_id=p.project_id 
	and p.tenant_id=t.tenant_id 
	and p.field_id='${fieldid}' 
	and t.tenant_name_en='${tenantname}'
	and p.project_name_en in ('${project_name_en}');
	"
	select_sql "$sql_txt"
	project_agent_count=`cat ${sql_file}|sed '/^$/d'|sed 's/ //g'`
	rm ${sql_file}
	if [ "${project_agent_count}"x == "0"x ]
	then
		print_log "[$fun][INFO] 查询【组件执行参数配置表 CCTL_CFG_PROJECT_PARA】组件节点已清理" $printflag
	else
		print_log "[$fun][INFO] 查询【组件执行参数配置表 CCTL_CFG_PROJECT_PARA】组件节点没有清理，需清理..." $printflag
	fi
}







					
					














