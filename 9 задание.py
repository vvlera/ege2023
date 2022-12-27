with open('c:\Users\Валерия\Documents\GitHub\inf\9.txt') as f:
    s=f.readlines()
    for i in range (len(s)):
        s[i]=s[i].replace(';',' ')
    #print(s)
    sp=list(map(int,s))
    #print(sp)
    x=y=0
    for a in range(len(sp)):
        x=y
        y=x+6
        res6=sp[x:y]
        print(res6)
        #input()
        for q in res6:
            if res6.count(q)==2:
                b = q                
                del res6[res6.index(q)]
                del res6[res6.index(q)]                
                #print(res6)
                otv=0
                if len(res6)==4:
                    if sum(res6[q])/len(res6)<=b*2:
                        otv+=1
                    else:
                        del res6

                else:
                    del res6  
            else:
                del res6
            print(otv)
                
            
    
        
        
            
        
        
        
    
    
    


