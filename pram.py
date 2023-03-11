l = [x for x in range(0,21)]
l= l[::-1]
print(l)
q= len(l)//2
l1 = []
left,right = 0, len(l)
#print(left,right)
while len(l1)!=2:
    l1 = l[left:right]
    ww= len(l1)//2
    w1,w2= l[ww], l[ww+1]
    if w1<w2:
        right -= ww
    elif w1>w2:
        left += ww
    '''print(w1,w2)
    print(left,right)'''
print(l1[0]) if l1[0]<l1[1] else print(l1[1])


