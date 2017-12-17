import vkapi
import os
import importlib
from command_system import command_list
import MySQLdb as my
import mysql.connector
from flask import Flask, request, json

def answ(data):
   return data['user_id']

def load_modules():
   files = os.listdir("mysite/commands")
   modules = filter(lambda x: x.endswith('.py'), files)
   for m in modules:
       importlib.import_module("commands." + m[0:-3])

ap1 = Flask(__name__)
@ap1.route('/', methods=['POST'])
def get_answer(body):
   message = "Прости, не понимаю тебя. Напиши 'помощь', чтобы узнать мои команды"
   attachment = ''
   distance = len(body)
   command = None
   data = json.loads(request.data)
   mid = answ(data['object'])
   idy = 'vk.com/id' + str(mid)
   cnx = mysql.connector.connect(host='DocMorg.mysql.pythonanywhere-services.com',database='DocMorg$Delivery',user='DocMorg',password='123456qwe')
   try:
       cursor = cnx.cursor()
       cursor.execute("SELECT count FROM delivery WHERE id='%s' ORDER BY number DESC LIMIT 1" % idy)
       count = cursor.fetchone()
       count = int((str(count))[1])
   except (my.DataError,my.InternalError, my.IntegrityError, my.OperationalError, my.NotSupportedError, my.ProgrammingError, ValueError):
       count = 0
   cursor.close()
   cnx.close()
   key = ''
   if count == 1:
       body = 'telephone'
       distance = len(body)
   if count == 2:
       body = 'time'
       distance = len(body)
   if count == 3:
       body = 'metro'
       distance = len(body)
   for c in command_list:
       for k in c.keys:
            d = damerau_levenshtein_distance(body, k)
            if d < distance:
                distance = d
                command = c
                key = k
                if distance == 0:
                    message, attachment = c.process()
                    return message, attachment
       if distance < len(body)*0.4:
            message, attachment = command.process()
            message = 'Я понял ваш запрос как "%s"\n\n' % key + message
   return message, attachment

def create_answer(data, token):
   load_modules()
   user_id = data['user_id']
   message, attachment = get_answer(data['body'].lower())
   vkapi.send_message(user_id, token, message, attachment)


ap2 = Flask(__name__)
@ap2.route('/', methods=['POST'])
def send_info(token):
    data = json.loads(request.data)
    mid = answ(data['object'])
    idy = 'vk.com/id' + str(mid)
    cnx = mysql.connector.connect(host='DocMorg.mysql.pythonanywhere-services.com',database='DocMorg$Delivery',user='DocMorg',password='123456qwe')
    try:
        cursor = cnx.cursor()
        cursor.execute("SELECT count FROM delivery WHERE id='%s' ORDER BY number DESC LIMIT 1" % idy)
        count = cursor.fetchone()
        count = int((str(count))[1])
    except (my.DataError,my.InternalError, my.IntegrityError, my.OperationalError, my.NotSupportedError, my.ProgrammingError, ValueError):
        count = 0
    if count == 4:
        load_modules()
        user_id = '112350426'
        cursor.execute("SELECT number FROM delivery WHERE id='%s' ORDER BY number DESC LIMIT 1" % idy)
        int1 = (cursor.fetchone())[0]
        message = 'Номер заказа: ' + str(int1) + '\n'
        cursor.execute("SELECT id FROM delivery WHERE id='%s' ORDER BY number DESC LIMIT 1" % idy)
        message = message + 'id: ' + ''.join(cursor.fetchone()) + '\n'
        cursor.execute("SELECT metro FROM delivery WHERE id='%s' ORDER BY number DESC LIMIT 1" % idy)
        message = message + 'Метро: ' + ''.join(cursor.fetchone()) + '\n'
        cursor.execute("SELECT time FROM delivery WHERE id='%s' ORDER BY number DESC LIMIT 1" % idy)
        message = message + 'Время: ' +  str(''.join(cursor.fetchone())) + '\n'
        cursor.execute("SELECT coffe FROM delivery WHERE id='%s' ORDER BY number DESC LIMIT 1" % idy)
        message = message + 'Кофе: ' + ''.join(cursor.fetchone()) + '\n'
        cursor.execute("SELECT phone FROM delivery WHERE id='%s' ORDER BY number DESC LIMIT 1" % idy)
        message = message + 'Телефон: ' + ''.join(cursor.fetchone())
        attachment = ''
        vkapi.send_message(user_id, token, message, attachment)
        add = "UPDATE delivery set count='5' WHERE id='%s' ORDER BY number DESC LIMIT 1" % idy
        cursor.execute(add)
        cnx.commit()
        cursor.close()
        cnx.close()

def damerau_levenshtein_distance(s1, s2):
   d = {}
   lenstr1 = len(s1)
   lenstr2 = len(s2)
   for i in range(-1, lenstr1 + 1):
       d[(i, -1)] = i + 1
   for j in range(-1, lenstr2 + 1):
       d[(-1, j)] = j + 1
   for i in range(lenstr1):
       for j in range(lenstr2):
           if s1[i] == s2[j]:
               cost = 0
           else:
               cost = 1
           d[(i, j)] = min(
               d[(i - 1, j)] + 1,  # deletion
               d[(i, j - 1)] + 1,  # insertion
               d[(i - 1, j - 1)] + cost,  # substitution
           )
           if i and j and s1[i] == s2[j - 1] and s1[i - 1] == s2[j]:
               d[(i, j)] = min(d[(i, j)], d[i - 2, j - 2] + cost)  # transposition
   return d[lenstr1 - 1, lenstr2 - 1]