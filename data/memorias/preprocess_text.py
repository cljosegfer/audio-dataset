#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 18:54:13 2022

@author: jose
"""

import os
from tqdm import tqdm

# parametros
input_file = './pg54829.txt'
output_folder = './text/'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# leitura
with open(input_file, 'r') as f:
    lines = f.readlines()
f.close()

# ----------------------------
# processamento
# ----------------------------

# remover inicio e final
lines = lines[71:8297]

# remover vazios
lines = [line for line in lines if line != '\n']

# remover espaços
lines = [line.strip() for line in lines]

# percebi alguns erros com o modulo seguinte
lines[5119] = 'CAPITULO CXXIV\n'
lines[5830] = 'CAPITULO CLIII\n'

# dedicatoria
for line in lines[26:33]:
    lines[25] += ' {}'.format(line)
    lines.remove(line)

# dialogo adao e eva
gemidos = [2671, 2673, 2675, 2676, 2678, 2680, 2682, 2683, 2684, 
           2686, 2688, 2690, 2691, 2692, 2693, 2694, 2696, 2698, 
           2700]
for idx in sorted(gemidos, reverse = True):
    lines.pop(idx)

# # separar capítulos e remove numero romano
# key = 'CAPITULO'
# capitulos = []
# capitulo = []
# i = 1
# for line in lines:
#     if key in line:
#         line = '{} {}\n'.format(key, i)
#         i += 1
#         capitulos.append(capitulo)
#         capitulo = []
#     capitulo.append(line)
# capitulos.append(capitulo)
# assert len(capitulos) == 161 # memorias tem 160 capitulos

# # agrupar capitulos dos audios

# remover numero romano
key = 'CAPITULO'
i = 1
for line in lines:
    if key in line:
        line = '{} {}\n'.format(key, i)
        i += 1

# ----------------------------

# escrita
print('export text')
path = output_folder + 'memorias.txt'
with open(path, 'w') as f:
    for line in tqdm(lines):
        f.write('{}\n'.format(line))
f.close()
