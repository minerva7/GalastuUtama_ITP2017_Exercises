def factorial(a):
    try:
        if a == 1:
            return 1
        elif a == 0:
            return 1
        else:
            return a*factorial(a-1)
    except(RecursionError,TypeError):
        return None

w = float(input('Input number here: '))
if w > 1:
    print(int(factorial(w)))
elif 0 <= w <= 1:
    print(1)
