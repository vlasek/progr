import model as model
import model_complex as model2
import view

def button_click():
    value_x=view.get_value()
    value_f=view.get_value() # это ввод знака + - * /
    value_y=view.get_value()
    # model.init(value_x, value_y, value_f)
    result=model.calculate(value_x, value_y, value_f)
    # view.view_data(result, "result")
    print(f'результат операции {value_x} {value_f} {value_y} =  {result}')

def button_click2():
    value_x=view.get_value()
    value_f=view.get_value() # это ввод знака + - * /
    value_y=view.get_value()
    # model2.init(value_x, value_y, value_f)
    result=model2.calc_complex_numbers()
    # view.view_data(result, "result")