a = int(input("Enter a: "))
b = int(input("Enter b: "))

n = int(input("Enter Modulus n: "))

if n <= 0:
    print("Modulus Must be positive")
else:
    print("Addition:", (a+b) % n)
    print("Subtraction:", (a-b) % n)
    print("Multiplication:", (a * b) % n)
    print("Exponentiation:", pow(a, b, n))

    try:
        print("Inverse of a:", pow(a, -1, n))
    except ValueError:
        print("Modular Inverse Does Not Exist.")