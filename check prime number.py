#to check wheather the given number is prime or not
def prime_or_not(n):
    for i in range(2,n):
        
      if n%i==0:
          return True
      else:
          return False
n=int(input('please enter a number'))
prime_or_not(n)
