#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 11:49:30 2022

@author: jose
"""

import os

# ----------------------------
# esse script vai sempre depender do ds
# ----------------------------

# parametros
input_file = './pg3333.txt'
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
lines = lines[32:11076]

# remover vazios
lines = [line for line in lines if line != '\n']

# separar cantos
nomes = ['Canto Primeiro\n', 'Canto Segundo\n', 'Canto Terceiro\n', 
          'Canto Quarto\n', 'Canto Quinto\n', 'Canto Sexto\n', 
          'Canto Sétimo\n', 'Canto Oitavo\n', 'Canto Nono\n', 
          'Canto Décimo\n']
cantos = []
canto = []
idx = 0
ultimo = False
for line in lines:
    if not ultimo:
        if line == nomes[idx]:
            idx += 1
            if idx == len(nomes):
                ultimo = True
            cantos.append(canto)
            canto = []
    canto.append(line)
cantos.append(canto)
cantos.pop(0)

# remover indice estrofe
for canto in cantos:
    idx = 1
    estrofe = str(idx) + '\n'
    for line in canto:
        if line == estrofe:
            canto.remove(line)
            idx += 1
            estrofe = str(idx) + '\n'

# ----------------------------

# escrita
for canto in cantos:
    path = output_folder + 'lus_canto_{:02d}.txt'.format(cantos.index(canto) + 1)
    with open(path, 'w') as f:
        for line in canto:
            f.write(line)
    f.close()
