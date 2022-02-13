import controller as c
import print_result


mode1 = int(input('Введите режим работы калькулятора: \n1 - рационалные числа, 0 - комплексные: \n'))
if mode1 == 1:
    print_result.print_about(c.button_click())
else:
    print_result.print_about(c.button_click2())

