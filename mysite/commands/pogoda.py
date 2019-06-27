import command_system
from flask import Flask

from urllib.request import urlopen
import xml.etree.ElementTree as ET


def answ(data):
   return data['user_id']


def xmlconv():
    file = urlopen('https://api.openweathermap.org/data/2.5/find?q=Moscow&type=accurate&units=impearial&mode=xml&APPID=68b0969da63792a004f8c0fa027db8de')
    root = ET.fromstring(file.read().decode('utf-8'))
    file.close()
    return root


ap1 = Flask(__name__)
@ap1.route('/', methods=['POST'])
def pogoda():
    def getinfo():
        root = xmlconv()
        for list in root.findall('list'):
            for item in list.findall('item'):
                for city in item.findall('city'):
                    if city.find('country').text == 'RU':
                        c = 273.15
                        for temperature in item.findall('temperature'):
                            temp = str(round((float(temperature.get('value'))),2)-c)+'C°'
                        for humidity in item.findall('humidity'):
                            humid = str(humidity.get('value'))+'%'
        return humid,temp

    message = 'Moscow now: \n Humidity: %s \n Temparature: %s' % getinfo()
    return message, ''

pogoda_command = command_system.Command()

pogoda_command.keys = ['погода']
pogoda_command.description = 'Показать погоду'
pogoda_command.process = pogoda
