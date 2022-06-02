#factorial of a given number
def factorial(n):
    f=1
    for i in range(1,n+1):
        f*=i
    print(f)
n=int(input('please enter a number'))
factorial(n)
