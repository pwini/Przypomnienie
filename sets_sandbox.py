# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 17:46:17 2019

@author: Ja
"""

S1=set(['1','2','3','4','5','6','7','8','9','0'])

S2=set(['1','1','2','3'])

L1=['1','2','3','4','5','6','7','8','9','0']

L2=['1','1','2','3']

T1=('1','2','3','4','5','6','7','8','9','0')

T2=('1','1','2','3')

S3=set(L1)

S4=set(L2)

#Operacje dla zbiorów
#Częsć wspólna zbiorów
S=S3 & S4
print('Częsć wspólna: ')
print(S)

#Suma zbiorów
S=S3 | S4
print('Suma zbiorów: ')
print(S)

#Różnica zbiorów:
S=S3 - S4
print('Różnica zbiorów: ')
print(S)




