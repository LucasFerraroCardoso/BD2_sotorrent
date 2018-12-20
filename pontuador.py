#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 13:43:10 2018

@author: lucascardoso
"""
import csv

def pontuar(body, title):
    score = 0
    if body[3] == 'W' and body[4] == 'h':
        score += 2
    
    if '<code>' in body:
        score += 1
    
    if 'thank' in body or 'please' in body or 'could' in body or 'would' in body or 'help' in body:
        score += 4
        
    if len(title) <= 50:
        score += 3
    
    return score
        
nome_ficheiro = 'results-20181220-135052.csv'
ficheiro = open(nome_ficheiro)

score = 0
score_list = []
resp = []

reader = csv.reader(ficheiro)
for linha in reader:
    score = pontuar(linha[8],linha[15])
    score_list.append(score)
    resp.append(int(linha[17]))

lista = []
lista = list(zip(score_list,resp))
lista.sort()
lista_sem = []
lista_com = []
for x in lista:
	if x[1] == 0:
		lista_sem.append(x)
	if x[1] > 0:
		lista_com.append(x)
		
print("Total de perguntas encontradas: {}".format(len(lista)))
print("Total de perguntas sem resposta: {}".format(len(lista_sem)))
print("Total de perguntas com resposta: {}".format(len(lista_com)))

notas = [0,1,2,3,4,5,6,7,8,9,10]
for n in notas:
	lista2 = []
	lista3 = []
	for x in lista:
		if x[0] == n and x[1] == 0:
			lista2.append(x)
		if x[0] == n and x[1] > 0:
			lista3.append(x)
	
	print("Total de perguntas com nota igual a {} sem resposta: {}".format(n,len(lista2)))
	print("Total de perguntas com nota igual a {} com resposta: {}\n".format(n,len(lista3)))
