def fibanacci(n):
   if n<=1:
      return n
   else:
      return fibanacci(n-1)+fibanacci(n-2)
n=int(input("enetr a number"))
for i in range(n):
   print(fibanacci(i))
