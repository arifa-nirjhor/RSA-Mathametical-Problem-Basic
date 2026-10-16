def prime_facorization(n):
    factors = []
    divisor = 2

    while divisor * divisor <= n:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    if n>1:
        factors.append(n)

    return factors

number = int(input("Enter a Number: "))

if number < 2:
    print("Enter an integer greater than 1.")
else: 
    print("Prime Factors: ", prime_facorization(number))