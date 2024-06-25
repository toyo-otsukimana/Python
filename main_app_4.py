# 引用：Flask：Webアプリでサーバ上のオーディオファイルを再生・ダウンロード
# https://www.wizard-notes.com/entry/python/flask-audiofile
# -*- coding: utf-8 -*-
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/music/<path:filename>")
def play(filename):
    return send_from_directory("music", filename)

if __name__ == "__main__":
    app.run("0.0.0.0", 80, debug=True)