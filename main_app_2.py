# 引用：https://jp-seemore.com/iot/python/9879/
# JPSM　初心者も安心！Pythonで音を鳴らす7つの方法
import numpy as np
import simpleaudio as sa

frequency = 440  # 440Hz（A4）の音を出す
fs = 44100  # サンプリング周波数
seconds = 3  # 3秒間鳴らす

t = np.linspace(0, seconds, seconds * fs, False)
note = np.sin(frequency * t * 2 * np.pi)
audio = note * (2**15 - 1) / np.max(np.abs(note))  # 16ビットオーディオに変換
audio = audio.astype(np.int16)

play_obj = sa.play_buffer(audio, 1, 2, fs)
play_obj.wait_done()
