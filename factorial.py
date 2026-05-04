def fact(n):
   if n==0:
      r=1
   else:
      r=n*fact(n-1)
   return r
num=int(input("enter a number"))
s=fact(num)
print("factorial",s)
