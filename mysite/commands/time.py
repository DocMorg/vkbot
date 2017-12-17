import command_system
import mysql.connector
from flask import Flask, request, json

def answ(data):
   return data['user_id']

ap1 = Flask(__name__)
@ap1.route('/', methods=['POST'])
def time():
   message = 'Отлично, остался последний пункт!) \n Введи станцию метро, где ты хотел бы забрать свой заказ. \n Пока доступны на выбор: Планерная, Сходненская и Тушинская.'
   cnx = mysql.connector.connect(host='DocMorg.mysql.pythonanywhere-services.com',database='DocMorg$Delivery',user='DocMorg',password='123456qwe')
   cursor = cnx.cursor()
   data = json.loads(request.data)
   mi = data['object']
   mid = answ(data['object'])
   idy = 'vk.com/id' + str(mid)
   time = mi['body'].lower()
   add = "UPDATE delivery set time='%s' WHERE id='%s' ORDER BY number DESC LIMIT 1" % (time,idy)
   cursor.execute(add)
   cnx.commit()
   add = "UPDATE delivery set count='3' WHERE id='%s' ORDER BY number DESC LIMIT 1" % idy
   cursor.execute(add)
   cnx.commit()
   cursor.close()
   cnx.close()
   return message, ''

time_command = command_system.Command()

time_command.keys = ['time']
time_command.description = 'Добавить телефон'
time_command.process = time