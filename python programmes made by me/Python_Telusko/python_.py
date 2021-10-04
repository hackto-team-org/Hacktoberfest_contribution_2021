# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 20:17:25 2020

@author: admin
"""


#x,y,z=int(input("enter x")),int(input("enter y")),int(input("enter z"))
#if (x>y):
#    if(x>z):
#        print("x is greatest =>",x)
#    else:
#        print("z is greatest =>",z)
#else:
#    if(y>z):
#        print("y is greatest =>",y)
#    else:
#        print("z is greatest =>",z)
#print("bye")
#    

#i=0
#x=input("enter a name")
#while(i<=len(x)-1):
#    print(x[i],x)
#    i+=1
#
#
#i=5
#while(i>0):
#    j=1
#    print("sam ",end="")
#    while(j<5):
#        print("rocks ",end="")
#        j+=1
#    i-=1     
#    print()
#    
#    
#x=0
#y=1
#print("0 1 ",end="")
#for i in range(50):
#    z=x+y
#    x=y
#    y=z
#    print(y)
#'''  
#    
#'''
#for Number in range (1, 101):
#    count = 0
#    for i in range(2, Number):
#        if(Number % i == 0):
#            count = count + 1
#            break
#
#    if (count == 0 and Number != 1):
#        print(" %d" %Number, end = '  ')
#        
   
#for i in range(4):
#    for j in range(4-i):
#        print("# ",end="")
#    print()          
#    


#for i in range(1,5):
#    for j in range(5-i):
#        print(i,end="")
#        i+=1
#    print()    
#print()
#
#
#for i in range(4):
#    num=65
#    for j in range(i+1):
#        ch=chr(num)
#        print(ch,end="")
#        num=num+1
#        
#    num=80+(i)    
#    for k in range(3-i):
#        ch=chr(num)
#        print(ch,end="")
#        num+=1
#    print()    
# 
#
#
#print()
#for i in range(1,5):
#      for j in range(i,5):
#            print(j,end="  ")
#      print()
 
'''array introduction'''
   
#from array import *
#
#value=array("i",[1,2,3,4,5])
#print(value.buffer_info())     
#print(value.append(77))                    
#print(value.extend([6,7,8,9]))               
#print(value.itemsize)
#print()
#
#newarr=array(value.typecode,(x for x in value))
#
#for i in newarr:
#    print(i)
#    
#print()   
#newarray=value
##print(newarray)
#for i in newarray:
#    print(i)

'''sorted array'''

#from array import *
#
#arr=array('u',['p','e','a','w'])
#arr=sorted(arr)
#print(arr)
#from math import factorial
#x=int(input("enter the no."))
#print(factorial(x))
#

''' entering elements into an empty array'''

#from array import *
#
#arr=array('i',[])  
#n=int(input("enter the lenth of array"))
#
#for i in range(n):
#    x=int(input("enter the i+1 number"))
#    arr.append(x)
#
#print(arr)    

'''searching an element in an array'''

#from array import *
#
#arr=array('i',[])  
#n=int(input("enter the lenth of array"))
#
#for i in range(n):
#    x=int(input("enter the number"))
#    arr.append(x)
#
#num=int(input("enter the no. which you want to search"))
#
#for i in range(n):
#    if(arr[i]==num):
#        print("no is at index ",i+1)
#        break
#else:
#    print("no.is not in the array")

'''deleting an element from a given position'''

#from array import *
#
#arr=array('i',[])  
#n=int(input("enter the lenth of array"))
#
#for i in range(n):
#    x=int(input("enter the number"))
#    arr.append(x) 
#
#pos=int(input("enter index position"))
#
#for i in range(n):
#    if(i>=pos and i<n-1):
#        arr[i]=arr[i+1]
#
#for i in range(n-1):
#    print(arr[i])
#    
'''deleting an element from a given position(method 2)'''

#import array as a

#arr=a.array("i",[])
#lent=int(input("Enter the length of array : "))
#for i in range(lent):
#    val=int(input("Enter the elements of array one by one and press enter"))
#    arr.append(val)
#print(arr)
#arr2=a.array('i',[])
#del_elm=int(input("Enter the element you wish to remove/delete : "))
#for element in arr:
#    if del_elm==element:
#        continue
#    else:
#        arr2.append(element)    

'''reversing an array'''

#from array import *
#
#arr=array('i',[])  
#n=int(input("enter the lenth of array"))
#
#for i in range(n):
#    x=int(input("enter the number"))
#    arr.append(x)
#''' slicing technique  is used'''
#arr=arr[::-1]
#print(arr)
#
#arr.reverse()
#print(arr)

''' DIFFERENT METHODS OF MAKING AN ARRAY'''
''' ------------------------------------'''
'''NUMPY array'''

'''1. using "array()" '''

#from numpy import *
#
#arr=array([1,2,3],int)
#arr2=array([4,5,6.04])

'''type casting float value 6.04 into int'''

#arr3=array([4,5,6.04],int)
#
#print(arr.dtype)
#print(arr2.dtype)
#print(arr3.dtype)
#
#print()
'''2. using "linspace()" '''
#
#arr=linspace(0,15,12)
#print(arr)
#
#print()

'''3. using "arange"'''
#arr=arange(0,15,2)
#print(arr)
#
#print()

'''4. using "logspace()"'''
#arr=logspace(0,15,5)
#print(arr)
#print('%.2f' %arr[0])
#
#print()

'''5 & 6 using "zeros() & ones()"'''
#arr=zeros(3)
#print(arr)
#arr=ones(4,int)
#print(arr)
#
#print()
#    
'''adding a constant to each element of an array'''

#from numpy import *
#
#arr=array([1,6,3,4])
#
#for i in range(len(arr)):
#    arr[i]=arr[i]+5
#
#print(arr)    
#
#arr=arr+5
#print(arr)
#
'''COPYING AN ARRAY WITH DIFFERNT ID (ADDRESS)'''

#from numpy import *
#
#arr1=array([1,2,3,4])
#'''shallow copy'''
#arr2=arr1.view()
#arr1[1]=9
#
#print(arr1)
#print(arr2)
#print(id(arr1))
#print(id(arr2))
#
#'''deep copy'''
#
#from numpy import *
#
#arr1=array([1,2,3,4])
#arr2=arr1.copy()
#arr1[1]=9
#
#print(arr1)
#print(arr2)
#print(id(arr1))
#print(id(arr2))

'''MULTIDIMENTIONAL ARRAY'''
'''----------------------'''

#from numpy import *
#
#arr1=array([
#        [1,2,3,7,8,9],
#        [4,5,6,10,11,12]
#        ])
#print(arr.ndim)
#
#arr2=arr1.flatten()
#print(arr2)
#arr3=arr1.reshape(3,4)
#print(arr3)
#arr3=arr3.reshape(1,12)
#print(arr3)

'''MAKING A 3D ARRAY FROM 2D ARRAY'''

#from numpy import *
#
#arr1=array([
#        [1,2,3,7,8,9],
#        [4,5,6,10,11,12] 
#        ])    
#    
#arr3=arr1.reshape(2,2,3)  
#print(arr3)  

'''MAKING A MATRIX'''

#from numpy import *

#arr1=array([
#        [1,2,3],
#        [5,6,7],
#        [8,9,10]
#        ])
#arr2=array([
#        [1,2,3],
#        [7,8,9],
#        [4,6,2]
#        ])
#    
#arr1=matrix(arr1)
#arr2=matrix(arr2)
#
#arr3=arr1 + arr2
#print(arr3)
#
#arr3=arr1 * arr2
'''matrix from user input (IMPORTANT) '''


#from numpy import *
#
#
#n=int(input("enter the no. of values"))
#
#arr1=array([],int)
#arr2=array([],int)
#
#lst1=[]
#lst2=[]
#
#for i in range(n):      
#    ele=int(input("enter the no."))
#    lst1.append(ele)
#    
#for i in range(n):      
#    ele=int(input("enter the no."))
#    lst2.append(ele)    
#    
#print(lst1)
#print(lst2)    
#
#print()
#
#arr1=append(arr1,lst1)
#arr2=append(arr2,lst2)
#
#print()
#print(arr1)
#print(arr2)    
#
#arr1=arr1.reshape(2,2)
#arr2=arr2.reshape(2,2)
#matrix(arr1)
#matrix(arr2)
#
#arr3=arr1 * arr2
#print(arr3)

'''keyworded variable length argument'''

#def person(name,**data):
#    print(name)
#    print(data)
#    
#    for i,j in data.items():
#        print(i,j)
#        
#person('sam',age=20,city='BHILAI')    

'''concept of local and global variable'''
#a=10
#
#def something():
#    a=5
#    '''storing a value of flobal variable '''
#    x=globals()['a']
#    print("value of x",x)
#    print("in fun",a)
#    
#    globals()['a']=15
#    
#something()
#print("outside",a)

'''counting even and odd no. in a list'''

#lst=[]
#click='y'
#while(click=='y'):
#    x=int(input("enter the values in lst"))
#    lst.append(x)
#    click=input("do you want to continue,press 'y'")
#print(lst)    
#    
#def even_odd(lst):
#    
#    even=0
#    odd=0
#    
#    for i in lst:
#        if(i%2==0):
#            even+=1
#        else:
#            odd+=1
#    
#    return even,odd
# 
#even,odd=even_odd(lst)    
#
#print("even = ",even," odd = ",odd)    
#    
#print("Even : {} and Odd : {}".format(even,odd))    
#    
    
''' recursion'''

#from sys import *
#setrecursionlimit(1000)
#print(getrecursionlimit())
#
#i=1
#def greet():
#    global i
#    i+=1
#    print("hello",i)
#    greet()
#    
#greet()    
#    
    
#def fact(n):
#    if (n==0 or n==1):
#        return 1
#    else:
#        return n * fact(n-1)
#fact=fact(5)
#print("FACT : {}".format(fact))    

'''FILTER'''

#from functools import *
#def is_even(a):   
#    return a%2==0
#
#lst=[1,2,3,4,5,6,7,8]
#
#evens=list(filter(is_even,lst))
#print(evens)
#
#'''OR using lambda and filter, map, reduce  '''
#
#from functools import *
#lst=[1,2,3,4,5,6,7,8]
#
#evens=list(filter(lambda n : n%2==0,lst))
#print(evens)
#
#divide=list(map(lambda n : n/2,evens))
#print(divide)
#
#sub=reduce(lambda a,b : a+b,divide)
#print(sub)



'''Decorator'''
'''---------'''

'''using decorator we can add functionality to a function without actually changing its block content'''

#def div(a,b):
#    print(a/b)
#    
#'''taking  div function as parameter as func'''
#    
#def smart_div(func): 
#        
#    def inner(x,y):
#        if x<y:
#            x,y=y,x
#            return func(x,y)
#        else:
#            return func(x,y)
#    return inner
#    
#                                                 
#div1=smart_div(div)
#
#div1(2,4)

'''MODULES=> new python files which are interconnected just like html and css'''
'''there is a seperate module for this "python_module1.py" which is imported here'''

#from python_module1 import add   
#
#a=2
#b=3
#
#result=add(a,b)
#print(result)

'''special variable"__name__"''' 
#
#from python_module1 import *
#print("hello" +  __name__)

'''more things with module'''

#from python_module1 import *
#def main():
#    print("hello")
#
#if(__name__ == "__main__"):
#    main()

'''Object Oriented Programming '''
'''---------------------------'''

'''Class AND Object'''

'''Declaration of class'''
#
#class student:
#    
#    ''' "self" is must to put'''
#    
#    def properties(self):
#        name = input("enter name")
#        roll = int(input("enter roll no."))
#        print("name =",name,"roll no. =",roll)
#        
'''declaration of objects'''
#
#
#stud1=student()
#stud2=student() 
#
#'''calling function'''
#
'''method 1'''
#student.properties(stud1)
#student.properties(stud2)
#
'''method 2'''
#stud1.properties()
#stud2.properties()     


'''__init__(self) in the previous code'''

#class student:
#    
#    ''' "self" is must to put'''
#    
#    '''__init__ automatically called(constructor)'''
#    
#    def __init__(self,name,roll):
#        
#        '''variables names can be same,it can be self.name = name'''
#        
#        self.x = name
#        self.y = roll
#            
#    def properties(self):
#        print("name =",self.x,",roll no. =",self.y)
#
'''passing parameters in __init__'''
#
#stud1=student('Sam',1)
#stud2=student('har',2) 

#stud1.properties()
#stud2.properties()     

'''manupulation in above program'''

#class student:
#    
#    ''' "self" is must to put'''
# 
#    '''__init__ automatically called(constructor)'''
#    
#    def __init__(self,name,roll):
#        
#        '''variables names need not to be same,it can be self.x = name'''
#        
#        self.name = name
#        self.roll = roll
#    
#    def compare(self,other):
#        if(self.roll == other.roll):
#            return True
#        else:
#            return False
#        
#    def properties(self):
#        print("name =",self.name,",roll no. =",self.roll)
#
'''passing parameters in __init__'''
#
#stud1=student('Sam',1)
#stud2=student('har',2) 
#
#stud1.roll= 30
#
'''now comapring stud1 and stud2 if both roll no. are same'''
#if(stud1.compare(stud2)):
#    print("they are same")
#else:
#    print("they are not same")
#    
#
#stud1.properties()
#stud2.properties()     


'''types of variables'''
#
#class car:
#    
#    '''class variable'''
#    wheels=4
#    
#    '''variables outside __init__ are class variables and inside it are instance variables'''
#    def __init__(self):
#        self.mil=10
#        self.comp="AUDI"
#
#obj1=car()
#obj2=car()
#
#car.wheels=5
#
#obj1.mil=8
#
#print(obj1.mil,obj1.comp)
#print(obj2.mil,obj2.comp)

'''types of METHODS'''
'''-------------------'''
'''1. INSTANCE method'''

#class student:
#    school="BSP"
#    
#    def __init__(self,m1,m2,m3):
#        self.m1=m1
#        self.m2=m2
#        self.m3=m3
#        
#    def avg(self):
#        return (self.m1 + self.m2 + self.m3)/3
#        
#    '''subtype of INSTANCE method'''
#    '''1. ACCESOR(getters) method'''
#        
#    def get_m1(self):
#        return self.m1
#        
#    '''2. MUTATORS(setters) method'''
#    
#    def set_m1(self,value):
#        self.m1=value
#            
#
#s1 = student(10,20,30)
#s2 = student(40,50,60)
#
#print(s2.get_m1())

'''2.CLASS method'''

#class student:
#    school="BSP"
#    
#    def __init__(self,m1,m2,m3):
#        self.m1=m1
#        self.m2=m2
#        self.m3=m3
#        
#    def avg(self):
#        return (self.m1 + self.m2 + self.m3)/3
#    
#    ''' "cls"  keyword is used when we use class method and we have to use a decorator before method "@classmethod" '''
#               
#    @classmethod    
#    def get_school_name(cls):
#        return cls.school
#    
#    
#s1 = student(10,20,30)
#s2 = student(40,50,60)
#
#print(student.get_school_name())


'''3.STATIC method'''

#class student:
#    school="BSP"
#    
#    def __init__(self,m1,m2,m3):
#        self.m1=m1
#        self.m2=m2
#        self.m3=m3
#        
#    def avg(self):
#        return (self.m1 + self.m2 + self.m3)/3
#    
#    ''' no keyword is used and we have to use a decorator before method "@staticmethod" '''
#               
#    @staticmethod    
#    def info():
#        print("hello, this is static method")
#    
#    
#s1 = student(10,20,30)
#s2 = student(40,50,60)
#
#student.info()


'''class inside a class'''

#class student:
#    
#    def __init__(self,name,rollno,brand):
#        self.name=name
#        self.rollno=rollno    
#        '''using this we can create objects of laptop class'''
#        self.lap=self.laptop(brand)
#        
#    def show(self):
#        print(self.name,self.rollno)
#        self.lap.show()
#    '''class inside a class'''
#    class laptop:
#        
#        def __init__(self,brand):
#            self.brand=brand
#            self.cpu="i5"
#            self.ram=8
#        
#        def show(self):
#            print(self.brand,self.cpu,self.ram)
#
#s1=student('sam',1,"asus")
#s2=student('har',2,"hp")
#            
#'''creating inner class object'''
#
#lap1=s1.lap
#lap2=s2.lap
#
#s1.show()
#lap1.show()


'''INHERITANCE'''

#class A:
#    def feature1(self):
#        print("feature 1 is working")
#    
#    def feature2(self):
#        print("feature 2 is working")
#      
#        '''single level inheritance'''
#class B(A):
#    def feature3(self):
#        print("feature 3 is working")
#    
#    def feature4(self):
#        print("feature 4 is working") 
#
#        '''multi level inheritance'''
#class C(B):
#    def feature5(self):
#        print("feature 5 is working")
#    
#    def feature6(self):
#        print("feature 6 is working")
#        
#        
#a1=A()
#
#b1=B()
#
#c1=C()
#
#a1.feature2()
#
#b1.feature1()
#        
#c1.feature6()

'''multiple inheritance'''
#class A:
#    def feature1(self):
#        print("feature 1 is working")
#    
#    def feature2(self):
#        print("feature 2 is working")
#      
#        '''single level inheritance'''
#class B:
#    def feature3(self):
#        print("feature 3 is working")
#    
#    def feature4(self):
#        print("feature 4 is working") 
#
#        '''multiple inheritance'''
#class C(A,B):
#    def feature5(self):
#        print("feature 5 is working")
#    
#    def feature6(self):
#        print("feature 6 is working")
#        
#  
#a1=A()
#
#b1=B()
#
#c1=C()
#
'''class A and class B are two different classes'''
#a1.feature2()
#
#b1.feature4()
#        
#c1.feature6()        

'''constuctor in inheritance'''

#class A:
#   
#    def __init__(self):
#        print("In A init")
#        
#    def feature1(self):
#        print("feature 1-A is working")
#    
#    def feature2(self):
#        print("feature 2 is working")
#     
#class B:
#    
#    def __init__(self):
#        print("In B init")
#        
#    def feature1(self):
#        print("feature 1-B is working")
#    
#    def feature4(self):
#        print("feature 4 is working") 
#        
#        
#'''concept of Method Resolution Order(MRO)'''       
#'''here A is written first i.e. C(A,B) therefore, A's init is executed'''
#class C(A,B):
#    
#    def __init__(self):
#        super().__init__()
#        print("In C init")   
#    
#    def feat(self):
#        super().feature4() 
#        
#
#c1=C()
#
#c1.feature1()
#
#c1.feat()

'''DUCK TYPING'''

'''Python program to demonstrate''' 
'''DUCK TYPING'''
  
  
#class Bird: 
#    def fly(self): 
#        print("fly with wings") 
#  
#class Airplane: 
#    def fly(self): 
#        print("fly with fuel") 
#  
#class Fish: 
#    def swim(self): 
#        print("fish swim in sea") 
#  
#''' Attributes having same name are considered as duck typing'''  
#
#for obj in Bird(), Airplane(), Fish(): 
#    obj.fly() 

'''one more example of """DUCK TYPING"""'''
#class spyder:
#    
#    def execute(self):
#        print("compiling")
#        print("running")
#
#class pycharm:
#    
#    def execute(self):
#        print("compiling")
#        print("running")
#        print("executing")
#        
#class laptop:
#    
#    def code(self,ide):
#        ide.execute()
#        
#spy = spyder()
#
#py =  pycharm()
#
#lap1= laptop()
#
#lap1.code(spy)    
#lap1.code(py)


'''more in previous code'''

#
#class spyder:
#    
#    
#    def __init__(self):
#        print("compiling")
#        print("running")
#        
#    def execute(self):
#        pass
#
#class pycharm:
#
#    def __init__(self):
#        print("compiling")
#        print("running")
#        print("executing")
#        
#    def execute(self):
#        pass
#    
#class laptop:
#    
#    def code(self,ide):
#        ide.execute()
#        
#spy = spyder()
#
#py =  pycharm()
#
#lap1= laptop()
#
#lap1.code(spy)
#lap1.code(py)

'''OPERATOR OVERLOADING'''

#class student:
#    
#    def __init__(self,m1,m2):
#        self.m1=m1
#        self.m2=m2
#        print("hello")
#        
#    def __add__(self,other):
#        
#        m1=self.m1+other.m1
#        m2=self.m2+other.m2
#        print("yo")
#        s3= student(m1,m2)
#    
#        return s3
#    
#    def __sub__(self,other):
#        
#        m1=self.m1-other.m1
#        m2=self.m2-other.m2
#        print("yo 2")
#        s4= student(m1,m2)
#
#        return s4
#    '''__ge__ means graeter than equal to'''
#    def __gt__(self,other):
#        r1= self.m1+self.m2
#        r2= other.m1+other.m2
#        print("yo 3")
#        
#        if(r1>r2):
#            return True
#        else:
#            return False
#    
#    def __str__(self):
#        
#        return "{} {}".format(self.m1,self.m2)
#    
#''' so here we are overriding buildin functions  like __add__ ,etc "'''
#
#s1 = student(70,80)
#s2= student(30,40)
#
#s3 = s1+s2
#print(s3.m2)
#
#s4 = s1-s2
#print(s4.m2)
#
#print(s1.m1+s1.m2)
#
#'''checking greater'''
#
#if (s1>s2):
#    print("s1 wins")
#else:
#    print("s2 wins")    
#
#print(s1)

'''METHOD OVERLOADING'''
'''python doesnot support method overloading''' 

'''METHOD OVERRIDING'''
#
#class A:
#    def show(self):
#        print("hello A")
#        
#class B(A):
#    '''here B is having it's own show() therefore it is calling that,otherwise if we comment B's show() it will call A's show(),this is method overriding'''
#    
#    def show(self):
#        print("hello B")      
#        
#b1=B()
#b1.show()        


'''ABSTRACT CLASSES and ABSTRACT METHODS'''
#
#from abc import ABC,abstractmethod
#
#'''ABC is an abstract class argument and @abstractmethod is a decorator''' 
#
#class computer(ABC):
#     @abstractmethod
#     def process(self):
#         pass
#
#class laptop(computer):
#     def process(self):
#         print("in laptop()")
#
#class whiteboard(computer):
#    def process(self):
#        print("in abstract's process whiteboard")
#    def write(self):
#        print("in whiteboard()")
#        
#class programmer:
#    
#    def work(self,com):
#        print("in programmer()")
#        com.process()
#        
#lap=laptop()
##lap.process()
#
#prog=programmer()
#
#brd=whiteboard()
#
#prog.work(brd)

'''ITERATORS'''
'''---------'''
'''iterator basic prog'''

#nums=[1,2,3,4,5,6]
#
#it=iter(nums)
#
#print(it.__next__())
#
#print("hello")
#print(it.__next__())
#
#'''or it can be also used as'''
#
#print(next(it))


'''ITERATOR prog, making our own object for iteration'''

#class topten:
#    
#    def __init__(self):
#        self.num=1
#        
#    '''to iterate values we need __iter__'''
#    def __iter__(self):
#        return self
#    '''the for loop internally uses __next__ function'''
#    def __next__(self):
#        if(self.num<=100 ):
#            val=self.num
#            self.num += 10
#            return val
#        else:
#            '''we can't use break here bcz their is no loop,therefore we use:-'''
#            raise StopIteration
#        
#values=topten()
#
#print(values.__next__())
#
#for i in values:
#    print(i)        


'''GENERATOR --> Gives ITERATOR'''
#
#def topten():
#    return 1
#    '''these return doesn't execute because return 1 is executed and func. terminated'''
#    return 2
#    return 3
#
#values=topten()
#print(values)
'''but with YIELD'''

#def topten():
#    yield 1
#    yield 2
#    yield 3
#
#values=topten()
#
#for i in values:
#    print(i)
    
'''generators returning squares of no's'''
    
#def fabonicci():
#    n=0
#    m=1
#    res=0
#    yield 0
#    yield 1
#    
#    while(res<20):
#        res=n+m
#        n=m
#        m=res
#        yield res
#
#values=fabonicci()        
#
#for i in values:
#    print(i)

'''EXCEPTION HANDLING'''
#a=5
#b=3
#
#try:
#    print("resource open")
#    print(a/b)
#    k= int(input("enter a no."))
#    print(k)
#    
#except ZeroDivisionError as e:
#    print("hey,you cannot divide a no.by zero",e)
#
#except ValueError as e:
#    print("you cannot pass a character",e)
#    
#except Exception as e:
#    print("this except all kind of error",e)     
#
#finally:
#    print("resource closed")


'''MULTITHREADING---->> A VERY AWESOME CONCEPT'''

#from threading import *
#from time import sleep
#
#class hello(Thread):
#    def run(self):
#        for i in range(5):
#            print("Hello")
#            sleep(1)
#            
#class hi(Thread):
#    def run(self):
#        for i in range(5):
#            print("Hi")
#            sleep(1)
#            
#t1=hello()
#t2=hi()
#
#t1.start()
#sleep(0.2)
#t2.start()

'''FILE HANDLING'''
#
#f = open(r'C:\Users\admin\Desktop\sameer_info.txt','a')
#f.write("\nI live in Bhilai")

'''Linear Search'''

#from array import array
#
#arr=array('i',[])
#
#n=int(input("enter the size of array"))
#
#for i in range(n):
#    x=int(input("enter the number"))
#    arr.append(x) 
#    
#k=int(input("enter the value you want to search"))
#
#for i in range(len(arr)):
#    if(arr[i]==k):
#        print(k," is in index",i+1)
#        break
#else:
#    print(k," is not found")        
#print(arr)

'''BINARY SEARCH'''
#from array import *
#
#arr=array('i',[])
#
#n=int(input("enter the size of array"))
#
#for i in range(n):
#    x=int(input("enter the number"))
#    arr.append(x) 
#
#arr=sorted(arr)
#print(arr)
#    
#num=int(input("enter the value you want to search"))
#
#lb=0
#ub=len(arr)-1
#   
#while lb <= ub: 
#
#        mid = (lb + ub)//2 
#          
#        # Check if x is present at mid 
#        if arr[mid] == num: 
#            print(num," is at",mid+1)
#            break
#  
#        # If x is greater, ignore left half 
#        elif arr[mid] < num:
#            lb = mid + 1
#  
#        # If x is smaller, ignore right half 
#        else: 
#            ub = mid - 1
#else:
#    print("not found")            

'''BUBBLE SORT'''

#from array import *
#
#arr=array('i',[])
#
#n=int(input("enter the size of array"))
#
#for i in range(n):
#    x=int(input("enter the number"))
#    arr.append(x) 
#    
#print(arr)    
#
#                         #swapping
#def bub_sort(arr):
#    
#    for i in range(len(arr)):
#        for j in range(len(arr)-1):
#            if(arr[j]>arr[j+1]):
#                temp=arr[j+1]
#                arr[j+1]=arr[j]
#                arr[j]=temp     
#
#
#bub_sort(arr)
#print(arr)

'''SELECTION SORT'''

#from array import *
#
#arr=array('i',[])
#
#n=int(input("enter the size of array"))
#
#for i in range(n):
#    x=int(input("enter the number"))
#    arr.append(x) 
#
#
#def selection_sort(arr):
#
#    for i in range(len(arr)-1):
#        minpos=i
#        for j in range(i+1,len(arr)):
#            if(arr[minpos]>arr[j]):
#                minpos=j
#                
#        temp=arr[i]
#        arr[i]=arr[minpos]
#        arr[minpos]=temp     
#        print(arr)
#            
#selection_sort(arr)
#print("\n",arr)           

''' Insertion Sort'''
#from array import *
#n=int(input("enter the value of n"))
#arr=array('i',[])
#
#for i in range(n):
#    x=int(input("enter the number"))
#    arr.append(x)
#
#def insertion_sort(arr):
#    for i in range(1,n):
#        key=arr[i] 
#        j=i-1
#        while(j>=0 and arr[j]>key):
#            
#            arr[j+1]=arr[j]
#            j-=1
#            
#        arr[j+1]=key
#insertion_sort(arr)
#print("\n",arr)        

'''Quick Sort'''
from array import *
n=int(input("enter the value of n"))
arr=array('i',[])

for i in range(n):
    x=int(input("enter the number"))
    arr.append(x)   
    

            
'''Class example'''
#class A:
#    def show(self):
#        print("hello")
#        
#    def show11(self):
#obj1=A()
#
#obj1.show11()     

'''Split function'''

#x = list(map(int, input("Enter a multiple value: ").split(" ")))    #input values  with spaces, we can use "," also or anything
#print("List of students: ", x)   

