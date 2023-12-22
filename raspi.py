from flask import Flask
import os

kamera_dosya_yolu = "/home/pi/camera"
log_dosyasi_adi = kamera_dosya_yolu + "/fotolar.txt"
foto_sayici = 0

app = Flask(__name__, static_url_path=kamera_dosya_yolu, static_folder=kamera_dosya_yolu)

@app.route("/")
def index():
    return "Hello World"

@app.route("/check-movement")
def check_movement():
    mesaj = ""
    satir_sayaci = 0
    foto_dosya_adi = ""
    if os.path.exists(log_dosyasi_adi):
        with open(log_dosyasi_adi, "r") as f:
            for satir in f:
                satir_sayaci += 1
                foto_dosya_adi = satir
        global foto_sayici
        fark = satir_sayaci - foto_sayici
        mesaj = str(fark) + " son görülen zamandan bu yana olan fotoğraf.. <br/><br/>"
        mesaj += "Son foto: " + foto_dosya_adi + "<br/>"
        mesaj += "<img src=\"" + foto_dosya_adi + "\">"
        foto_sayici = satir_sayaci
    else:
        mesaj = "yeni bir şey yok.."
    return mesaj
        
app.run(host="0.0.0.0")