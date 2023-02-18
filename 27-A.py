with open('27-A.txt')as f:
    s=list(map(int,list(f.readlines())))
    #print(s)
        
    rd=[x for x in range(1,6)]
    q=len(rd)//2
    #print(q)
    r=rd+rd
    #print(rd)
    for i in range(len(rd)):
        rd1=r[i:i+5]
        print(rd1)
        zt=[]
        for y in range(len(rd1)):
            zt.append(abs(q-y)*rd1[y])
        print(zt)
        
