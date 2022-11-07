
for a in range(1,1000):
    F= True
    for x in range(1,100000):
        if ((x%2==0) <= (x%3!=0)) or (x+a>=100):
            F= True
        else:
            F= False
            break
    if F== True:
        print(a)
        break