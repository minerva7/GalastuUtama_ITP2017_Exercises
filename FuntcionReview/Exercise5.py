a = int(input('Input first number here: '))
b = int(input('Input second number here: '))
c = str(input('+ , - , * , /' + '\nInput your action from the choices above: ')).lower()
d = str(input('float / int' + '\nInput your output format: ')).lower()

def calculator(a, b, c, d):
    if c == '+' :
        result = a + b
    elif c == '-':
        result = a - b
    elif c == '*':
        result = a * b
    elif c == '/':
        result = float(a / b)
    else:
        result = 'Input +,-,*,or /'

    if d == 'int':
        return print(round(int(result)))
    elif d == 'float':
        return print(float(result))

calculator(a, b, c, d)
