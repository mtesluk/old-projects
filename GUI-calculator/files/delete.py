def del_all(txt,con,num,char):
    '''delete all numbers from memory'''
        
    del con[:]
    del num[:]
    del char[:]
    txt.set("")
