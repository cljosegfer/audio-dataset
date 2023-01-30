#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 14:01:22 2023

@author: jose
"""

import os
from pydub import AudioSegment
from datetime import datetime
from tqdm import tqdm

def read_srt(file):
    with open(file) as f:
        lines = f.readlines()

    times = lines[1::4]
    transcript = lines[2::4]
    
    return times, transcript

def get_times(time):
    begin, end = time[:-1].split(' --> ')
    
    date = datetime.strptime(begin, '%H:%M:%S,%f')
    begin = date.hour * 3600 + date.minute * 60 + date.second
    
    date = datetime.strptime(end, '%H:%M:%S,%f')
    end = date.hour * 3600 + date.minute * 60 + date.second
    
    return begin * 1000, end * 1000 # mseconds

# param

data_folder = 'a_margem_da_historia_1903_librivox'
ds = 'margem'
output_folder = ds

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# sample

files = sorted(os.listdir(data_folder))

mp3_files = [file for file in files if file[-4:] == '.mp3']
srt_files = [file for file in files if file[-4:] == '.srt']

# trim

for file_idx, srt_file in tqdm(enumerate(srt_files)):
    mp3_file = mp3_files[file_idx]
    
    # read srt
    srt_file = os.path.join(data_folder, srt_file)
    times, transcripts = read_srt(srt_file)
    
    # read mp3
    mp3_file = os.path.join(data_folder, mp3_file)
    audio = AudioSegment.from_mp3(mp3_file)
    
    for sequence_idx, time in enumerate(times):
        transcript = transcripts[sequence_idx]
        
        begin, end = get_times(time)
        
        sequence = audio[begin:end]
        
        # export
        path = '{}_{}_{}'.format(ds, file_idx, sequence_idx)
        path = os.path.join(output_folder, path)
        
        sequence.export(path + '.wav', format = 'wav')
        with open(path + '.txt', 'w') as f:
            f.write(transcript)
