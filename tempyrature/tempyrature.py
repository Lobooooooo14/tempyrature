class Converter:
    def __init__(self) -> None:
        """
        A simple temperature converter.
        """
        pass


    def celsius2fahrenheit(celsius: float) -> float:
        fahrenheit = 1.8 * celsius + 32
        return fahrenheit


    def fahrenheit2celsius(fahrenheit: float) -> float:
        celsius = (fahrenheit - 32) / 1.8
        return celsius


    def celsius2kelvin(celsius: float) -> float:
        kelvin = celsius + 273.15
        return kelvin


    def kelvin2celsius(kelvin: float) -> float:
        celsius = kelvin - 273.15
        return celsius


    def fahrenheit2kelvin(fahrenheit: float) -> float:
        kelvin = 273.15 + ((fahrenheit - 32.0) * (5.0/9.0))
        return kelvin


    def kelvin2fahrenheit(kelvin: float) -> float:
        fahrenheit = 1.8 * (kelvin - 273.15) - 32
        return fahrenheit
