from temperature import Celsius as cel, Fahrenheit as fah, Kelvin as kel

tempInput = float(input("Enter the temperature you want to convert: "))
scaleInput = input("Enter the scale of the temperature you entered (Celsius, Fahrenheit, or Kelvin): ")
newScale = input("Enter the scale you want to convert the temperature to (Celsius, Fahrenheit, or Kelvin): ")

def convertTemperature(tempInput, scaleInput, newScale):
    match scaleInput:
        case "Celsius":
            if newScale == "Fahrenheit":
                return cel(tempInput).convertFahrenheit()
            elif newScale == "Kelvin":
                return cel(tempInput).convertKelvin()
        case "Fahrenheit":
            if newScale == "Celsius":
                return fah(tempInput).convertCelsius()
            elif newScale == "Kelvin":
                return fah(tempInput).convertKelvin()
        case "Kelvin":
            if newScale == "Celsius":
                return kel(tempInput).convertCelsius()
            elif newScale == "Fahrenheit":
                return kel(tempInput).convertFahrenheit()