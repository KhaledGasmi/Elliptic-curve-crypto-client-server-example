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
   python3 manInTheMiddle
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
