with open('C:/Users/student/Documents/142Б/9.txt') as f:
    s=f.readlines()
    for i in range (len(s)):
       s[i]=s[i].replace(';',' ')
    sp=list(map(int,s))
    x=y=0
    otv=0
    while x<=len(sp):
        x=y
        y=x+6
        res6 = sp[x:y]
        print(res6)
        for q in res6:
            if res6.count(q)==2:
                b = q              
                del res6[res6.index(q)]
                del res6[res6.index(q)]                
                print(res6)    
            elif res6.count(q)>=2:
                for i in range(res6.count(q)):
                    del res6[res6.index(q)]
                print(res6)    
        if len(res6)==4:
            if sum(res6)/4<=b*2:
                otv+=1
                print(otv)
print(otv)   
                
            
    
        
        
            
        
        
        
    
    
    


