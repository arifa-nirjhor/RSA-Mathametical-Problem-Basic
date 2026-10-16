def gcd(a,b):

    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    return abs(a)


num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

result = gcd(num1, num2)

print("GCD = ", result)