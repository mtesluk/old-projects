import tkinter



class Object():
    '''object for connecting label with Entry'''
    
    def __init__(self,master,tekst,row,security):
        '''constructor'''
        
        self.master=master
        self.tekst=tekst
        self.row=row
        self.l= tkinter.Label(self.master,text=self.tekst)
        self.security = security
        
        #if security, show Str in Entry as ***** 
        if self.security:
            self.entry = tkinter.Entry(self.master,show="*")
        else:
            self.entry = tkinter.Entry(self.master)
            
        self.l.grid(row=self.row,column=0,sticky="e")
        self.entry.grid(row=self.row,column=1)

    
    def getStr(self):
        '''getting text from Entry'''
        
        return self.entry.get()

    
    def cl(self):
        '''cleaning Entry'''
        
        self.entry.delete(0,"end")
        
