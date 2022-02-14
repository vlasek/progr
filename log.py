from model import calculate
from model_complex import calc_complex_numbers
import controller

def calculate_logger(x, y, z, about):               # для модуля model.py
    with open('model_log.csv', 'a') as data:
        data.write(f'result: {x}{y}{z}={about}\n')
        

def calc_complex_numbers_logger(x, y, z, about):                # для модуля model_complex
    with open('model_log.csv', 'a') as data:
        data.write(f'result  {x}{y}{z}={about}\n')
