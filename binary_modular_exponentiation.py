
def binary_modular_exponentiation(base, exponent, modulus):

    if modulus <= 0:
        raise ValueError("Modulus must be positive.")

    if exponent < 0:
        raise ValueError("Exponent must be non-negative.")

    result = 1 % modulus
    base = base % modulus

    while exponent > 0:

        if exponent % 2 == 1:
            result = (result * base) % modulus

        base = (base * base) % modulus

        exponent = exponent // 2

    return result


def main():

    print("===== BINARY MODULAR EXPONENTIATION =====")

    try:
        base = int(input("Enter base (a): "))
        exponent = int(input("Enter exponent (b): "))
        modulus = int(input("Enter modulus (n): "))

        result = binary_modular_exponentiation(
            base, exponent, modulus
        )

        print("\n===== RESULT =====")
        print(f"({base}^{exponent}) mod {modulus} = {result}")

        print("\n===== VERIFICATION =====")
        print("Python built-in result:",
              pow(base, exponent, modulus))

        if result == pow(base, exponent, modulus):
            print("Verification Successful!")

    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()

