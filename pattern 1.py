rows = 5
i = 0
for i in range(i,rows+1):
    for j in range(rows + 1 - i):
        print(' ',end = '')
    for j in range(i-1):
        print('*',end= '') 
    for j in range(i):
        print('*',end = '')
    print()   
