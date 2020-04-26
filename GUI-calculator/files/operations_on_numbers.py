def solving(num,char):
        '''solve calculations'''
        
        if len(char) > 0 and len(num) > 1:
            for i in range(len(char)):
                if char[0] == '+':
                    num[0]=num[0]+num[1]
                    num[0] = float("%0.5f" % num[0])
                    del num[1]
                    del char[0]
                elif char[0] == '-':
                    num[0]=num[0]-num[1]
                    num[0] = float("%0.5f" % num[0])
                    del num[1]
                    del char[0]
                elif char[0] == '*':
                    num[0]=num[0]*num[1]
                    num[0] = float("%0.5f" % num[0])
                    del num[1]
                    del char[0]
                elif char[0] == '/':
                    if num[1] != 0:
                        num[0]=num[0]/num[1]
                        num[0] = float("%0.5f" % num[0])
                        del num[1]
                        del char[0]
                    else:
                        del num[1]
                        del char[0]
                        return "You cant devide by 0\nContinue!!!" 
        return num[0]


def joining_numbers(con):
        '''putting all digit from list into one number'''

        if con[0] == "0" and len(con) > 0:
                del con[0]
        
        return "".join(con)

    
def saving_number(con,num,char):
    '''saving numbers to one list'''
    
    #if size of digits in list is bigger than 0
    #then it can save digits to one number
    if len(con)>0:
        num.append(float("".join(con)))
        
    if len(num) > len(char)+1:
        del num[0]

    
def saving_char(con,num,char,c):
    '''saving char for calculation to one list'''
    
    if len(char) >= len(num) and len(char) > 0:
        del char[-1]

    if len(char) + 1 == len(num):
            char.append(c)
