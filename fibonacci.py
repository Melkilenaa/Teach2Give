# Write a program to generate the Fibonacci sequence up to 100.

#using recursive function
def recFibo(n):
    if n <= 1:
        return n
    else:
        return(recFibo(n-1)+recFibo(n-2))
nterms = 100
if nterms <= 0:
   print("Enter an integer that is positive:")
else:
   print("The Fibonacci sequense is:")
   for i in range(nterms):
      print(recFibo(i))  