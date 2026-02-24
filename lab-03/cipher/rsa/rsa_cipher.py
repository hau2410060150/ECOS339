# cipher/rsa/rsa_cipher.py
import os
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes


class RSACipher:
    def __init__(self, keys_dir=None):
        # keys_dir = lab-03/cipher/rsa/keys
        base_dir = os.path.dirname(__file__)
        self.keys_dir = keys_dir or os.path.join(base_dir, "keys")
        os.makedirs(self.keys_dir, exist_ok=True)

        self.private_key_path = os.path.join(self.keys_dir, "private_key.pem")
        self.public_key_path = os.path.join(self.keys_dir, "public_key.pem")

    def generate_keys(self, key_size=2048):
        private_key = rsa.generate_private_key(public_exponent=65537, key_size=key_size)
        public_key = private_key.public_key()

        # save private
        priv_bytes = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption(),
        )
        with open(self.private_key_path, "wb") as f:
            f.write(priv_bytes)

        # save public
        pub_bytes = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo,
        )
        with open(self.public_key_path, "wb") as f:
            f.write(pub_bytes)

    def load_keys(self):
        with open(self.private_key_path, "rb") as f:
            private_key = serialization.load_pem_private_key(f.read(), password=None)

        with open(self.public_key_path, "rb") as f:
            public_key = serialization.load_pem_public_key(f.read())

        return private_key, public_key

    def encrypt(self, message: str, key):
        ciphertext = key.encrypt(
            message.encode("utf-8"),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None,
            ),
        )
        return ciphertext  # bytes

    def decrypt(self, ciphertext: bytes, key):
        plaintext = key.decrypt(
            ciphertext,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None,
            ),
        )
        return plaintext.decode("utf-8")

    def sign(self, message: str, private_key):
        signature = private_key.sign(
            message.encode("utf-8"),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH,
            ),
            hashes.SHA256(),
        )
        return signature  # bytes

    def verify(self, message: str, signature: bytes, public_key):
        try:
            public_key.verify(
                signature,
                message.encode("utf-8"),
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH,
                ),
                hashes.SHA256(),
            )
            return True
        except Exception:
            return False