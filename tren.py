from functools import reduce
a=reduce(lambda x,y: x+y,[1,3,4,5,6,7,8,9]) #reduce(function,consequence) - функция, применяемая к элементам последовательности и сводящая их к одному числу
print(a)

b=list(filter(lambda c: c>3,[1,2,3,4,5,6,7,8,9,0])) # filter(function,consequence)- позволяет отфильтровать элементы последовательности по условию
print(b)

v=[3,6,9,4,6,2]
d=list(map(str,v))# map(function,consequence)- преобразование элементов последовательности к какому-либо типу
print(d)

def nums(n):
    for i in range(n):
        yield i
#a=nums(10)
a=reduce(lambda x,y: x+y,nums(10))
print(a)
#for i in a:
    #print(i)

