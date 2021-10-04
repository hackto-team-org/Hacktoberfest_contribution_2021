import random

def choose():
    words=['rainbow','computer','science','programming','mathematics','player','condition','reverse','water','board']
    pick=random.choice(words)
    return pick

def jumble(word):
    jumbled="".join(random.sample(word,len(word)))
    return jumbled

def thank(p1n,p2n,p1,p2):
    print(p1n,"your score is:",p1)
    print(p2n,"your score is:",p2)
    print("thanks for playing")
    print("have a nice day")
        
def play():
    p1name=input("player 1,plz enter the name")
    p2name=input("player 2,plz enter the name")
    pp1=0
    pp2=0
    turn=0
    n=1
    while(n==1):
        #computer's task
        picked_word=choose()
        #create the question
        qn=jumble(picked_word)
        print(qn)
        #for player 1 
        if turn%2==0:
            print(p1name,"this is your turn")
            ans=input("what is on my mind?")
            if ans==picked_word:
                pp1=pp1+1
                print("your score is",pp1)
            else:
                print("better luck next time,the correct word is",picked_word)
            c=input("press 1 to continue or 0 to quit:")
            c=int(c)
            if c==0:
                thank(p1name,p2name,pp1,pp2)
                break
        #for player 2
        else:
            print(p2name,"this is your turn")
            ans=input("what is on my mind?")
            if ans==picked_word:
                pp2=pp2+1
                print("your score is",pp2)
            else:
                print("better luck next time,the correct word is",picked_word)
            c=input("press 1 to continue or 0 to quit:")
            c=int(c)
            if c==0:
                thank(p1name,p2name,pp1,pp2)
                break
        turn=turn+1    
play()
