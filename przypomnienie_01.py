# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 14:45:18 2017

@author: piotr_000
"""
import matplotlib.pyplot as mlp
import numpy as np

a=1
#x=np.arange(-100,100,1)
start=np.round((-a)*np.pi)
stop=np.round((a)*np.pi)

print(start)
print(stop)

x=np.linspace(start,stop,1000000)
y=1/((x-2)*(x-1)*x*(x+1)*(x+2))
#y=np.sin(x)
mlp.figure(1)
mlp.plot(x,y,'-r')
mlp.ylim(-10,10)
#mlp.plot(x,x,'--g')
mlp.show()
