#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 13:38:28 2022

@author: jose
"""

import os
from tqdm import tqdm
from pydub import AudioSegment
import librosa
import soundfile as sf

# ----------------------------
# esse script vai sempre depender do ds
# ----------------------------

# parametros
input_folder = './os_lusiadas_0908_librivox_64kb_mp3'
output_folder = './audio/'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# ----------------------------
# processamento
# ----------------------------

# mp3 to wav e trimm
print('mp3 to wav e trimm, ~1min')

# tempo inicial e final do corte, (min * 60 + seg) * 1000
times = [[(19)*1000, (36*60+20)*1000], [(19)*1000, (38*60+46)*1000], 
         [(19)*1000, (49*60+58)*1000], [(19)*1000, (36*60+41)*1000], 
         [(20)*1000, (35*60+45)*1000], [(19)*1000, (35*60+23)*1000], 
         [(20)*1000, (30*60+32)*1000], [(20)*1000, (35*60+50)*1000], 
         [(18)*1000, (33*60+47)*1000], [(19)*1000, (55*60+43)*1000]]

for file in tqdm(os.listdir(input_folder)):
    idx = int(file.split('_')[1]) - 1
    start, end = times[idx]
    mp3_path = os.path.join(input_folder, file)
    wav_path = os.path.join(output_folder, file[:-4] + '.wav')
    sound = AudioSegment.from_mp3(mp3_path)
    sound[start:end].export(wav_path, format = 'wav')

# sample rate
print('sample rate, ~10min')
orig_sr = 22050
target_sr = 16000

for file in tqdm(os.listdir(output_folder)):
    wav_path = os.path.join(output_folder, file)
    y, _ = librosa.load(wav_path, sr = orig_sr)
    y_16k = librosa.resample(y, orig_sr = orig_sr, target_sr = target_sr)
    sf.write(wav_path, y_16k, samplerate = target_sr)
