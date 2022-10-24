s=[]
for n in range(1,1000):
    if n%2!=0 and n%3!=0 and n%5!=0 and n%7!=0 and n%n**0.5!=0:
        print(n)
        s.append(n)
for i in s:
    for x in range(1,100):
        if x*4+117==i:
            print(x,i)