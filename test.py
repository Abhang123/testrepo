# Fibonacci Series

def fibonacci_series():

  print("\n")
  mylist = []
  n = int(input("Enter the length of the fibonacci series list : "))
  print("\n")
  
  a = 0
  b = 1
  for i in range(n):
    mylist.append(a)
    a,b = b,a+b
  print(mylist)
  print("\n")

fibonacci_series()
