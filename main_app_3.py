# 引用：https://jp-seemore.com/iot/python/9879/
# JPSM　初心者も安心！Pythonで音を鳴らす7つの方法
import numpy as np
import simpleaudio as sa

def play_tone(frequency, duration):
    fs = 44100
    t = np.linspace(0, duration, duration * fs, False)
    note = np.sin(frequency * t * 2 * np.pi)
    audio = note * (2**15 - 1) / np.max(np.abs(note))
    audio = audio.astype(np.int16)
    play_obj = sa.play_buffer(audio, 1, 2, fs)
    play_obj.wait_done()

notes = [(440, 0.5), (440, 0.5), (493.88, 0.5), (587.33, 1)]
for note in notes:
    play_tone(*note)
