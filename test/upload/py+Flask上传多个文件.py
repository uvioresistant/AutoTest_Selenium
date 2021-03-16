#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:fengg
@file:py+Flask上传多个文件.py
@time:2021/03/10
"""
import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename

app = Flask(__name__)
# Path to the upload directory
app.config['UPLOAD_FOLDER'] = 'uploads/'
# 接收上传的文件
app.config['ALLOWED_EXTENSION'] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # 获取上传文件名
    uploaded_files = request.files.getlist("file[]")
    filenames = []
    for file in uploaded_files:
        # 检查上传文件是否是允许的类型
        if file and allowed_file(file.filename):
            # 确保安全后，移除不支持的文件
            filename = secure_filename(file.filename)
            # 移动
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            filenames.append(filename)
    return render_template('upload. html', filenames=filenames)

@app.route('/uploads/filenames')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("80"), debug=True)