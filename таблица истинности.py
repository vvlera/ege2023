for w in range(0,2):
    for x in range(0,2):
        for y in range(0,2):
            for z in range(0,2):
                F=(not(y<=x)or (z<=w) or(not(z)))
                print(w,x,y,z)

#yxzw