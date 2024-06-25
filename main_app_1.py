# flask_app_07.pyや前回の研究制作時に作成したプログラムを参考に作成
from flask import Flask,render_template,session,request,redirect,url_for
import os                               # osモジュールの追加
import win32com.client as wincl

# インスタンスの生成
app = Flask(__name__)

# メイン
@app.route('/') # Flaskのrouteを使用
# 以下に音声再生に関する処理を記述する
def index():
    return render_template('main.html')
def change_app():
    frame_app.tkraise()
    voice = wincl.Dispatch("SAPI.SpVoice")
    voice.Speak(entry1_frame.get())

def change_main():
    frame.tkraise()
    voice = wincl.Dispatch("SAPI.SpVoice")
    voice.Speak(entry1_frame_app.get())

# ウィンドウを閉じるための関数
def close_window():
    root.destroy()

# 音声再生をするための関数
def playSound(ev):
    soundFile = document["start-mp3"] 
    # JavaScriptのdocument.getElementById("start-mp3") に該当
    soundFile.play()