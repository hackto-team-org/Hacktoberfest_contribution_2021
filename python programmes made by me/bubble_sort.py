def bubble(a):
    n=len(a)
    
    for i in range(n):
        for j in range(0,n-i-1):
            if(a[j]>a[j+1]):
                a[j],a[j+1]=a[j+1], a[j]
    print(a)
                
a=[1,6,2,6,9,3,6]
bubble(a)