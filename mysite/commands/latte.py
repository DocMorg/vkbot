import command_system
import mysql.connector
from flask import Flask, request, json

def answ(data):
   return data['user_id']

ap1 = Flask(__name__)
@ap1.route('/', methods=['POST'])
def latte():
   message = 'Всё понятно, я записал \n А можно узнать твой телефон?'
   cnx = mysql.connector.connect(host='DocMorg.mysql.pythonanywhere-services.com',database='DocMorg$Delivery',user='DocMorg',password='123456qwe')
   cursor = cnx.cursor()
   data = json.loads(request.data)
   mid = answ(data['object'])
   idy = 'vk.com/id' + str(mid)
   add = "UPDATE delivery set coffe='Латте' WHERE id='%s' ORDER BY number DESC LIMIT 1" % idy
   cursor.execute(add)
   cnx.commit()
   add = "UPDATE delivery set count='1' WHERE id='%s' ORDER BY number DESC LIMIT 1" % idy
   cursor.execute(add)
   cnx.commit()
   cursor.close()
   cnx.close()
   return message, ''

latte_command = command_system.Command()

latte_command.keys = ['Латте']
latte_command.description = 'Заказать латте'
latte_command.process = latte