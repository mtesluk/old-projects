import pymysql
import os
from .create_mysql import create_table
from tkinter import messagebox

def create_if_table_not_exist(TABLE_NAME):
    '''checkinng if table "accounts" exist'''

    #connecting with mysql
    try:
        #this password and login are saved and you wont see it,
        #if you want give your own options
        cnx = pymysql.connect(host='localhost',
                              user=os.environ.get('USER_MYSQL'),
                              passwd=os.environ.get('PASS_MYSQL'),
                              db='logowanie')
    except:
        messagebox.showinfo("Register","We have problem with connecting to database")
    else:
        cursor = cnx.cursor()

        #trying to take datas from mysql
        try:
            cursor.execute("SHOW tables LIKE %s",(TABLE_NAME))
        except:
            messagebox.showinfo("Register","We have problem with checking if table exist")
        else:
            cnx.commit()
            
            #catch data from mysql
            data=cursor.fetchone()
            
            #checking if table exist
            if data:
                pass
            else:
                create_table(TABLE_NAME)
            
        cnx.close()

