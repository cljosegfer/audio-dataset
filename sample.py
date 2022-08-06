#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 10:13:13 2022

@author: jose
"""

import os
import json
from pydub import AudioSegment

# parametros

data_folder = 'data'
ds_folder = 'lusiadas'

text_folder = 'text'
audio_folder = 'audio'
align_folder = 'align'
output_folder = 'sample'

text_folder = os.path.join(data_folder, ds_folder, text_folder)
audio_folder = os.path.join(data_folder, ds_folder, audio_folder)
align_folder = os.path.join(data_folder, ds_folder, align_folder)
output_folder = os.path.join(data_folder, ds_folder, output_folder)

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# sample

text_files = sorted(os.listdir(text_folder))
audio_files = sorted(os.listdir(audio_folder))
align_files = sorted(os.listdir(align_folder))

# text_path = 'lus_canto_01.txt'
# audio_path = 'lusiadas_01_camoes_64kb.wav'
# align_path = 'lus_canto_01.json'
for text_path, audio_path, align_path in zip(text_files, audio_files, align_files):
    text_path = os.path.join(text_folder, text_path)
    audio_path = os.path.join(audio_folder, audio_path)
    align_path = os.path.join(align_folder, align_path)
    
    # --- read
    # text
    with open(text_path, 'r') as f:
        text = f.readlines()
    f.close()
    # audio
    audio = AudioSegment.from_wav(audio_path)
    # align
    with open(align_path, 'r') as f:
        align = json.load(f)['fragments']
    f.close()

    for i, sample_align in enumerate(align):
        # align
        start = float(sample_align['begin'])
        end = float(sample_align['end'])
        # text
        sample_text = sample_align['lines'][0]
        assert text[i] != sample_text, f'texto nao corresponde em {i}'
        # audio
        start = int(start * 1000)
        end = int(end * 1000)
        sample_audio = audio[start:end]
        
        # --- export
        sample_text_path = '{}_{}.txt'.format(text_path.split('/')[-1][:-4], i)
        sample_text_path = os.path.join(output_folder, sample_text_path)
        sample_audio_path = '{}_{}.wav'.format(text_path.split('/')[-1][:-4], i)
        sample_audio_path = os.path.join(output_folder, sample_audio_path)
        
        # text (precisa disso?)
        with open(sample_text_path, 'w') as f:
            f.write(sample_text)
        f.close()
        # audio
        sample_audio.export(sample_audio_path, format = 'wav')
