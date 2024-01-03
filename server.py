import socket
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization, hashes
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

# Server
private_key, public_key = generate_key_pair()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 5000))
server.listen(1)

print('Server waiting for connection...')
connection, client_address = server.accept()
print('Connected to:', client_address)

# Send public key to the client
connection.send(public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
))

# Receive client's public key
client_public_key_bytes = connection.recv(1024)
client_public_key = serialization.load_pem_public_key(client_public_key_bytes, backend=default_backend())
print("the client's public key is {}".format(client_public_key))

while True:
    # Receive and decrypt a message from the client
    received_ciphertext = connection.recv(1024)
    received_iv = connection.recv(1024)
    decrypted_message = decrypt_message(private_key, client_public_key, received_ciphertext, received_iv)
    print("before decryption :", received_ciphertext)
    print('Received message from client:', decrypted_message)

    if decrypted_message.lower() == 'end':
        print('Communication ended by client.')
        break

    # Encrypt and send a message
    message = decrypted_message
    ciphertext, iv = encrypt_message(client_public_key, message)
    connection.send(ciphertext)
    connection.send(iv)

connection.close()
server.close()