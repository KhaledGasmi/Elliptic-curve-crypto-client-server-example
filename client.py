import socket
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

def generate_key_pair():
    private_key = ec.generate_private_key(ec.SECP256R1(), default_backend())
    public_key = private_key.public_key()
    return private_key, public_key

def encrypt_message(public_key, plaintext):
    shared_key = private_key.exchange(ec.ECDH(), public_key)
    derived_key = hashes.Hash(hashes.SHA256(), backend=default_backend())
    derived_key.update(shared_key)
    encryption_key = derived_key.finalize()[:16]
    iv = b'0123456789012345'  # Initialization Vector
    cipher = Cipher(algorithms.AES(encryption_key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext.encode('utf-8')) + encryptor.finalize()
    return ciphertext, iv

def decrypt_message(private_key, public_key, ciphertext, iv):
    shared_key = private_key.exchange(ec.ECDH(), public_key)
    derived_key = hashes.Hash(hashes.SHA256(), backend=default_backend())
    derived_key.update(shared_key)
    encryption_key = derived_key.finalize()[:16]
    cipher = Cipher(algorithms.AES(encryption_key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_text = decryptor.update(ciphertext) + decryptor.finalize()
    return decrypted_text.decode('utf-8')

# Client
private_key, public_key = generate_key_pair()
print("the privat key is {} \n the public key is {}".format(private_key, public_key) )

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 5000))

# Receive server's public key
server_public_key_bytes = client.recv(1024)
server_public_key = serialization.load_pem_public_key(server_public_key_bytes, backend=default_backend())
print("the server's public key {}".format(server_public_key))


# Send public key to the server
client.send(public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
))

while True:
    # Encrypt and send a message to the server
    message = input('Enter a message for the server (type "end" to finish): ')
    ciphertext, iv = encrypt_message(server_public_key, message)
    print("message to send :", message)
    client.send(ciphertext)
    client.send(iv)

    if message.lower() == 'end':
        print('Communication ended by client.')
        break

    # Receive and decrypt a message from the server
    received_ciphertext = client.recv(1024)
    received_iv = client.recv(1024)
    decrypted_message = decrypt_message(private_key, server_public_key, received_ciphertext, received_iv)
    print("befor decreption :", received_ciphertext)
    print('Received message from server:', decrypted_message)


client.close()
