from cryptography.fernet import Fernet
import base64


def writekey():
    key = Fernet.generate_key()
    with open('data/key.key','wb') as f:
        f.write(key)
        print('done')

def load_key():
    return open('data/key.key','rb').read()

def encrypt(msg,key):
    f = Fernet(key)
    return f.encrypt(bytes(str(msg).encode()))

def decrypt(enc,key):
    f = Fernet(key)
    return f.decrypt(enc).decode()

