from .operations_on_numbers import *


def show_0(txt,con):
    '''give number 0 to screen and add to list'''
        
    con.append("0")
    txt.set(joining_numbers(con))

        
def show_1(txt,con):
    '''give number 1 to screen and add to list'''
        
    con.append("1")
    txt.set(joining_numbers(con))

#next its analogy
    
def show_2(txt,con):
    con.append("2")
    txt.set(joining_numbers(con))


def show_3(txt,con):
    con.append("3")
    txt.set(joining_numbers(con))
        

def show_4(txt,con):
    con.append("4")
    txt.set(joining_numbers(con))

    
def show_5(txt,con):
    con.append("5")
    txt.set(joining_numbers(con))

    
def show_6(txt,con):
    con.append("6")
    txt.set(joining_numbers(con))
        
    
def show_7(txt,con):
    con.append("7")
    txt.set(joining_numbers(con))

    
def show_8(txt,con):
    con.append("8")
    txt.set(joining_numbers(con))

    
def show_9(txt,con):
    con.append("9")
    txt.set(joining_numbers(con))

def show_dot(txt,con):
    con.append(".")
    txt.set(joining_numbers(con))
    
def show_plus(txt,con,num,char):
    saving_number(con,num,char)
    saving_char(con,num,char,'+')
    del con[:]
    txt.set(con)

    
def show_minus(txt,con,num,char):
    saving_number(con,num,char)
    saving_char(con,num,char,'-')
    del con[:]
    txt.set(con)

    
def show_multiply(txt,con,num,char):
    saving_number(con,num,char)
    saving_char(con,num,char,'*')
    del con[:]
    txt.set(con)

    
def show_devide(txt,con,num,char):
    saving_number(con,num,char)
    saving_char(con,num,char,'/')
    del con[:]
    txt.set(con)

    
def show_eq(txt,con,num,char):
    '''give the equation of calculations'''
    
    saving_number(con,num,char)
    del con[:]
    txt.set(str(solving(num,char)))
