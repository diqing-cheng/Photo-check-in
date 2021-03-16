#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import face_recognition
from flask import Flask, jsonify, request, redirect, render_template

# You can change this to any folder on your system
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)


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

    # 图片上传失败，输出以下html代码
    return '''
    <!doctype html>
    <title>Is this a picture of Obama?</title>
    <h1><face_recognition test</h2>
    <form method="POST" enctype="multipart/form-data">
      要识别的人的照片：<input type="file" name="file"></br>
      作为识别标准的照片：<input type="file" name="target"></br><input type="submit" value="Upload">
    </form>
    '''


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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
