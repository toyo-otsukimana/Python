# 引用：【Python】日本語対応！テキストを音声に変換｜Google Text-To-Speech APIの利用方法
#       JPSM　初心者も安心！Pythonで音を鳴らす7つの方法
# URL：https://di-acc2.com/programming/python/25101/
#      https://jp-seemore.com/iot/python/9879/
# main_app_5.py（プロトタイプ）にフロントエンド部分の紐づけ処理を追加したもの
# web上にメイン画面を展開するところまで。使用説明画面は見つからない判定になる

from flask import Flask,render_template,session,request,redirect,url_for
import os                               # osモジュールの追加
from gtts import gTTS
import pygame
import time

# インスタンスの生成
app = Flask(__name__)

# メイン画面
@app.route('/')
def index():
    return render_template('main.html') # メイン画面を展開する

# 音声再生機能
@app.route('/main_action',methods = ['POST'])
def main_action():
    # text to speech関数（引数：変換テキスト、対応言語、出力ファイル名）
    def text_to_speech(text, language, filename):    
        
        # gTTSインスタンスの作成
        text2speech = gTTS(text,lang=language) # 音声変換するテキストと対応言語（ja：日本語）

        # 音声変換したデータをファイルに保存
        text2speech.save(filename + ".mp3")
        
        return True

    # テキスト（動作テスト用）
    # webアプリ化する際にフォームから受け取った文字列の受け皿として利用する
    # text = "こんにちは！今日の天気は雨で降水確率は80％です"
    
    # main.htmlのフォームから音声再生する文字列を受け取る
    text = request.form['talk']

    # 対応言語(日本語)英語も入力できるが、発音はローマ字読み風になる
    language = "ja"

    # 保存ファイル名
    filename = "gTTS_Text2Speech"

    # 関数実行
    text_to_speech(text, language, filename)

    # .mp3のファイルを音声再生する
    def play_mp3(filename):
        pygame.mixer.init()
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

    # 音声再生する関数を実行
    play_mp3('gTTS_Text2Speech.mp3') # 保存ファイル名と統一する
    time.sleep(10) # ()内で音声再生の秒数を指定。これがないと上手く動かない

# アプリケーションの起動
if __name__ == '__main__':
    app.run(debug=True)