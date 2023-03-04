with open('27-B.txt')as f:
    s=list(map(int,list(f.readlines())))
    #print(s)
    s.pop(0)   
    l=len(s)
    q=len(s)//2
    #print(q)
    r=s+s
    #print(s)
    start,finish,step=0,1000000,50000
while True:
    zt=[]
    for i in range(start,finish,step):
        rd1=r[i:i+l]
        cost=0
        #print(rd1)
        for y in range(len(rd1)):
            ind=y
            if y>=q:
                ind=l-y
            cost=cost+ind*rd1[y]
        zt.append(cost)
        print(i,cost)
        kilo=zt.index(min(zt))*step
    print(min(zt),zt.index(min(zt))*step)
    start,finish,step=start+kilo-step,start+kilo+step,step//10
    if step==0: step=1
