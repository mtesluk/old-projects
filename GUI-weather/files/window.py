from PyQt4 import QtGui,QtCore
from API.api import Json
import sys
import datetime

class Window(QtGui.QMainWindow):
    '''main window'''

    def __init__(self):
        '''initial settings for main window'''

        #inheritance from PyQt attributes
        super(Window,self).__init__()
        
        #set basic options
        self.setGeometry(300,100,800,600)
        self.setWindowTitle("Weather")
        self.setWindowIcon(QtGui.QIcon("pythonlogo.png"))
        self.set_background_color()
        
        #city to check weather
        self.city = ""
        
        #show elements on the screen
        self.show_entry_field()
        self.show_date_label()
        self.show_drop_list()
        self.show_city_label()
        self.create_temp_label()
        
        #finnaly showing of everything
        self.show()

    def set_background_color(self):
        '''set background color'''
        
        p = self.palette()
        p.setColor(self.backgroundRole(), QtGui.QColor(128,159,255))
        self.setPalette(p)

    def show_city_label(self):
        '''label with name of city'''

        #create label
        self.city_label = QtGui.QLabel(self)

        #set text of label
        self.city_label.setText(self.city)

        #set font of label
        self.font_city = QtGui.QFont("Arial",35)
        self.city_label.setFont(self.font_city)

        #set spot on screen
        self.city_label.setGeometry(300,10,350,50)
    

    def change_city_label(self):
        '''just change label on city name'''
        
        self.city_label.setText(self.city)
    
        
    def show_date_label(self):
        '''show label with today date'''

        #download today day
        self.today = str(datetime.date.today())

        #create label
        self.date_label = QtGui.QLabel(self)

        #set text of labele
        self.date_label.setText(self.today)

        #set font of label
        self.font_date = QtGui.QFont("Times",20)
        self.date_label.setFont(self.font_date)

        #set spot on screen
        self.date_label.setGeometry(550,50,130,90)


    def show_drop_list(self):
        '''create and operate on drop down list'''

        #create drop down list
        self.comboBox = QtGui.QComboBox(self)

        #add items of today and tomorrow
        self.comboBox.addItem("DAY")
        self.comboBox.addItem("today")
        self.comboBox.addItem("tomorrow")

        #create variable of date tomorrow
        self.tomorrow = self.today
        self.tomorrow = self.tomorrow[:8] + str(int(self.tomorrow[8:]) + 1)

        #add item to lista
        self.in_two_days = self.today
        text = self.in_two_days[:8] + str(int(self.in_two_days[8:]) + 2)
        self.comboBox.addItem(text)

        #add next item do frop down
        self.in_three_days = self.today
        text = self.in_three_days[:8] + str(int(self.in_three_days[8:]) + 3)
        self.comboBox.addItem(text)

        #and the same
        self.in_four_days = self.today
        text = self.in_four_days[:8] + str(int(self.in_four_days[8:]) + 4)
        self.comboBox.addItem(text)

        #and the same
        self.in_five_days = self.today
        text = self.in_five_days[:8] + str(int(self.in_five_days[8:]) + 5)
        self.comboBox.addItem(text)
        
        self.comboBox.setGeometry(330,80,130,28)

        #when you choose item then it actuall every temerature
        self.comboBox.activated[str].connect(self.show_temp)
        
        
    def show_entry_field(self):
        '''connect label, entry field and button in one element'''

        #create entry field to write searching city
        self.entry_field = QtGui.QLineEdit(self)

        #create entry label 
        self.entry_label = QtGui.QLabel(self)
        self.entry_label.setText("City:")

        #create entry button to start searching
        self.entry_btn = QtGui.QPushButton("Search",self)
        self.entry_btn.clicked.connect(self.search)

        #connect the elements into one element
        #and set the posiotion on the screen
        self.flo = QtGui.QHBoxLayout()
        self.flo.addWidget(self.entry_label)
        self.flo.addStretch()
        self.flo.addWidget(self.entry_field)
        self.flo.addStretch()
        self.flo.addWidget(self.entry_btn)
        self.flo.setGeometry(QtCore.QRect(100,70,200,50))

    def create_temp_label(self):
        '''
        static labales of temeratures at chosen day 
        in drop down list
        '''

        #make font
        self.font_lab = QtGui.QFont("Times",15)

        #create the label
        self.temp_label_1 = QtGui.QLabel(self)

        #set default text
        self.temp_label_1.setText("00:00 -- C")

        #spot on the screen label
        self.temp_label_1.setGeometry(350,150,150,50)

        #set font
        self.temp_label_1.setFont(self.font_date)

        #next is the same but others label
        self.temp_label_2 = QtGui.QLabel(self)
        self.temp_label_2.setText("03:00 -- C")
        self.temp_label_2.setGeometry(350,200,150,50)
        self.temp_label_2.setFont(self.font_date)

        self.temp_label_3 = QtGui.QLabel(self)
        self.temp_label_3.setText("06:00 -- C")
        self.temp_label_3.setGeometry(350,250,150,50)
        self.temp_label_3.setFont(self.font_date)

        self.temp_label_4 = QtGui.QLabel(self)
        self.temp_label_4.setText("09:00 -- C")
        self.temp_label_4.setGeometry(350,300,150,50)
        self.temp_label_4.setFont(self.font_date)

        self.temp_label_5 = QtGui.QLabel(self)
        self.temp_label_5.setText("12:00 -- C")
        self.temp_label_5.setGeometry(350,350,150,50)
        self.temp_label_5.setFont(self.font_date)

        self.temp_label_6 = QtGui.QLabel(self)
        self.temp_label_6.setText("15:00 -- C")
        self.temp_label_6.setGeometry(350,400,150,50)
        self.temp_label_6.setFont(self.font_date)

        self.temp_label_7 = QtGui.QLabel(self)
        self.temp_label_7.setText("18:00 -- C")
        self.temp_label_7.setGeometry(350,450,150,50)
        self.temp_label_7.setFont(self.font_date)

        self.temp_label_8 = QtGui.QLabel(self)
        self.temp_label_8.setText("21:00 -- C")
        self.temp_label_8.setGeometry(350,500,150,50)
        self.temp_label_8.setFont(self.font_date)


        
    def show_temp(self,text):
        '''
        when the date from drop down list is chosen it goes to this 
        function, and seperate what day is it and take temperature of 
        that day
        '''

        #set text of drop down list
        #because today and tomorrow is not a date we must change it
        #as a date string 
        if text == "today":
            text = self.today
        elif text == "tomorrow":
            text = self.tomorrow
            
        #helping and temporary lists
        self.hour_temp_list = []
        tmp_list = []

        #take from string important things like
        #hour and temp
        for i,date in enumerate(self.date_list):
            if text in date:
                self.hour_temp_list.append(date[11:16].encode("ascii")+" "+str(self.temp_list[i])+" C")
                tmp_list.append(date[11:16].encode("ascii"))


        #it sets labels when today and last day
        #are not full, so wouldnt be any problem with lists
        if len(tmp_list) == 7:
            if tmp_list[0] == "00:00":
                tmp_list.insert(7,'0')
                self.hour_temp_list.insert(7,'0')
            else:
                tmp_list.insert(0,'0')
                self.hour_temp_list.insert(0,'0')
        elif len(tmp_list) == 6:
            if tmp_list[0] == "06:00":
                for _ in range(2):
                    tmp_list.insert(0,'0')
                    self.hour_temp_list.insert(0,'0')
            else:
                for _ in range(2):
                    tmp_list.insert(6,'0')
                    self.hour_temp_list.insert(6,'0')
        elif len(tmp_list) == 5:
            if tmp_list[0] == "09:00":
                for _ in range(3):
                    tmp_list.insert(0,'0')
                    self.hour_temp_list.insert(0,'0')
            else:
                for _ in range(3):
                    tmp_list.insert(5,'0')
                    self.hour_temp_list.insert(5,'0')
        elif len(tmp_list) == 4:
            if tmp_list[0] == "12:00":
                for _ in range(4):
                    tmp_list.insert(0,'0')
                    self.hour_temp_list.insert(0,'0')
            else:
                for _ in range(4):
                    tmp_list.insert(4,'0')
                    self.hour_temp_list.insert(4,'0')
        elif len(tmp_list) == 3:
            if tmp_list[0] == "15:00":
                for _ in range(5):
                    tmp_list.insert(0,'0')
                    self.hour_temp_list.insert(0,'0')
            else:
                for _ in range(5):
                    tmp_list.insert(3,'0')
                    self.hour_temp_list.insert(3,'0')
        elif len(tmp_list) == 2:
            if tmp_list[0] == "18:00":
                for _ in range(6):
                    tmp_list.insert(0,'0')
                    self.hour_temp_list.insert(0,'0')
            else:
                for _ in range(6):
                    tmp_list.insert(2,'0')
                    self.hour_temp_list.insert(2,'0')
        elif len(tmp_list) == 1:
            if tmp_list[0] == "21:00":
                for _ in range(7):
                    tmp_list.insert(0,'0')
                    self.hour_temp_list.insert(0,'0')
            else:
                for _ in range(7):
                    tmp_list.insert(1,'0')
                    self.hour_temp_list.insert(1,'0')
        elif len(tmp_list) == 0:
            for _ in range(8):
                tmp_list.insert(0,'0')
                self.hour_temp_list.insert(0,'0')
                
                
        #setting our temp label as appropriate temperature and hour
        #if there is no hour today because we look forward not backward
        #than set label as default
        if str(tmp_list[0]) != '0':
            self.temp_label_1.setText(str(self.hour_temp_list[0]))
        else:
            self.temp_label_1.setText("00:00 -- C")

        #the same what upper
        if str(tmp_list[1]) != '0':
            self.temp_label_2.setText(str(self.hour_temp_list[1]))
        else:
            self.temp_label_2.setText("03:00 -- C")

        if str(tmp_list[2]) != '0':
            self.temp_label_3.setText(str(self.hour_temp_list[2]))
        else:
            self.temp_label_3.setText("06:00 -- C")

        if str(tmp_list[3]) != '0':
            self.temp_label_4.setText(str(self.hour_temp_list[3]))
        else:
            self.temp_label_4.setText("09:00 -- C")

        if str(tmp_list[4]) != '0':
            self.temp_label_5.setText(str(self.hour_temp_list[4]))
        else:
            self.temp_label_5.setText("12:00 -- C")

        if str(tmp_list[5]) != '0':
            self.temp_label_6.setText(str(self.hour_temp_list[5]))
        else:
            self.temp_label_6.setText("15:00 -- C")

        if str(tmp_list[6]) != '0':
            self.temp_label_7.setText(str(self.hour_temp_list[6]))
        else:
            self.temp_label_7.setText("18:00 -- C")

        if str(tmp_list[7]) != '0':
            self.temp_label_8.setText(str(self.hour_temp_list[7]))
        else:
            self.temp_label_8.setText("21:00 -- C")

    def search(self):
        '''search city in the internet and clear field'''

        #set name of city to look for
        self.city = str(self.entry_field.text()).capitalize()

        #clear data in entry field
        self.entry_field.clear()

        #get data from internet
        self.get_data()

        #ad change city label
        self.change_city_label()
        
        
    def close_application(self):
        '''close application'''
        
        sys.exit()
        
    def get_data(self):
        '''get data from API site'''

        #get Json object
        json = Json(self.city)

        #get data from internet
        self.date_list,self.temp_list = json.get_data_from_json()
        
        
