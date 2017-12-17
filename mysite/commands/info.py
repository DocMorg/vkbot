import command_system

def info()
   message = ''
   message += '? ' + 'Напиши Заказ для начала оформления заказа и выбора кофе.'+'n'
   return message, ''

info_command = command_system.Command()

info_command.keys = ['Помощь', 'помоги', 'help']
info_command.description = 'Покажу список команд'
info_command.process = info