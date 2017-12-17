import command_system
import mysql.connector
from flask import Flask, request, json

def answ(data):
   return data['user_id']

ap1 = Flask(__name__)
@ap1.route('/', methods=['POST'])
def espresso():
   message = 'Всё понятно, я записал \n А можно узнать твой телефон?'
   cnx = mysql.connector.connect(host='DocMorg.mysql.pythonanywhere-services.com',database='DocMorg$Delivery',user='DocMorg',password='123456qwe')
   cursor = cnx.cursor()
   data = json.loads(request.data)
   mid = answ(data['object'])
   idy = 'vk.com/id' + str(mid)
   add = "UPDATE delivery set coffe='Эспрессо' WHERE id='%s' ORDER BY number DESC LIMIT 1" % idy
   cursor.execute(add)
   cnx.commit()
   add = "UPDATE delivery set count='1' WHERE id='%s' ORDER BY number DESC LIMIT 1" % idy
   cursor.execute(add)
   cnx.commit()
   cursor.close()
   cnx.close()
   return message, ''

espresso_command = command_system.Command()

espresso_command.keys = ['эспрессо']
espresso_command.description = 'Заказать эспрессо'
espresso_command.process = espresso