import command_system

def info()
   message = ''
   message += '? ' + '������ ����� ��� ������ ���������� ������ � ������ ����.'+'n'
   return message, ''

info_command = command_system.Command()

info_command.keys = ['������', '������', 'help']
info_command.description = '������ ������ ������'
info_command.process = info