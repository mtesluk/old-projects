from .others.mail import mail
from .mysql.insert_mysql import saving_in_database
from .others.exit_window import exit_window
from tkinter import messagebox

def save(event,regist,o_log,o_pass1,o_pass2,o_mail,o_phone,o_age):
        '''saving data in database'''
        
        #geting text from Entry email
        receiver = o_mail.getStr()

        #saving login,password,etc in databse
        #if pass1 and pass2 are the same
        if o_pass1.getStr() == o_pass2.getStr():
                try:
                        saving_in_database(o_log.getStr(),o_pass1.getStr(),o_mail.getStr(),o_phone.getStr(),o_age.getStr())
                except:
                        messagebox.showinfo("Register","We have problem with database")

                #send email confirming that you have registered
                try:
                        mail(receiver,"Registration","Everything is ok!!!")
                except:
                        messagebox.showinfo("Email","You are registered, but we can't send you an email")

                exit_window(event,regist)
        else:
                messagebox.showinfo("Register","You don't have the same passwords")

                #clear Entry of passwords
                o_pass1.cl()
                o_pass2.cl()
                        
                
