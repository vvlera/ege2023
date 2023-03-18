with open('27-A_1.txt')as f:
    n=f.readlines()
    n.pop(0)
    pr= []
    sum = 0
    for i in n:
        pr.append(list(map(int,i.split())))
    rz= []
    for x,y in pr:
            rz.append(abs(x-y))
            sum =sum + max(x,y)
    if sum%5==0:
        sum= sum-min(rz)
    print(sum)
    
