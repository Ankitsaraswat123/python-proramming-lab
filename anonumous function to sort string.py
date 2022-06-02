def value(x):
    sum=0
    lst1=[]
    for i in range(x):
        sum=sum+ord(i)

    return sum
lst=['Vishnukant','Shubham','Jatin Gupta','Ashish']
out=value(lst)
print(out)
