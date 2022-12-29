count=0
lst=['а','п','р','с','у']
for i in lst:
    for x in lst:
        for y in lst:
            for z in lst:
                for w in lst:
                    count+=1
                    v= str(i)+ str(x) + str(y) +str(z)+str(w)
                    if v[0]=='у'and 'аа' not in v and v.count('а')==2:
                        print(count)
                        
                        
                        

                    

                   
                
    