import command_system

def hello():
   message = 'Привет!\nЯ новый чат-бот.\n Напиши "заказ", чтобы заказать кофе!'
   return message, ''

hello_command = command_system.Command()

hello_command.keys = ['Привет', 'hello', 'дратути', 'здравствуй', 'здравствуйте', 'дороу', 'ку']
hello_command.description = 'Поприветствую тебя'
hello_command.process = hello