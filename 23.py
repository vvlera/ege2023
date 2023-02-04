from itertools import product
def f(x,y):
    count=0
    for i in range(1,10):
        pr= list(product('12', repeat=i))
        for g in pr:
            pr1=''.join(g)
            q=x
            for n in pr1:
                if n=='1': q+=1
                elif n=='2': q*=2
                
            if q==y:
                count+=1
    return count

print(f(1,10))
