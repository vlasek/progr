
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

# тестирование
x=(5+4j)
y=(4+4j)
f='+'
# print(complex(x))
# print(complex(y))
print(f)
print(calc_complex_numbers(x, y, f))