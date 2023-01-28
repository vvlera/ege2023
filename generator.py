a=['2','3','4']
b=[(i,f) for i,f in enumerate(a)]
p= ['2','3','5']
c= [i+j for i,j in zip(a,p)]
print(c)
