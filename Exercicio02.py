# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa#
import random

MeuArray = []
listaInvertida = []

def adicionarnumeronoarray():
    pass
    newlist = []
    for n in range(1, 10):
        newlist.append(random.randint(1, 50))
    return newlist


MeuArray.append(adicionarnumeronoarray())

for num in MeuArray:
    print('Lista Normal :', num)
    listaInvertida = num[::-1]
    print('Lista Invertida :', listaInvertida)







