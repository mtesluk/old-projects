import tkinter
import os
from files.sign_in import sign_in
from files.others.object import Object
from files.registration import registration
from files.others.exit_window import exit_window


#starting program
root = tkinter.Tk()
root.title('Sign in')

#making objects for login
#number in argument is given for placing this objects
#False and True is for if Entry is password
howManyOb=2
ob_log = Object(root,'Login',0,security=False)
ob_pass = Object(root,'Password',1,security=True)
        
#button to accept login
b1 = tkinter.Button(root,
                    text="Sign in",
                    fg="black",
                    bg="white",
                    command=lambda event=None: sign_in(event,root,ob_log,ob_pass))

#button to leave window
b2 = tkinter.Button(root,
                    text="Exit",
                    fg="black",
                    bg="red",
                    command=lambda event=None: exit_window(event,root),
                    relief="raised")

#button to registrartion
b3 = tkinter.Button(root,
                    text="Sign up",
                    fg="black",
                    bg="white",
                    command=registration)

#label with information about lack of account
l1 = tkinter.Label(root,
                   text="Dont't you have account?----->")


#shortcuts for keyboard
root.bind("<Return>",lambda event: sign_in(event,root,ob_log,ob_pass))
root.bind("<Escape>",lambda event: exit_window(event,root))

#organasation of screen
b1.grid(row=howManyOb,column=0)
b2.grid(row=howManyOb,column=1)
b3.grid(row=howManyOb+1,column=1,sticky='w')
l1.grid(row=howManyOb+1,column=0)

#end of window
root.mainloop()
