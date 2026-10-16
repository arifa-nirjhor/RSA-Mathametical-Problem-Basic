def euler_totient(n):
    if n < 1:
        raise ValueError("n must ber positive")

    result = n
    p = 2

    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p


            result -= result // p
        p += 1

    if n > 1:
        result -= result // n

    return result

number = int(input("Enter a positive integer: "))

print("Euler's Totient: ", euler_totient(number))
