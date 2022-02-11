def calc_complex_numbers(x, y, f):
    if f == '-':
        return complex(x) - complex(y)
    elif f == '+':
        return complex(x) + complex(y)
    elif f == '*':
        return complex(x) * complex(y)
    elif f == '/':
        return complex(x) / complex(y)
    