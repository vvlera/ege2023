x = [x for x in range(1,8)]
from math import factorial
#x = [1,2,3,4]
pr = 0
q=0
for y in x:
    if y%2==0:
        q+=1
q1=q-(q-1)
k = factorial(q)/(factorial(q-2)*2)
for i in range(1,len(x)):
    if x[i]%2==0 and x[i]<=2:
        pr+=len(x)-1
pr2=(pr-q1)*q
pr = pr2+k
print(pr2, int(k))
print(pr)

