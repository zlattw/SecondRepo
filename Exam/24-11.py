class Temperature:
    def __init__(self, temperature: float):
        self.set_temperature(temperature)

    def celsius_to_fahrenheit(self):
        return (self.temperature * 9/5) + 32

    def fahrenheit_to_celsius(self):
        return (self.temperature - 32) * 5/9

    def set_temperature(self, temperature: float):
        if temperature < -273.15:
            raise ValueError("!!!Температура не може бути нижче -273.15")
        self.temperature = temperature

try:
    temp = Temperature(30)
    print(f"Температура у Фаренгейтах - {temp.celsius_to_fahrenheit()}")
    temp.set_temperature(-278)
except ValueError as error:
    print(error)

try:
    temp = Temperature(99)
    print(f"Температура в Цельсіях - {temp.fahrenheit_to_celsius()}")
except ValueError as error:
    print(error)