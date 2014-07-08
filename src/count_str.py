#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 8, 2014

@author: anroco

In a python str how to know the number of times repeat a string?

En un str python ¿como saber la cantidad de veces que se repite un string?
'''

#create a string
s = 'allows embedded "double" quotes.'
print(s)

#return the number of times it appears in the str.
count = s.count('l')
print (count)

#counts how many times that word appears
count = s.count('double')
print (count)

#str structure is equals to list, each character is an item and has an index.
#can be defined from that index must search.
count = s.count('e', 16)
print (count)

#can define a substring in which the search should be performed.
count = s.count('d', 7, 15)
print (count)
