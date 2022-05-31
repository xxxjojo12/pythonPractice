from sys import stdin

operators = ['+', '-', '*', '/']

operation_expression = stdin.readline().rstrip()

num1, num2, operator = None, None, None

for oper in operators:
    if oper in operation_expression:
        operator = oper
        num1, num2 = map(int, operation_expression.split(operator))

if operator == '+':
    print(num1+num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '*':
    print(num1 * num2)
else:
    print('%.2f' % (num1/num2))