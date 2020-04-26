import pymysql
import os
from tkinter import messagebox
from .mysql_exist import create_if_table_not_exist

def saving_in_database(txt_log,txt_pass1,txt_mail,txt_phone,txt_age):
    '''saving users's datas while registration'''

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
        messagebox.showinfo("Register","We have problem saving data to database")
    else:
        cursor = cnx.cursor()

        #trying to insert datas to mysql
        try:
            cursor.execute("INSERT INTO accounts (login,password,email,number,age) VAlUES (%s,%s,%s,%s,%s)",(txt_log,txt_pass1,txt_mail,txt_phone,txt_age))
        except:
            messagebox.showinfo("Register","We have problem with database")
        else:
            cnx.commit()
        
        cnx.close()
