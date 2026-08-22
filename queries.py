import sqlite3
import hashlib
import base64
from cryptography.fernet import Fernet

content = sqlite3.connect("Manager.db")
cur = content.cursor()
key = b'9IvKyvJVTtT_Yc4yAbuRZ8kSXvXvZfwzqGvfhUKxzZg='
f = Fernet(key)


def enc(to_encrypt):
    to_encrypt = bytes(to_encrypt,'utf-8')
    encrypted = f.encrypt(to_encrypt)
    return encrypted


def dec(to_decrypt):
    text = f.decrypt(to_decrypt)
    return text


def select(service):
    result = cur.execute("SELECT * FROM Password_Manager WHERE Service = ?",(service,)).fetchall()
    if not result:
        print("Not found")

    elif result[0][0] == "Main" :
        print("Secret!!")

    else:
        to_print_before=["Email/Username","Password"]
        for i in range(1,3):
            print(to_print_before[i-1], ": ",dec(result[0][i]).decode())


def add(data):
    if cur.execute("SELECT * FROM Password_Manager WHERE Service = ?",(data[0],)).fetchall():
        print("Already there!")
        return
    enc_data =  [ (data[0],enc(data[1]),enc(data[2])) ]
    cur.executemany("INSERT INTO Password_Manager VALUES (?,?,?)",enc_data)
    content.commit()


def edit(con,data):
    if con == "Main":
        new_pass_b = base64.b64encode(data[2].encode("utf-8"))
        hashed_password = hashlib.sha256(new_pass_b).hexdigest()
        cur.execute(
            "UPDATE Password_Manager SET Email = ?, Password = ? WHERE Service = ?",
            ("NULL", hashed_password, "Main"),
        )
        content.commit()
    else:
        enc_data =  [ (data[0],enc(data[1]),enc(data[2]),con) ]
        cur.executemany("UPDATE Password_Manager SET Service = ? , Email = ? , Password = ? WHERE Service = ?",enc_data)
        content.commit()


def delete(service):
    result = cur.execute("SELECT * FROM Password_Manager WHERE Service = ?",(service,)).fetchall()
    if not result:
        print("Already Not There!")
    else:
        cur.execute("DELETE FROM Password_Manager WHERE Service = ?",(service,))
        print("Deleted!")
        content.commit()

