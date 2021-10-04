# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 13:42:14 2020

@author: admin
"""
from numpy import *
#Enter the size of the Matrix

size=int(input("Enter the size of the Matrix"))

arr1=array([],int)   #  A 2-D Matrix to store matrix  
flag=0

print("Enter the matrix elements")
#Taking input from user for matrix
for j in range(size):
    print("enter elements in row",j+1)
    x=list(map(int,input().split(" ")))      # Enter "size" no. of values separated by space( )
    arr1=append(arr1,x)
    
print(arr1)    

arr1=arr1.reshape(size,size)  #reshaping arr1 to 2-D array

print(arr1)
 
# Checking if rows have repeated elements
#----------------------------------------

for j in range(size):
    for k in range(size):
        for l in range(k+1,size):
            if(arr1[j][k]==arr1[j][l]):
                flag=1
                break
            else:
                continue
        if(flag == 1):
            break
    if(flag == 1):
        break


# Checking if columns have repeated elements
#-------------------------------------------            

for k in range(size):
    for j in range(size):
        for l in range(j+1,size):
            if(arr1[j][k] == arr1[l][k]):
                flag = 1
                break
        if(flag == 1):
            break
    if(flag == 1):
        break

if(flag == 0):
    print("Entered matrix is a latin matrix")
else:
    print("entered matrix is not a latin matrix")    
