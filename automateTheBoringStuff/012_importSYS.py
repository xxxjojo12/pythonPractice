import sys

while 1:
    print('Type exit to exit')
    response = input()
    if response == 'exit':
        sys.exit()
    print(f'You typed {response}')