'''def f(n):
    if n==1:
        return 1
    else:
        return f(n-1)+1      
print(f(3))
'''
'''def f(n):
    if n==1:
        return 1
    elif n%2==0:
        return n+f(n-1)
    elif n%2!=0 and n>1:
        return 2*f(n-2)
print(f(26))
'''   
'''def f(n):
    if n<3:
        return 2
    elif n>2 and n%2==0:
        return f(n-1)+f(n-2)-n
    elif n>2 and n%2!=0:
        return f(n-2)-f(n-1)+2*n
print (f(30))
'''
'''a=1
b=1
for i in range(1,2024):
   a*=i
for h in range(1,2021):
    b*=h
print(a//b)
'''
'''data=[34,2,65,4,87]
spisok=list(x for x in data if x>2)
print(spisok)    
'''
'''import random
sp= [random.randint(0,10) for i in range(0,10)]
print(sp)    
sp2=list(map(str,sp))
print(sp2)
'''    
with open('текстовый файлик.txt')as f:
    sp=f.readline().split()
    sp=[int(x) for x in sp]
    #sp=list(map(int, f.readline()))
    print(sp)
    
