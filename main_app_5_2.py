# 引用：【Python】日本語対応！テキストを音声に変換｜Google Text-To-Speech APIの利用方法
# URL：https://di-acc2.com/programming/python/25101/
# from gtts import gTTS
import pygame

'''
# text to speech関数（引数：変換テキスト、対応言語、出力ファイル名）
def text_to_speech(text, language, filename):    
    
    # gTTSインスタンスの作成
    text2speech = gTTS(text,lang=language) # 音声変換するテキストと対応言語（ja：日本語）

    # 音声変換したデータをファイルに保存
    text2speech.save(filename + ".mp3")
    
    return True

# テキスト（動作テスト用）
text = "こんにちは！今日の天気は雨で降水確率は80%です。"

# 対応言語
language = "ja"

# 保存ファイル名
filename = "gTTS_Text2Speech"

# 関数実行
text_to_speech(text, language, filename)
'''

# .mp3のファイルを音声再生する
def play_mp3(filename):
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

play_mp3('gTTS_Text2Speech.mp3')