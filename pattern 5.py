rows=5
k=1
for i in range(1,rows+1):
    for j in range(i):
        print(k,end='')
        k+=1
        if k>9:
            k=1
    print()    
