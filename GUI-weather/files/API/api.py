import requests
import math
import json
import datetime

class Json:
    '''
    Class to retrieve data from API 
    '''

    def __init__(self,city_name):
        #determine city in which the temerature will be check
        
        self.city_name = city_name
    
    def get_json(self):
        #download information as json text
        #and return text
        
        self.link = 'http://api.openweathermap.org/data/2.5/forecast?q={}&appid=b07ad1b517ff23c9bdbd2b76e3f6dcc3'.format(self.city_name)
        self.r = requests.get(self.link)
        return self.r.json()


    def get_data_from_json(self):
        #from json text, search information
        #about date and temerature at this time
        #return list of two list with datas

        self.date_list = []
        self.temp_list = []
        self.content = self.get_json()
        for c in self.content["list"]:
            self.date_list.append(c["dt_txt"])
            self.temp_list.append(math.floor(c["main"]["temp"]-273))

        self.save_to_file()
        return [self.date_list,self.temp_list]

    def save_to_file(self):
        with open("/home/mtesluk/python/weather/project/history/{}_{}.json".format(self.city_name,datetime.date.today()),"a") as f:
            json.dump(self.content,f,indent=2)

