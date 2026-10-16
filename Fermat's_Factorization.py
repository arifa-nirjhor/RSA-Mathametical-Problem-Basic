from math import isqrt

def fermat_factorization(n):

    if n < 2:
        raise ValueError("n must be grater than 1")

    if n % 2 == 0:
        return 2, n//2

    x = isqrt(n)

    if x * x < n:
        x += 1

    while True:
        y_squared = x * x -n
        y = isqrt(y_squared)

        if y * y == y_squared:
            return x - y, x + y

        x += 1


number = int(input("Enter a Number: "))

a , b = fermat_factorization(number)

print("Factors : ", a, "x", b)