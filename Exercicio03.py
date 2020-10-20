#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.#

import random

MeuArray = []

def adicionarnumeronoarray():
    pass
    newlist = []
    for n in range(1, 5):
        newlist.append(random.randint(1, 10))
    return newlist


MeuArray.append(adicionarnumeronoarray())

for num in MeuArray:
    print(sum(num) / 4)