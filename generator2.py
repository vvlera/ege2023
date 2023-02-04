from itertools import chain
#b=[n*2 for n in a if n<3]
#b=[[i,f] for i,f in enumerate(a)]
#b=[i+j for i,j in zip(a,a2)]
''''a2=[5,6,7]
a= [1,2,3]
c=1
print('1')if c==1 else _
b=[('true'if n>2 else 'false')for n in a]
b2=[i+j for i in a for j in a2]
print(b,b2)
b3=[[i for i in range(1,n+1)] for n in a]
print(b3)'''
sp=[['a','m',[5,4,4]]]
sp2=['b','f',[5,5,5]]
sp3=['c','m',[2,1,2]]
'>=5'
#x=[[(name,'+ct' if sum(score)/len(score)==5 else '-ct')]for name,gender,score in sp]
a= sp+sp2+sp3
#print(a)
a= [*sp,*sp2,*sp3]
#print(a)
a=list(chain(sp,sp2,sp3))
#print(a)
s=[sp,sp2,sp3]
#print(s)
s=list(chain(n for n in s))
#print(s)
s=[0,2,1,23]
def f(x):
    return x**2
#print(f(5))
ff=lambda y,x: y*x
#print(ff(5,2))
a=[1,2,3,4,5]
f3= lambda x:1 if all(x) else 0
f4= lambda x:1 if any(x) else 0
b=list(map(str,a))
#print(f3(a), f4(a))
#print(b)

b= list(map(lambda x: str(a)+'l',a))
#print(b)
c='12345'
c1=list(map(lambda x: int(x)+1,c))
print(c1)

g= list(filter(lambda x: int(x)%2==0,c))
print(g)

