with open('C:/Users/student/Documents/142Б/9.txt') as f:
    s=f.readlines()
    #print(s)
    for i in range (len(s)):
        s[i]=s[i].replace(';',' ')
    #print(s)
    sp=list(map(int,s))
    #print(sp)
    
    for a in sp:
        res6=[]
        res6= sp[0:6]
        print(res6)
        
        
    
    
    


