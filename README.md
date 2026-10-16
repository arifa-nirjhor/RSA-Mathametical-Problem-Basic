# RSA Mathematical Foundations & Problem-Solving Algorithms

A structured collection of **RSA-related mathematical algorithms and problem-solving exercises** implemented using Python. This repository focuses on understanding the number-theoretic concepts that form the mathematical foundation of the RSA cryptosystem through practical programming examples.

The work in this repository is developed as part of my **cryptography learning and algorithm practice**, with an emphasis on understanding the relationship between mathematical theory, algorithm design, Python implementation, and cryptographic applications.

## Overview

The repository covers fundamental topics in number theory and modular mathematics, including:

- Prime Factorization using Trial Division
- Fermat's Factorization Method
- Greatest Common Divisor (GCD) using the Euclidean Algorithm
- Euler's Totient Function
- Modular Arithmetic, Modular Exponentiation, and Modular Multiplicative Inverse

Each exercise focuses on implementing a specific mathematical concept and observing its behavior through numerical examples. **The current repository contains foundational algorithms, not a complete RSA encryption/decryption implementation.**

## Course Topics

### 1. Prime Factorization

Implementation of **trial division** to decompose a positive integer into its prime factors.

- Tests possible divisors starting from 2.
- Repeatedly divides by each factor to capture multiplicity.
- Appends any remaining prime factor after trial division.

**Example:** `372 = 2 × 2 × 3 × 31` → `[2, 2, 3, 31]`

**Source:** [`prime_factorization.py`](prime_factorization.py)

### 2. Fermat's Factorization Method

Implementation of Fermat's method, based on the difference-of-squares identity:

$$n = x^2-y^2 = (x-y)(x+y)$$

- Starts at the ceiling of the square root of the input.
- Searches for a value of `x` such that `x² − n` is a perfect square.
- Returns a pair of integer factors; the factors are not necessarily prime.

**Example:** `5959 = 77² − 4² = 73 × 81`

