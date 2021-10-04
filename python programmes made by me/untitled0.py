# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 22:32:58 2019

@author: sameer
"""
#n=input("whats your choice")
#c=int(n)
#if(c==1):
   # print("so you are sameer")
    #input("whats your age")
#if(c==2):
   # print("ohho.......you are anshu ",input("whats your age"))

#new coding\  
#answer=0
#n=input("what tables you wanna recide")
#c=int(n)
#for i in range(3):
   # print(c,"X",i,"=",c*i)
#n=input("what tables you wanna recide")
#print(n)  
#for i in range(4):
#    print(n)
#(print("good morning everyone","lets start the day")
#n=1
#c=1
#while(c==1):
 #   print("patient no.",n,"plz come in")
 #   c=input("continue(0/1)")
 #   c=int(c)
 #   n=n+1
#print("thanks,this is end of our day")   



#LIST
#shop=["brush","curd","jam","kurkure"]
#print(shop)
#for c in shop:
 #   print(c)
#shop.append("maggi masala")
#for c in shop:
#    print(c)
#shop.append("pen")
#d=(shop[1:4])
#for c in d:
#   print(c)
    
#shop.insert(2,"ball")
#for c in shop:
 #  print(c)  
#print(len(shop))  \


#Day 3 
#shop=["brush","curd","jam","kurkure"]
#slicing
#c=print(shop[:4])
#for item in c:
 
#from statistics import mean
#from scipy import stats
#estimate=[1000,500,600,666,55,444,555,411,88,666,7777,3663,6584,98,996,7785,44,400,500,350,45,456,1123,556]
#estimate.sort()
#m=stats.trim_mean(estimate,.1)
#print(m)
#from scipy import stats
#import matplotlib.pyplot as plt
#estimate=[1000,500,600,666,55,444,555,411,88,666,7777,3663,6584,98,996,7785,44,400,500,350,45,456,1123,556]
#estimate.sort()
#plt.ylabel("ages")
#plt.xlabel("students")
#y=[]
#for i in estimate:
#    y.append(4)
#plt.plot(estimate,y,'r--')    
 
   
    
#date:-31/07/19     #permutation jumbled word game
import random
 
def choose():
    words=['umbrella','parrot','rope','towel','board','grapes','rainbow','computer','mouse']
    pick=random.choice(words)
    return pick

def jumble(word):
    jumbled="".join(random.sample(word,len(word)))
    return jumbled

def thanks(p1name,pp1,p2name,pp2):
    print(p1name,"your total score is",pp1)
    print(p2name,"your total score is",pp2)
    print("thanks for playing","have a nice day")
    
def play():
    p1name=input("player1 ,please enter your name")
    p2name=input("player2 ,please enter your name") 
    pp1=0
    pp2=0
    turn=0
    n=1
    while(n==1):
        #computer's task
        picked_word=choose()
        #creating the question
        qn=jumble(picked_word)
        print(qn)
        if turn%2==0:
            #for player1
            print(p1name,",","this is your turn")
            ans=input("what you think?,")
            if ans==picked_word:
                pp1=pp1+1
                print("your score is",pp1)
            else:
                print("betterluck next time","the correct word is",picked_word)
                c=input("press 1 to continue or 0 to exit")
                c=int(c)
                if c==0:
                    thanks(p1name,pp1,p2name,pp2)
                    break
        else:
            #for player2
            print(p2name,",","this is your turn")
            ans=input("what you think?,")
            if ans==picked_word:
                pp2=pp2+1
                print("your score is",pp2)
            else:
                print("betterluck next time","the correct word is",picked_word)
                c=input("press 1 to continue or 0 to exit")
                c=int(c)
                if c==0:
                    thanks(p1name,pp1,p2name,pp2)
                    break             
        turn=turn+1  
play()           