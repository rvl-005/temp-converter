from app.temperature import Celsius as cel, Fahrenheit as fah, Kelvin as kel

tempInput = float(input("Enter the temperature you want to convert: "))
scaleInput = input("Enter the scale of the temperature you entered (Celsius, Fahrenheit, or Kelvin): ")
newScale = input("Enter the scale you want to convert the temperature to (Celsius, Fahrenheit, or Kelvin): ")

def convertTemperature(tempInput, scaleInput, newScale):
    conversions = {
        ("Celsius", "Celsius"): cel(tempInput).convertCelsius,
        ("Celsius", "Fahrenheit"): cel(tempInput).convertFahrenheit,
        ("Celsius", "Kelvin"): cel(tempInput).convertKelvin,
        ("Fahrenheit", "Celsius"): fah(tempInput).convertCelsius,
        ("Fahrenheit", "Fahrenheit"): fah(tempInput).convertFahrenheit,
        ("Fahrenheit", "Kelvin"): fah(tempInput).convertKelvin,
        ("Kelvin", "Celsius"): kel(tempInput).convertCelsius,
        ("Kelvin", "Fahrenheit"): kel(tempInput).convertFahrenheit,
        ("Kelvin", "Kelvin"): kel(tempInput).convertKelvin
    }
    return conversions.get((scaleInput, newScale))()