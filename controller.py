import model as model
import view

def button_click():
    value_a=view.get_vlaue()
    value_d=view.get_value() # это ввод знака + - * /
    value_b=view.get_vlaue()
    model.init(value_a, value_d, value_b)
    result=model.calculate()
    view.view_data(result, "result")