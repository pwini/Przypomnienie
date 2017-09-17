# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 17:38:53 2017

@author: piotr_000
"""

import sympy.solvers as ss


x=ss.Symbol('x')
y=ss.Symbol('y')
sol=ss.solve([x**2+y-7,x+y**2-11],x,y,set=True,dict=True)

#for i in range(4):
#    for j in range(4):
#        print(sol[j][i])


print(sol)
#print("sol - type is: "+str(len(sol)))