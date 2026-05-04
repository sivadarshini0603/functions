def calculator(a,b):
   su=a+b
   sub=a-b
   mul=a*b
   div=a/b
   mod=a%b
   return su,sub,mul,div,mod
a=int(input("enter a number"))
b=int(input("enter b number"))
c=calculator(a,b)
print("output")
for i in c:
   print(i)
