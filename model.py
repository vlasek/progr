def calculate(x, y, f):
    x=float(x)
    y=float(y)
    if f == '+': return x+y
    elif f == '-': return x-y
    elif f == '*': return x*y
    elif f == '/': return x/y
    elif f!=('+','-','*','/'):return 'Введены не корректные данные'




