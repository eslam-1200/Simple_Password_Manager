import hashlib
import user_choice
import sqlite3
import base64
import time

cont = sqlite3.connect("Manager.db")
cur = cont.cursor()


main_check = cur.execute("SELECT Password FROM Password_Manager WHERE Service = 'main'").fetchone()
compare = main_check[0]
def hashing(to_hash):
    in_bytes = bytes(to_hash,'utf-8')
    encoded = base64.b64encode(in_bytes,altchars=None)
    hashed = hashlib.sha256(encoded).hexdigest()
    return hashed


def check():

    while True:
        counter = 5

        while counter > 0:
            password = input("Enter the password : ")
            password=hashing(password)

            if password == compare:
                print("Access granted :D")
                return

            else:
                print("Try Again")
                counter -= 1

        for seconds in range(30 ,0, -1):
            print(f"Attemps finished, try again after: {seconds:02d}",end="\r",flush=True)
            time.sleep(1)
        print("\ntry again now.")



def main_fun():
    check()
    user_choice.Choose()


main_fun()