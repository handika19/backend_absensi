import json
import os
from flask import Flask, request, jsonify
from operation import OperationCore
from werkzeug.utils import secure_filename
from datetime import datetime
import numpy as np
import cv2

app = Flask(__name__)

ops = OperationCore()

@app.route("/getpegawai")
def getpegawai():
    data = ops.lookPegawai()
    return data

@app.route("/absensi", methods=['POST'])
def absensi():
    if 'photo' not in request.files:
        return "Photo tidak ada"
    else:
        photo = request.files['photo']
        data = request.form
        nip = data["nip"].encode('utf-8')
        print(nip)
        return ops.postAbsensi(nip, photo)

@app.route('/cekabsensitoday', methods=["POST"])
def cekabsen():
    data = request.form
    nip = data["nip"].encode('utf8')
    return ops.cek_status_hadir(nip)

@app.route('/absenout', methods=['POST'])
def absenout():
    data = request.form
    nip = data["nip"].encode('utf-8')
    return ops.postLogout(nip)

@app.route("/login", methods=['POST'])
def login():
    #json = request.json
    dataf = request.form

    #email = json["email"].encode('utf-8')
    #password = json["password"].encode('utf-8')
    email = dataf["email"].encode('utf-8')
    password = dataf["password"].encode('utf-8')

    return ops.login(email, password)

@app.route("/getabsensi")
def getabsensi():
    data = ops.lookAbsensi()
    print(data)
    return data

@app.route("/")
def hello():
    return "<H1>Remember!, Everything Start From Hello World!</H1>"

if __name__ == "__main__":
    app.run()
