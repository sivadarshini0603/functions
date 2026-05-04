#module1.py
def fact(n):
     f = []
     for i in range(1, n + 1):
         if n % i == 0:
              f.append(i)
     return f

def isprime(n):
     if n < 2:
         return False
     for i in range(2, n):
         if n % i == 0:
             return False
     return True

def prime_fact(n):
     pf = []
     for i in range(1, n + 1):
         if n % i == 0 and isprime(i):
              pf.append(i)
     return pf
import module1
n = int(input("Enter number: "))
f = module1.fact(n)
pf = module1.prime_fact(n)
print(f"{'Factors':<15}", f)
print(f"{'Prime factors':<15}", pf)
