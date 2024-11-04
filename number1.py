# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 08:05:51 2024

@author: KYLE FRANZ RODRIGUEZ
"""

def main():
    class TemperatureConversion:
        def __init__(self, temp=1):
            self._temp = temp
    class CelsiusToFahrenheit(TemperatureConversion):
        def conversion(self):
            return (self._temp * 9) / 5 + 32
    class CelsiusToKelvin(TemperatureConversion):
        def conversion(self):
            return self._temp + 273.15
    class FahrenheitToCelsius(TemperatureConversion):
        def conversion(self):
            return (self._temp - 32) * 5 / 9
    class KelvinToCelsius(TemperatureConversion):
        def conversion(self):
            return self._temp - 273.15
    tempInCelsius = float(input("Enter the temperature in Celsius: "))
    convert = CelsiusToKelvin(tempInCelsius)
    print(str(convert.conversion()) + " Kelvin")
    convert = CelsiusToFahrenheit(tempInCelsius)
    print(str(convert.conversion()) + " Fahrenheit")
    #Additional
    tempInFahren = float(input("Enter the temperature in Fahrenheit: "))
    convert = FahrenheitToCelsius(tempInFahren)
    print(str(convert.conversion()) + " Celsius")
    tempInKelvin = float(input("Enter the temperature in Kelvin: "))
    convert = KelvinToCelsius(tempInKelvin)
    print(str(convert.conversion()) + " Celsius")

main()