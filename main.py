import controller
import controller as c
import log

mode1 = int(input('Введите режим работы калькулятора: \n1 - рационалные числа, 0 - комплексные: \n'))
if mode1 == 1:
    c.button_click()
else:
    c.button_click2()

