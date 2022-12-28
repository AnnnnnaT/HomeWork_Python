from datetime import datetime as dt


def temperature_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a', encoding='UTF-8') as file:
        file.write(f'{time}; temperature: {data}\n')


def pressure_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a', encoding='UTF-8') as file:
        file.write(f'{time}; pressure; {data}\n')


def wind_speed_loger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a', encoding='UTF-8') as file:
        file.write(f'{time}; wind_speed; {data}\n')
