import model as model
import model_complex as model2
import view
import log

def button_click():
    value_x = view.get_value()
    value_f = view.get_sign()  # это ввод знака + - * /
    value_y = view.get_value()
    result = model.calculate(value_x, value_y, value_f)
    log.calculate_logger(value_x, value_f, value_y, result)
    return(result)
   


def button_click2():
    value_x = complex(view.get_value())
    value_f = view.get_sign()  # это ввод знака + - * /
    value_y = complex(view.get_value())
    result = model2.calc_complex_numbers(value_x, value_y, value_f)
    log.calc_complex_numbers_logger(value_x, value_f, value_y, result)
    return (result)
