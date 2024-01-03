# Elliptic-curve-crypto-client-server-example

## Introduction

This documentation provides an example of a simple client-server communication using Elliptic Curve Cryptography (ECC) in Python. The code demonstrates the generation of key pairs, encryption, and decryption using the `cryptography` library.

## Requirements

- Python 3.x
- `cryptography` library
- `Scapy` library

Install the required library using:

```bash
pip install cryptography
pip install scapy
```

## Code Overview

### Server Code (`server.py`)

- `generate_key_pair()`: Generates a private-public key pair.
- `encrypt_message(public_key, plaintext)`: Encrypts a message using ECC.
- `decrypt_message(private_key, public_key, ciphertext, iv)`: Decrypts a message using ECC.

### Client Code (`client.py`)

- `generate_key_pair()`: Generates a private-public key pair.
- `encrypt_message(public_key, plaintext)`: Encrypts a message using ECC.
- `decrypt_message(private_key, public_key, ciphertext, iv)`: Decrypts a message using ECC.

### Man in the middle code (`manInTheMiddle`)

- `packet sniffer ` captures TCP packets on port 5000 and prints information about encrypted packets

## Usage

1. Run the server code:
   ```bash
   python3 server.py
   ```

2. Run the client code:
   ```bash
   python3 client.py
   ```
3. Run the manInTheMiddle code:
   ```bash
   python3 manInTheMiddle.py
   ```

## Explanation

1. The server generates a private-public key pair.
2. The server sends its public key to the client.
3. The client generates its private-public key pair.
4. The client sends its public key to the server.
5. The client and server exchange encrypted messages.
6. The script will start sniffing on the loopback interface (`lo`) and capture TCP packets on port 5000.
7. When an encrypted packet is detected, it will be printed with detailed information.

## Important Notes

- This example is for educational purposes and demonstrates basic ECC communication.
- In a real-world scenario, additional security measures should be implemented.
- Error handling and key management are crucial for a secure system.
- according to packet sniffing: Packet sniffing without proper authorization is illegal and unethical. Ensure that you have permission to monitor the network traffic.
- This script is for educational purposes only. Do not use it for malicious activities or without proper consent.
- Be aware of the legal implications and privacy considerations when capturing network packets.


## References

- [cryptography library documentation](https://cryptography.io/en/latest/)
- [Scapy Documentation](https://scapy.readthedocs.io/en/latest/)


Certainly! Below is the documentation for the provided Python code:

---

### Elliptic Curve Arithmetic

This Python script demonstrates basic elliptic curve arithmetic, specifically the double-and-add operation for scalar multiplication on an elliptic curve defined over a finite field.

#### Parameters:
- `a`: Coefficient in the elliptic curve equation \(y^2 \equiv x^3 + ax + b \pmod{p}\).
- `p`: Prime modulus specifying the finite field \(\mathbb{F}_p\) over which the elliptic curve is defined.
- `G`: Generator point on the elliptic curve, represented as a tuple `(x, y)`.
  
#### Functions:

1. **point_double(P, a, p)**
   - Computes the doubling of a point `P` on the elliptic curve.
   - Parameters:
     - `P`: Point on the elliptic curve (tuple representing coordinates).
     - `a`: Coefficient in the elliptic curve equation.
     - `p`: Prime modulus.
   - Returns: Doubled point.

2. **point_add(P, Q, a, p)**
   - Computes the addition of two points `P` and `Q` on the elliptic curve.
   - Parameters:
     - `P`: First point on the elliptic curve.
     - `Q`: Second point on the elliptic curve.
     - `a`: Coefficient in the elliptic curve equation.
     - `p`: Prime modulus.
   - Returns: Resultant point after addition.

3. **doubleAndAdd(t, P, a, p)**
   - Performs the double-and-add operation for scalar multiplication on the elliptic curve.
   - Parameters:
     - `t`: Scalar multiplier.
     - `P`: Generator point on the elliptic curve.
     - `a`: Coefficient in the elliptic curve equation.
     - `p`: Prime modulus.
   - Returns: Resultant point after scalar multiplication.

#### Example Usage:

```python
# Example Elliptic Curve Parameters
a = 2
p = 17
G = (5, 11)  # Generator point

# Scalar Multiplication Example
t = 26
result = doubleAndAdd(t, G, a, p)
print("Result:", result)
```

In this example, the elliptic curve equation is \(y^2 \equiv x^3 + 2x + 2 \pmod{17}\), and the generator point is \(G = (5, 11)\). The script performs scalar multiplication of the generator point by a scalar \(t = 26\), yielding the result on the elliptic curve.

---
