def calculator(c='+',d='float',*a):
    if a:
        result =a[0]
        if c == '+' :
            for i in a[1:]:
                result += i
        elif c == '-':
            for i in a[1:]:
                result -= i
        elif c == '*':
            for i in a[1:]:
                result -= i
        elif c == '/':
            for i in a[1:]:
                result /= float(i)
        else:
            for i in a[1:]:
                result = 'Input +,-,*,or /'

        if d == 'int':
            return print(round(int(result)))
        elif d == 'float':
            return print(float(result))
    else:
        raise Exception('no input!')

def check(b):
    nums = []
    if b == " ":
        return nums
    elif len(b) == 1:
        nums.append(int(b))
        return nums
    elif ',' in b:
        b = b.split(',')
        print(b)
        for i in b:
            if '.' in i:
                nums.append(float(i))
            elif '.' not in i:
                nums.append(int(i))
        return nums
    elif ' ' in b:
        b = b.split(' ')
        print(b)
        for i in b:
            if ' ' in i:
                nums.append(float(i))
            elif ' ' in i:
                nums.append(int(i))
        return nums
    elif '.' in b:
        nums.append(float(b))
        return nums

calculator('+','int',5,9,9,6)
