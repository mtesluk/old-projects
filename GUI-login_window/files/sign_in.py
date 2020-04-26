from tkinter import messagebox
from .others.program import program
from .others.exit_window import exit_window
from .mysql.fetch_mysql import checking_in_database


def sign_in(event,root,ob_log,ob_pass):
    '''command for log in'''

    #getting text from Entry field
    log = ob_log.getStr() 
    password = ob_pass.getStr()  

    #if login and password are correct
    if checking_in_database(log,password) == True:
        #exit login window
        exit_window(event,root)
        
        #run calculator
        program()
    else:
        #clear Entry field
        ob_pass.cl()

        #show warning
        messagebox.showinfo("Log in","You can't log in, try again")
