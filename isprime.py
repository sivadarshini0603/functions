def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input("Enter a number: "))
flag = False

for i in range(2, n // 2 + 1):
    if is_prime(i) and is_prime(n - i):
        print(f"{n} = {i} + {n - i}")
        flag = True

if not flag:
    print("Cannot be expressed as the sum of two prime numbers")
