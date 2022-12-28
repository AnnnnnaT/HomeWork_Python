from random import randint as ri


def get_temperature(sensor):
    return ri(-20, 0) if sensor else ri(0, 20)


def get_pressure(sensor):
    return ri(720, 750) if sensor else ri(750, 770)


def get_wind_speed(sensor):
    return ri(0, 30) if sensor == 1 else ri(30, 50)
