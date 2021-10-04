# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 12:26:44 2021

@author: admin
"""


'''Sorting and find the max no.'''

#from array import *
#n=int(input("enter the array size"))
#arr=[]
#
#for i in range(n):
#    x=int(input("Enter no. "+ str(i+1) + " =>"))
#    arr.append(x)
#
#def sort(arr):
#    for i in range(1,n):
#        k=arr[i]
#        j=i-1
#        while(j>=0 and arr[j]>k):
#            arr[j+1]=arr[j]
#            j-=1
#        arr[j+1]=k
#        
#sort(arr)
#print("\n",arr)
#
#print("The max two no's are: " + str(arr[n-1]) + " and " + str(arr[n-2]))



'''Find the numbers whose sum is closest to 14'''

#from array import *
#n=int(input("Enter the size of the array"))
#arr=[]
#
#for i in range(n):
#    x=int(input("Enter no. "+ str(i+1) + " =>"))
#    arr.append(x)
#    
#def comp(arr):
#    nsum=arr[0]+arr[1]
#    if(nsum>=14):
#        diff_prev=nsum-14
#    elif(nsum<14):
#        diff_prev=14-nsum    
#
#    num1=arr[0]
#    num2=arr[1]
#    
#    for i in range(n):
#        for j in range(n):
#            if(i==j):
#                continue
#            nsum=arr[i]+arr[j]
#            if(nsum>=14):
#                diff_curr=nsum-14
#            elif(nsum<=14):
#                diff_curr=14-nsum
#                
#            if(diff_prev>diff_curr):
#                num1=arr[i]
#                num2=arr[j]
#                diff_prev=diff_curr
#    return num1,num2
#
#num1,num2=comp(arr)
#print("The values whose sum is closest to 14 are => " + str(num1) + " and " + str(num2))        
            

'''Sum of tens digit of elements of an array'''

#n=int(input("enter the size of the array"))
#arr=[]
#
#for i in range(n):
#    x=int(input("Enter no. "+ str(i+1) + " =>"))
#    arr.append(x)
#
#print(arr)   
#
#    
#def sum_first(arr):
#    s=0
#    for i in range(n):
#        p=int(arr[i]/10)
#        s=s+p
#    return s
#
#sum=sum_first(arr)
#print(sum)  
        
        
        
        
        
        
        
        
        