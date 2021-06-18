# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 16:58:42 2020

@author: Ja
"""

import tensorflow as tf

# creates nodes in a graph
# "construction phase"
x1 = tf.constant(5)
x2 = tf.constant(6)

result = tf.mul(x1,x2)
print(result)