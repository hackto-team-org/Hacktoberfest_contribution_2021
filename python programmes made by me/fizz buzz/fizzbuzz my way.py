# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 02:36:23 2019

@author: admin
"""
def fizzbuzz(r):
    for i in range (1,r):
        if (i%3==0):
            print(str(i)," = fizz")
        if (i%3==0 and i%5==0):
            print(str(i)," = fizzbuzz")
        if(i%5==0):
            print(str(i)," = buzz")
        else:
            print(str(i))

#a=int(input("enter the number"))
#if ((a==2)or(a==3)or(a==5)or(a==7)):
#    print("the number is prime no.")
#else:    
#    if ((a%2==0)or(a%3==0)or(a%5==0)or(a%7==0)):
#        print("the no. is not a prime no.")
#    else:
#        print("the no. is prime no.")
        
a=int(input("enter the number"))
#print("it is neither prime nor composite")
for i in range(2,a):
    if (a%i==0):
        print("it is not a prime no.")
        break
else:
    print("it is a prime no.")
#    
#a=int(input("enter the number"))
#c=1
#while(c==1):
#    for i in range(2,a):
#        if (a%i==0):
#            print("it is not a prime no.")
#print("it is a prime no.")
#n=1
#c=1
#while(c==1):
#    for i in range(n):
#        a=input("the cost is")
#        b=int(input("do you wanna add more,1 to continue"))
#        if (b==1):
#            n=n+1
#            c==1
#            d=int(a)
#            break
#        else:
#            
#            print("the total amount is",d*.1 ) 
#
#with open("sameer.txt") as myfile:
#    print (myfile.read())
#        
        
