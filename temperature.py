import board
import analogio

tmp36 = analogio.AnalogIn(board.A0)

def get_temperature():
    voltage = tmp36.value * 3.3 / 65536
    temperature = (voltage - 0.5) * 100
    return temperature