import tkinter
from .others.object import Object
from .others.exit_window import exit_window
from .saving import save

def registration():
    '''starting window with registration'''
    
    regist= tkinter.Toplevel()
    regist.title('Registration')

    #creating labels+entry as one object
    howManyOb=6
    o_log = Object(regist, 'Login',0,False)
    o_pass1 = Object(regist, 'Password',1,True)
    o_pass2 = Object(regist, 'Password2',2,True)
    o_mail = Object(regist, 'Email',3,False)
    o_phone = Object(regist, 'Phone',4,False)
    o_age = Object(regist, 'Age',5,False)
        
    #button to register
    b4 = tkinter.Button(regist,
                        text="Sign up",
                        fg="black",
                        bg="white",
                        command=lambda event=None: save(event,regist,o_log,o_pass1,o_pass2,o_mail,o_phone,o_age))

    #button to leave
    b5 = tkinter.Button(regist,
                        text="Cancel",
                        fg="black",
                        bg="red",
                        command=lambda event=None: exit_window(event,regist))

    #shortcuts for keyboard
    regist.bind("<Escape>",lambda event: exit_window(event,regist))
    regist.bind("<Return>",lambda event: save(event,regist,o_log,o_pass1,o_pass2,o_mail,o_phone,o_age))

    #organasation of screen
    b4.grid(row=howManyOb,column=0)
    b5.grid(row=howManyOb,column=1)

    #end of window
    regist.mainloop()
