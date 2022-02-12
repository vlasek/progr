from model import calculate
from model_complex import calc_complex_numbers


def calculate_logger(data):               # для модуля model.py
    with open('model_log.csv', 'a') as data:
        data.write(f'result = {calculate}\n')
        

def calc_complex_numbers_logger(data):                # для модуля model_complex
    with open('model_compl.csv', 'a') as data:
        data.write(f'result = {calc_complex_numbers}\n')
