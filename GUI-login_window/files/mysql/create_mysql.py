import pymysql
import os
from tkinter import messagebox

def create_table(TABLE_NAME):
    '''creating table "accounts"'''

    #connecting with mysql
    try:
        #this password and login are saved and you wont see it,
        #if you want give your own options
        cnx = pymysql.connect(host='localhost',
                              user=os.environ.get('USER_MYSQL'),
                              passwd=os.environ.get('PASS_MYSQL'),
                              db='logowanie')
    except:
        messagebox.showinfo("Log in","We have problem with database")
    else:
        cursor = cnx.cursor()
        
        #trying to craete table
        try:
            cursor.execute("CREATE TABLE "+TABLE_NAME+" (`login` VARCHAR(30), `password` VARCHAR(30), `email` VARCHAR(30), `number` VARCHAR(15), `age` VARCHAR(3))")
        except:
            messagebox.showinfo("Log in","We have problem with creating table")
        else:
            cnx.commit()

        cnx.close()

