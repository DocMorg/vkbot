import command_system
import mysql.connector
from flask import Flask, request, json

def answ(data):
   return data['user_id']

ap1 = Flask(__name__)
@ap1.route('/', methods=['POST'])
def phone():
   message = 'В какое время вы хотели бы забрать свой заказ?\n Можете выбрать любое с 6 до 10 утра.'
   cnx = mysql.connector.connect(host='DocMorg.mysql.pythonanywhere-services.com',database='DocMorg$Delivery',user='DocMorg',password='123456qwe')
   cursor = cnx.cursor()
   data = json.loads(request.data)
   mi = data['object']
   mid = answ(data['object'])
   idy = 'vk.com/id' + str(mid)
   phon = mi['body'].lower()
   add = "UPDATE delivery set phone='%s' WHERE id='%s' ORDER BY number DESC LIMIT 1" % (phon,idy)
   cursor.execute(add)
   cnx.commit()
   add = "UPDATE delivery set count='2' WHERE id='%s' ORDER BY number DESC LIMIT 1" % idy
   cursor.execute(add)
   cnx.commit()
   cursor.close()
   cnx.close()
   return message, ''

latte_command = command_system.Command()

latte_command.keys = ['telephone']
latte_command.description = 'Добавить телефон'
latte_command.process = phone