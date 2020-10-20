# Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.#
import random

MeuArray = []


def adicionarnumeronoarray():
    pass
    newlist = []
    for n in range(1, 10):
        newlist.append(random.randint(1, 50))
    return newlist


MeuArray.append(adicionarnumeronoarray())

for num in MeuArray:
    print(num)









