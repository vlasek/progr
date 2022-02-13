# request не получисля вставил строчки Сергея
def calc_complex_numbers(x, y, f):
    if f == '-':
        return complex(x) - complex(y)
    elif f == '+':
        return complex(x) + complex(y)
    elif f == '*':
        return complex(x) * complex(y)
    elif f == '/':
        return complex(x) / complex(y)
    elif f!=('+','-','*','/'):return 'Введены не корректные данные'

print(calc_complex_numbers(2,3,'+'))


