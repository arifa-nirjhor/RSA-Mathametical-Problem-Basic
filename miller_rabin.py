
import secrets


def miller_rabin(n, rounds=40):

    if rounds < 1:
        raise ValueError("Rounds must be at least 1.")

    # Step 1: Handle small numbers
    if n < 2:
        return False

    if n in (2, 3):
        return True

    if n % 2 == 0:
        return False

    # Step 2: Check small prime divisibility
    small_primes = [3, 5, 7, 11, 13, 17, 19, 23, 29]

    for prime in small_primes:
        if n == prime:
            return True

        if n % prime == 0:
            return False

    # Step 3: Express n - 1 as 2^s * d
    d = n - 1
    s = 0

    while d % 2 == 0:
        d //= 2
        s += 1

    # Step 4: Perform Miller-Rabin rounds
    for _ in range(rounds):

        # Choose random base in [2, n - 2]
        a = secrets.randbelow(n - 3) + 2

        # Calculate a^d mod n
        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        # Step 5: Repeated squaring
        for _ in range(s - 1):
            x = pow(x, 2, n)

            if x == n - 1:
                break

        else:
            # Composite number detected
            return False

    # Passed all rounds
    return True


def main():

    print("===== MILLER-RABIN PRIMALITY TEST =====")

    try:
        number = int(input("Enter an integer: "))
        rounds = int(input("Enter number of rounds (e.g. 40): "))

        result = miller_rabin(number, rounds)

        print("\n===== RESULT =====")

        if result:
            print(f"{number} is PROBABLY PRIME.")
        else:
            print(f"{number} is COMPOSITE (or less than 2).")

        print("Testing rounds:", rounds)

    except ValueError as error:
        print("\nError:", error)


if __name__ == "__main__":
    main()

