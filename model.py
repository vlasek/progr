x = 6
y = 2
f = '-'

def calculate(x, y, f):
    x=float(x)
    y=float(y)
    if f == '+': return x+y
    elif f == '-': return x-y
    elif f == '*': return x*y
    elif f == '/': return x/y
    elif f!=('+','-','*','/'):return 'Введены не корректные данные'



print(calculate(5, 2, 3))
print(type(f))