**Source:** [`Fermat's_Factorization.py`](Fermat's_Factorization.py)

### 3. GCD — Euclidean Algorithm

Implementation of the **Euclidean Algorithm** to calculate the greatest common divisor of two integers.

$$\gcd(a,b)=\gcd(b,a\bmod b)$$

The program repeatedly updates the numbers until the remainder becomes zero, then returns the nonnegative GCD.

**Example:** `gcd(120, 7) = 1`

This concept is essential when selecting a valid RSA public exponent.

**Source:** [`GCD_Euclidean_Algorithm.py`](GCD_Euclidean_Algorithm.py)

### 4. Euler's Totient Function

Implementation of **Euler's totient function**, which counts the positive integers up to `n` that are coprime to `n`.

$$\varphi(n)=n\prod_{p\mid n}\left(1-\frac1p\right)$$

- Finds distinct prime factors using trial division.
- Updates the result once for each distinct prime factor.
- Handles any remaining prime factor after the loop.

**Example:** `φ(372) = 120`

For distinct primes `p` and `q`, textbook RSA uses `φ(pq) = (p − 1)(q − 1)` during key generation.

**Source:** [`Eulers'_Totient_Finction.py`](Eulers'_Totient_Finction.py)

### 5. Modular Arithmetic

Implementation of basic arithmetic operations under a positive modulus `n`:

- **Addition:** `(a + b) % n`
- **Subtraction:** `(a - b) % n`
- **Multiplication:** `(a * b) % n`
- **Exponentiation:** `pow(a, b, n)`
- **Multiplicative inverse of a:** `pow(a, -1, n)`, when it exists

**Example:** For `a = 11`, `b = 7`, and `n = 13`:

- Addition: `5`
- Subtraction: `4`
- Multiplication: `12`
- Exponentiation: `2`
- Inverse of `a`: `6`

These operations are central to RSA key generation, encryption, and decryption.

**Source:** [`Modular_Arithmetic.py`](Modular_Arithmetic.py)

## Technologies & Tools

| **Technology** | **Application** |
| --- | --- |
| **Python 3** | Core programming language |
| **Python standard library** | `math.isqrt()` and built-in modular arithmetic |
| **Visual Studio Code (optional)** | Code editing and execution |
| **Terminal / Command Prompt** | Running interactive Python scripts |

No third-party Python packages are required for the five current implementations.

## Learning Approach

The exercises follow an implementation-driven approach:

```text
Number Theory & Cryptography Fundamentals
                  ↓
          Mathematical Formula
                  ↓
       Step-by-Step Problem Solving
                  ↓
          Algorithm Design
                  ↓
         Python Implementation
                  ↓
       Numerical Verification
                  ↓
       Understanding RSA Concepts
```

This approach develops practical experience in translating mathematical ideas into working algorithms before progressing to a complete RSA cryptosystem.

## Learning Objectives

The exercises are designed to develop the ability to:

- Understand prime numbers, divisibility, and prime factorization.
- Implement trial division and Fermat's factorization.
- Calculate GCD using the Euclidean Algorithm.
- Understand coprimality and its importance in RSA key generation.
- Compute Euler's totient function using prime factors.
- Perform modular addition, subtraction, multiplication, and exponentiation.
- Determine whether a modular multiplicative inverse exists.
- Connect mathematical algorithms to RSA public and private key concepts.
- Strengthen Python programming, mathematical reasoning, and problem-solving skills.

## Practical Applications

The concepts explored in this repository provide foundational knowledge relevant to:

- RSA Cryptosystem Fundamentals
- Public-Key Cryptography
- Modular Arithmetic in Cryptographic Algorithms
- Number-Theoretic Problem Solving
- Cryptography Education and Algorithm Analysis
- Preparation for Secure RSA Implementation

## Repository Scope

```text
RSA Mathematical Foundations
│
├── Prime Factorization
│   ├── Trial Division
│   └── Fermat's Factorization Method
│
├── Number Theory
│   ├── GCD — Euclidean Algorithm
│   └── Euler's Totient Function
│
└── Modular Mathematics
    ├── Modular Addition
    ├── Modular Subtraction
    ├── Modular Multiplication
    ├── Modular Exponentiation
    └── Modular Multiplicative Inverse
```

### Repository Files

```text
.
├── prime_factorization.py
├── Fermat's_Factorization.py
├── GCD_Euclidean_Algorithm.py
├── Eulers'_Totient_Finction.py
├── Modular_Arithmetic.py
└── README.md
```

## Running the Programs

1. Install Python 3 and clone or download this repository.
2. Open a terminal in the repository directory.
3. Run a script and enter the requested integer inputs.

For example:

```bash
python prime_factorization.py
python GCD_Euclidean_Algorithm.py
python Modular_Arithmetic.py
```

For filenames containing an apostrophe, use double quotes in the terminal:

```bash
python "Fermat's_Factorization.py"
python "Eulers'_Totient_Finction.py"
```

> **Input notes:** Prime factorization expects an integer greater than 1; Fermat's factorization also requires an integer greater than 1; Euler's totient requires a positive integer. Modular arithmetic requires a positive modulus. A modular inverse exists only when `gcd(a, n) = 1`. The modular exponentiation line can raise `ValueError` for a negative exponent when the required inverse does not exist.

## Connection to RSA

These scripts prepare the mathematical foundations for the following **textbook RSA** procedure:

1. Choose distinct primes `p` and `q`.
2. Calculate `n = p × q`.
3. Calculate `φ(n) = (p − 1)(q − 1)`.
4. Choose `e` such that `gcd(e, φ(n)) = 1`.
5. Find `d = e⁻¹ mod φ(n)`.
6. Encrypt a message integer `M` using `C = Mᵉ mod n`.
7. Decrypt using `M = Cᵈ mod n`.

**Illustrative mathematical example (not yet a standalone implementation in this repository):**

Given `p = 11`, `q = 13`, `e = 7`, and `M = 9`:

- `n = 143`
- `φ(n) = 120`
- `d = 103`
- Public key: `(7, 143)`
- Private exponent and modulus: `(103, 143)`
- Encryption: `9⁷ mod 143 = 48`
- Decryption: `48¹⁰³ mod 143 = 9`

## Future Development

Potential future extensions include:

- Extended Euclidean Algorithm with a step-by-step table
- Square-and-Multiply (Efficient Modular Exponentiation)
- Complete Educational RSA Key Generation
- Textbook RSA Encryption and Decryption Demonstration
- Automated Unit Tests and Input Validation
- RSA-OAEP Implementation Using a Trusted Cryptographic Library

## Contributions

This repository primarily contains my **educational cryptography exercises and mathematical algorithm implementations**.

Suggestions, corrections, and improvements are welcome through GitHub Issues or Pull Requests, especially when they improve mathematical correctness, implementation quality, documentation, or educational clarity.

## Academic Purpose & Security Notice

This repository is maintained for **academic and educational purposes**. The algorithms are intended to demonstrate number-theoretic concepts and their connection to RSA.

**Do not use these exercises to protect sensitive information.** Small-number textbook RSA and handwritten cryptographic implementations are not secure for production use. Practical RSA encryption should use appropriately sized keys, RSA-OAEP padding, and an established cryptographic library.

## License

This repository is intended for **educational use**. No software license is specified here; add a `LICENSE` file if you want to grant explicit reuse and redistribution permissions.

## Author

**RSA Mathematical Foundations — Python Algorithm Implementations**

> **Understand the mathematics. Solve the problem. Implement the algorithm.**
