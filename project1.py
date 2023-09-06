#program to find factorial of a number
n=int(input("Enter A Number:"))  
def fact(n):
  if(n==0):
   return 1
  else:
    return n*fact(n-1)
print("Factorial of",n,"is",fact(n))
  



