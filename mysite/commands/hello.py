import command_system

def hello():
   message = '������!\n� ����� ���-���.\n ������ "�����", ����� �������� ����!'
   return message, ''

hello_command = command_system.Command()

hello_command.keys = ['������', 'hello', '�������', '����������', '������������', '�����', '��']
hello_command.description = '������������� ����'
hello_command.process = hello