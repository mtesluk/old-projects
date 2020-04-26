import pymysql
import os
from tkinter import messagebox
from .mysql_exist import create_if_table_not_exist

def checking_in_database(login,passwd):
    '''checking if guest in registered'''

    TABLE_NAME = 'accounts'

    create_if_table_not_exist(TABLE_NAME)
    
    #connecting with mysql
    try:
        #this password and login are saved and you wont see it,
        #if you want give your own options
        cnx = pymysql.connect(host='localhost',
                              user=os.environ.get('USER_MYSQL'),
                              passwd=os.environ.get('PASS_MYSQL'),
                              db='logowanie')
    except:
        messagebox.showinfo("Log in","We have problem fetching data from database")
    else:
        cursor = cnx.cursor()
        
        #trying to take datas from mysql
        try:
            cursor.execute("SELECT password FROM "+TABLE_NAME+" WHERE login=%s",(login))
        except:
            messagebox.showinfo("Log in","We have problem with database")
        else:
            cnx.commit()
            
            #catch data from mysql
            data=cursor.fetchone()
            
            #saving data as variable
            try:
                for d in data:
                    data1=d
            except:
                return False

        cnx.close()
            
        #if data from mysql is correct with giving password
        if data1 == passwd:
            return True
        else:
            return False
