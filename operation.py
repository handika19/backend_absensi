import face_recognition
import argparse
import base64
import pickle
import cv2
import pymysql
import json, hashlib
import os
from werkzeug.utils import secure_filename
from flask import jsonify, Flask
from datetime import date
from datetime import time
from datetime import datetime
from flask_api import status

app = Flask(__name__)
app.config['PATH_PHOTO'] = 'static/img'

BASE_URL = "http://127.0.0.1:5000/"

class OperationCore(object):
    def __init__(self):
        self.db = self.connectDatabase()

    def connectDatabase(self):
        db = pymysql.connect("localhost","root","","sistem_absensi")
        return db

    def postLogout(self, nip):
        data = datetime.now()
        waktu_out = data.strftime("%X")
        tanggal = data.strftime("%Y-%m-%d")

        cek = self.ceknip(nip)

        if cek == True:
            query = """update absensi set waktu_pulang = %s where nip = %s and tanggal = %s"""
            args = (waktu_out, nip.decode("utf-8"), tanggal)

            cursor = self.db.cursor()
            cursor.execute(query,args)
            self.db.commit()

            return jsonify(msg="Absen pulang berhasil")
        else:
            return jsonify(msg="Absen pulang gagal")


    def postAbsensi(self, nip, photo):
        cek = self.ceknip(nip)

        data = datetime.now()
        waktu_masuk = data.strftime("%X")
        tanggal = data.strftime("%Y-%m-%d")

        if cek == True:
            photo_name = self.savephoto(nip,photo)
            cekrecog = self.recog('static/img/'+photo_name)

            nipcek = nip.decode("utf-8")

            if nipcek == cekrecog:
                query = """INSERT INTO absensi(nip,waktu_masuk,tanggal,foto_url)VALUES(%s,%s,%s,%s)"""
                args = (nip, waktu_masuk, tanggal, BASE_URL+"static/img/"+photo_name)

                cursor = self.db.cursor()
                cursor.execute(query,args)
                self.db.commit()

                if cursor.rowcount > 0:
                    dat_return = "Berhasil", 200
                else:
                    dat_return = "Tidak berhasil absen", 404
            else:
                dat_return = "Bukan muka anda", 417
            return dat_return
        else:
            dat_return = "Anda bukan pegawai disini", 404
        return json.dumps(dat_return)

    def recog(self, photopath):
        data = pickle.loads(open("encodings-nip.pickle", "rb").read())

        #photo = str(photo)
        image = cv2.imread(photopath)
        print(image.shape)
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        boxes = face_recognition.face_locations(rgb, model="cnn")
        encodings = face_recognition.face_encodings(rgb, boxes)


        for encoding in encodings:
            matches = face_recognition.compare_faces(data["encodings"], encoding)
            name = "Unknown"

            if True in matches:
                matchedIdxs = [i for (i, b) in enumerate(matches) if b]
                counts = {}
                for i in matchedIdxs:
                    name = data["names"][i]
                    counts[name] = counts.get(name, 0) + 1
                    # print(name)
                name = max(counts, key=counts.get)
                print("max : "+ str(name))
        return name

    def savephoto(self, nip, photo):
        photo_name = "img_"+nip.decode("utf-8")+".jpeg"
        photo.save(os.path.join(app.config["PATH_PHOTO"], photo_name))
        return photo_name

    def ceknip(self, nip):
        query =  """SELECT * FROM `pegawai` where nip = %s"""
        cursor = self.db.cursor()
        cursor.execute(query, nip)
        data = cursor.fetchall()

        if cursor.rowcount > 0:
            return True
        else:
            return False

    def cek_status_hadir(self, nip):
        nipdec = nip.decode("utf-8")
        query = """SELECT * FROM pegawai where nip = %s AND status_absen = 1 """
        cursor = self.db.cursor()
        cursor.execute(query, nipdec)
        data = cursor.fetchall()

        if cursor.rowcount > 0:
            return jsonify(status=1)
        else:
            return jsonify(status=0)


    def login(self, email, password):
        passhash = hashlib.md5(password)
        hash1 = passhash.hexdigest()

        args = (email, hash1)
        cursor = self.db.cursor()

        query =  """SELECT * FROM `pegawai` where email = %s AND password = %s """
        cursor.execute(query, args)

        row_headers = [x[0] for x in cursor.description]
        data = cursor.fetchall()

        json_data = []
        for i in data:
            json_data.append(dict(zip(row_headers, i)))

        return json.dumps(json_data)

    def lookPegawai(self):
        query = """SELECT * FROM pegawai"""
        cursor = self.db.cursor()
        cursor.execute(query)

        row_headers = [x[0] for x in cursor.description]
        data = cursor.fetchall()

        json_data = []
        for i in data:
            json_data.append(dict(zip(row_headers, i)))
        #print(json.dumps(json_data))
        return json.dumps(json_data)

    def lookAbsensi(self):
        data = datetime.now()
        tanggal = data.strftime("%Y-%m-%d")
        args = (tanggal)

        #SELECT id_absensi, nama, jabatan, tanggal, waktu_masuk, waktu_pulang
        #FROM absensi inner join pegawai on absensi.nip = pegawai.nip
        query = """SELECT id_absensi, absensi.nip, nama, jabatan, tanggal, waktu_masuk, waktu_pulang, foto_url FROM absensi inner join pegawai on absensi.nip = pegawai.nip WHERE tanggal = %s"""
        cursor = self.db.cursor()
        cursor.execute(query, args)

        row_headers = [x[0] for x in cursor.description]
        data = cursor.fetchall()

        json_data = []
        for i in data:
            json_data.append(dict(zip(row_headers, i)))

        return json.dumps(json_data)
