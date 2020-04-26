import tkinter
from files.exit_window import exit_window
from files.delete import *
from files.showing_on_screen import *

def program():
    '''main program'''

    
    #initiate new window
    prog= tkinter.Tk()
    prog.title('Program')

    #making new variable
    txt=tkinter.StringVar()
    con=[]
    num=[]
    char=[]
    
    #all initiations of widgets
    c1 = tkinter.Button(prog,text="C",command=lambda: del_all(txt,con,num,char))
    n1 = tkinter.Button(prog,text="1",command=lambda: show_1(txt,con))
    n2 = tkinter.Button(prog,text="2",command=lambda: show_2(txt,con))
    n3 = tkinter.Button(prog,text="3",command=lambda: show_3(txt,con))
    b1 = tkinter.Button(prog,text="+",command=lambda: show_plus(txt,con,num,char))
    n4 = tkinter.Button(prog,text="4",command=lambda: show_4(txt,con))
    n5 = tkinter.Button(prog,text="5",command=lambda: show_5(txt,con))
    n6 = tkinter.Button(prog,text="6",command=lambda: show_6(txt,con))
    b2 = tkinter.Button(prog,text="-",command=lambda: show_minus(txt,con,num,char))
    n7 = tkinter.Button(prog,text="7",command=lambda: show_7(txt,con))
    n8 = tkinter.Button(prog,text="8",command=lambda: show_8(txt,con))
    n9 = tkinter.Button(prog,text="9",command=lambda: show_9(txt,con))
    b3 = tkinter.Button(prog,text="\\",command=lambda: show_devide(txt,con,num,char))
    b4 = tkinter.Button(prog,text=".",command=lambda: show_dot(txt,con))
    n0 = tkinter.Button(prog,text="0",command=lambda: show_0(txt,con))
    b5 = tkinter.Button(prog,text="=",command=lambda: show_eq(txt,con,num,char))
    b6 = tkinter.Button(prog,text="*",command=lambda: show_multiply(txt,con,num,char))
    t = tkinter.Label(prog ,textvariable=txt)

    #arrangment of screen
    t.grid(row=1,column=1,columnspan=3)
    c1.grid(row=1,column=0)
    n1.grid(row=2,column=0)
    n2.grid(row=2,column=1)
    n3.grid(row=2,column=2)
    b1.grid(row=2,column=3)
    n4.grid(row=3,column=0)
    n5.grid(row=3,column=1)
    n6.grid(row=3,column=2)
    b2.grid(row=3,column=3)
    n7.grid(row=4,column=0)
    n8.grid(row=4,column=1)
    n9.grid(row=4,column=2)
    b3.grid(row=4,column=3)
    n0.grid(row=5,column=1)
    b4.grid(row=5,column=0)
    b5.grid(row=5,column=3)
    b6.grid(row=5,column=2)

    prog.bind("<Escape>",lambda event: exit_window(event,prog))
    
    prog.mainloop()


#start program
program()
