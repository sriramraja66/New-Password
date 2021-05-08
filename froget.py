from getpass import getpass
from encdec import *
key = load_key()

def user_pass():
    try:
        with open("data/user.bin","rb") as f:
            return f.read()
    except:
        print("User Not Found")

def change():
    passwd = getpass("Enter The New Password : ")
    cpasswd = getpass("Conform The Password : ")

    if passwd == cpasswd:
        p = encrypt(passwd,key)
        with open("data/user.bin","wb") as f:
            f.write(p)
        
if __name__ == "__main__":
    print(user_pass())