import command_system
import mysql.connector
from flask import Flask, request, json

def answ(data):
   return data['user_id']

ap1 = Flask(__name__)
@ap1.route('/', methods=['POST'])
def zakaz():
    message = 'Так, понял, что заказываем?\n Смотри, у нас есть:\n •Капучино\n •Американо\n •Латте\n •Эспрессо\n Тебе какой? '
    cnx = mysql.connector.connect(host='DocMorg.mysql.pythonanywhere-services.com',database='DocMorg$Delivery',user='DocMorg',password='123456qwe')
    cursor = cnx.cursor()
    data = json.loads(request.data)
    mid = answ(data['object'])
    idy = 'vk.com/id' + str(mid)
    add = "INSERT INTO delivery (id) VALUES ('%s')" % (idy)
    cursor.execute(add)
    cnx.commit()
    add = "UPDATE delivery set count='0' WHERE id='%s' ORDER BY number DESC LIMIT 1" % idy
    cursor.execute(add)
    cnx.commit()
    cursor.close()
    cnx.close()
    return message, ''

zakaz_command = command_system.Command()

zakaz_command.keys = ['Заказ', 'заказать', 'хочу заказать']
zakaz_command.description = 'Начать оформление заказа'
zakaz_command.process = zakaz