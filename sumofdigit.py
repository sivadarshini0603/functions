l=[]
def sum_digits(b):
   if b==0:
      return 1
   dig=b%10
   l.append(dig)
   sum_digits(b/10)
n=int(input("enter a number"))
sum_digits(n)
print(int(sum(l)))
