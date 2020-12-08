import sqlite3
conn = sqlite3.connect('login.db') #create and activate db

cursor = conn.cursor()

cursor.execute(''' CREATE TABLE IF NOT EXISTS login(
                    USUARIO TEXT PRIMARY KEY NOT NULL,
                    SENHA INT NOT NULL)''')

#cursor.execute("INSERT INTO login VALUES('pamela', 12345)")
conn.commit() #apply changes

cursor.execute("SELECT * FROM login")
print(cursor.fetchall())

def write(USUARIO, SENHA): #write values in db
    cursor.execute('''INSERT INTO login(USUARIO, SENHA) VALUES(?, ?)''', (USUARIO, SENHA))
    conn.commit()

def read(USUARIO, SENHA):
    cursor=conn.cursor()
    cursor.execute('''SELECT USUARIO, SENHA from login''')
    data = cursor.fetchall()
    conn.commit()
    return data
    