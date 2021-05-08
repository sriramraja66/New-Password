from encdec import *
from getpass import getpass
from data.user import user
from database import database
from settings import settings
from froget import user_pass,change

# instance for settings
sett = settings()
db = database()
key = load_key()
dec = decrypt(user_pass(),key)

def UI():
    print('1 : Add Data')
    print('2 : Update Record')
    print('3 : Delete Record')
    print('4 : Change Password')
    print('5 : Exit')
    return sett.integer_in('Enter Here : ')

incorrect = 4

while 1:
    sett.cls()
    passwd = getpass('Enter your Password : ')
    while 1:   
        sett.cls() 
        if passwd == dec:
            incorrect = 4
            print('Records Are :-\n')
            db.viewall()
            ch = UI()
            if ch == 1:
                desc = input("Enter The Decription (Press 99 to Go Back): ")
                if desc == '99':
                    continue
                p = getpass("Enter The Password : ")
                enc = encrypt(msg=p,key=key)
                db.insert(desc,enc.decode())
                print('Added..')

            elif ch == 2:
                i = input("Enter The ID (Press 99 to Go Back) : ")
                if i == '99':
                    continue
                p = getpass("Enter The New Password : ")
                enc = encrypt(p,key)
                db.update(i,enc.decode())
                print("Updated...")

            elif ch == 3:
                i = input("Enter The ID (Press 99 to Go Back) : ")
                if i == '99':
                    continue
                db.delete(i)
                print('Deleted')
            
            elif ch == 4:
                if passwd == dec:
                    try:
                        change()
                        print("sucess")
                    except:
                        print("Error")
                
                    sett.sec(2)
                
            else:
                print("Exit")
                quit()

        elif incorrect == 1:
                print('Un Aurhorized Use....')
                print('Database is going to deleted...')
                sett.sec(2)
                db.remove_db()
                quit()
        else:
            print('Password Incorrect.. ')
            print('You Have : ',incorrect-1," Chance") 
            incorrect-=1
            sett.sec(1)
            break
    sett.sec(1)
    