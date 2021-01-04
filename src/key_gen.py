import os

from Crypto.PublicKey import RSA

from src.utils import save_file


def generate_public_key(path):
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    save_file(os.path.join(path, "private.pem"), private_key)
    save_file(os.path.join(path, "public.pem"), public_key)
