import command_system
import mysql.connector
from flask import Flask, request, json

def answ(data):
   return data['user_id']

ap1 = Flask(__name__)
@ap1.route('/', methods=['POST'])
def metro():
   message = 'Ваш заказ принят! Ожидайте звонка, либо сообщения Вконтакте, когда ваш заказ будет доставлен к метро^^'
   cnx = mysql.connector.connect(host='DocMorg.mysql.pythonanywhere-services.com',database='DocMorg$Delivery',user='DocMorg',password='123456qwe')
   cursor = cnx.cursor()
   data = json.loads(request.data)
   mi = data['object']
   mid = answ(data['object'])
   idy = 'vk.com/id' + str(mid)
   metr = mi['body'].lower()
   add = "UPDATE delivery set metro='%s' WHERE id='%s' ORDER BY number DESC LIMIT 1" % (metr,idy)
   cursor.execute(add)
   cnx.commit()
   add = "UPDATE delivery set count='4' WHERE id='%s' ORDER BY number DESC LIMIT 1" % idy
   cursor.execute(add)
   cnx.commit()
   cursor.close()
   cnx.close()
   return message, ''

metro_command = command_system.Command()

metro_command.keys = ['metro']
metro_command.description = 'Добавить станцию метро'
metro_command.process = metro