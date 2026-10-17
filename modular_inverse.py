
from extended_euclidean import extended_gcd


def modular_inverse(a, m):
    if m <= 1:
        raise ValueError("Modulus must be greater than 1.")

    gcd_value, x, y = extended_gcd(a, m)

    if gcd_value != 1:
        raise ValueError(
            "Modular inverse does not exist because "
            "GCD(a, m) is not 1."
        )

    inverse = x % m

    return inverse


def main():
    print("===== MODULAR MULTIPLICATIVE INVERSE =====")

    try:
        a = int(input("Enter integer (a): "))
        m = int(input("Enter modulus (m): "))

        inverse = modular_inverse(a, m)

        print("\n===== RESULTS =====")
        print("Integer (a):", a)
        print("Modulus (m):", m)
        print("Modular Inverse:", inverse)

        print("\n===== VERIFICATION =====")
        print(f"({a} * {inverse}) % {m} = {(a * inverse) % m}")

    except ValueError as error:
        print("\nError:", error)


if __name__ == "__main__":
    main()
