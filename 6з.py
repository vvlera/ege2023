for x in range(10000):
    s=x
    s= (s-21)//10
    n=1
    while s>0:
        n=n*2 
        s=s-n
    if n==32:
        print(x)
        break

'''for i in range(0,3):
    for x in range(0,3):
        for y in range(0,3):        
            z=str(i)+str(x)+str(y)
            print(z) '''  

'''from itertools import product
for i,x,y in product(range(0,3),range(0,3),range(0,3)):
    s=str(i)+str(x)+str(y)
    print(s)'''
    
