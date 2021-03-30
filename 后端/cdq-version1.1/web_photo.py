#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import face_recognition
from flask import Flask, jsonify, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()



# You can change this to any folder on your system
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)

class Config(object):
    """配置参数"""
    # 设置连接数据库到URL
    user = 'test'
    password = '4thefuture'
    host = '127.0.0.1'
    database = 'photo_check_in'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://%s:%s@%s:3306/%s' % (user,password,host,database)

    # 设置sqlalchemy自动跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # 查询时会显示原始sql语句
    app.config['SQLALCHEMY_ECHO'] =True

    # 禁止自动提交数据处理
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = False

# 读取配置
app.config.from_object(Config)

# 创建数据库sqlalchemy工具对象
db = SQLAlchemy(app)

class Student(db.Model):
    # 定义表明
    __tablename__ = 'student'
    # 定义字段
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    account = db.Column(db.String(60), nullable = False, index = True)
    password = db.Column(db.String(60), nullable = False)
    role = db.Column(db.String(60), nullable = False)
    school = db.Column(db.String(60), nullable = False)
    classId = db.Column(db.String(60), nullable = False)
    name = db.Column(db.String(60), nullable = False)
    gender = db.Column(db.String(60), nullable = False)

class Teacher(db.Model):
    # 定义表明
    __tablename__ = 'teacher'
    # 定义字段
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    account = db.Column(db.String(60), nullable = False, index = True)
    password = db.Column(db.String(60), nullable = False)
    role = db.Column(db.String(60), nullable = False)
    school = db.Column(db.String(60), nullable = False)
    workId = db.Column(db.String(60), nullable = False)
    name = db.Column(db.String(60), nullable = False)
    gender = db.Column(db.String(60), nullable = False)

if __name__ == '__main__':
    # 删除所有表
    #db.drop_all()

    # 创建所有表
    db.create_all()

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_image():
    # 检测图片是否上传成功
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        if 'target' not in request.files:
            return redirect(request.url)
        
        file = request.files['file']
        target = request.files['target']

        if file.filename == '' or target.name == '':
            return redirect(request.url)

        
        if file and target and allowed_file(file.filename) and allowed_file(target.filename):
            # 图片上传成功，检测图片中的人脸
            return detect_faces_in_image(file,target,)

    # 图片上传失败，返回结果
    result = {
        'msg':'img upload failed',
    }
    return jsonify(result)


def detect_faces_in_image(file_stream,target_file_stream):
    # 载入作为识别标准的图片
    target_img = face_recognition.load_image_file(target_file_stream)
    
    # 为识别标准图片中的人脸编码
    known_face_encodings = face_recognition.face_encodings(target_img)

    # 载入用户上传的图片
    img = face_recognition.load_image_file(file_stream)
    # 为用户上传的图片中的人脸编码
    unknown_face_encodings = face_recognition.face_encodings(img)

    face_found = False
    found_same_face = False
    
    if len(unknown_face_encodings) > 0 and len(known_face_encodings) > 0:
        face_found = True
        # 看看有没有相同的人脸出现在两张照片中
        match_results = face_recognition.compare_faces([known_face_encodings[0]], unknown_face_encodings[0])
        for results in match_results :
            if results :
                found_same_face = True
                
    # 将识别结果以json键值对的数据结构输出
    result = {
        "face_found_in_image": face_found,
        "found_same_face": found_same_face,
     }
    return jsonify(result)


@app.route('/loginuser', methods=['GET', 'POST'])
def loginuser():
    if request.method == 'POST':
        
        try:
            data = request.json
            user = data['loginUser']
            account = user['account']
            password = user['pass']
            role = user['role']      
            
            if role=='student':
                query_user = Student.query.filter_by(account=account)[0]
            elif role=='teacher':
                query_user = Teacher.query.filter_by(account=account)[0]
            else:
                return Response(False,'user login failed','')    

            if query_user==None:
                return Response(False,'user login failed','')
            else:
                if query_user.password==password and query_user.role == role:
                    return Response(True,'user login success',query_user.id)
                else:
                    return Response(False,'user login failed','')
        except Exception as e:
            print(e)
            return Response(False,'user login failed1','')
        
    else:
        return Response(False,'user login failed2','')


def Response(type,msg,value):
    result = {
        'success':type,
        'message':msg,
        'data':value
    }
    return jsonify(result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
