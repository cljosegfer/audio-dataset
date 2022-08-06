#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 09:01:49 2022

@author: jose
"""

import os
from tqdm import tqdm
from aeneas.executetask import ExecuteTask
from aeneas.task import Task

# parametros

data_folder = 'data'
ds_folder = 'lusiadas'

text_folder = 'text'
audio_folder = 'audio'
output_folder = 'align'

text_folder = os.path.join(data_folder, ds_folder, text_folder)
audio_folder = os.path.join(data_folder, ds_folder, audio_folder)
output_folder = os.path.join(data_folder, ds_folder, output_folder)

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# aeneas
# prazer, meu nome é aeneas

text_files = sorted(os.listdir(text_folder))
audio_files = sorted(os.listdir(audio_folder))
output_files = [files[:-4] + '.json' for files in text_files]

print('aeneas, ~2min')
for text, audio, output in tqdm(zip(text_files, audio_files, output_files)):
    text_path = os.path.join(text_folder, text)
    audio_path = os.path.join(audio_folder, audio)
    output_path = os.path.join(output_folder, output)
    
    config_string = u'task_language=por|is_text_type=plain|os_task_file_format=json'
    task = Task(config_string=config_string)
    
    task.text_file_path_absolute = u'{}'.format(text_path)
    task.audio_file_path_absolute = u'{}'.format(audio_path)
    task.sync_map_file_path_absolute = u'{}'.format(output_path)
    
    ExecuteTask(task).execute()
    
    task.output_sync_map_file()

# # aeneas draft
# text = 'lus_canto_1.txt'
# audio = 'lusiadas_01_camoes_64kb.wav'

# output = os.path.join(output_folder, text[:-4] + '.json')
# text = os.path.join(text_folder, text)
# audio = os.path.join(audio_folder, audio)

# config_string = u'task_language=por|is_text_type=plain|os_task_file_format=json'
# task = Task(config_string=config_string)

# task.text_file_path_absolute = u'{}'.format(text)
# task.audio_file_path_absolute = u'{}'.format(audio)
# task.sync_map_file_path_absolute = u'{}'.format(output)

# ExecuteTask(task).execute()

# task.output_sync_map_file()
