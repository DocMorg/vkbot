from flask import Flask, request, json
from settings import token, confirmation_token
import messageHandler

app = Flask(__name__)

@app.route('/', methods=['POST'])
def processing():
    data = json.loads(request.data)
    if 'type' not in data.keys():
        messageHandler.send_info(token)
        return 'not vk'
    if data['type'] == 'confirmation':
        return confirmation_token
    elif data['type'] == 'message_new':
        messageHandler.create_answer(data['object'], token)
        messageHandler.send_info(token)
        return 'ok'