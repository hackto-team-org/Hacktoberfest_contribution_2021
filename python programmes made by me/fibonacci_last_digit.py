# -*- coding: utf-8 -*-
"""
Created on Tue May 19 13:26:07 2020

@author: admin
"""
#Fibonacci last digit
n=int(input())
n1=0
n2=1

for i in range(2,n+1):
    nex=n1+n2
    n1=n2
    n2=nex

print(nex%10)   