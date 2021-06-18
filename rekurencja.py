# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 22:49:45 2020

@author: Ja
"""

def odliczanie(n):
    if n==0:
        return 0
    else:
        return str(n)+"_"+str(odliczanie(n-1))

def fibo(n):
    S=0
    if n<2:
        S=S+1
    else:
        S=S+n+fibo(n-1)
    return S
    print(str(fibo(n-1)))
    
for i in range(3):
    print(fibo(i))