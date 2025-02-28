from temperature import Celsius as cel, Fahrenheit as fah, Kelvin as kel

try:
    tempInput = float(input("Enter the temperature you want to convert: "))
    scaleInput = input("Enter the scale of the temperature you entered (Celsius, Fahrenheit, or Kelvin): ")
    newScale = input("Enter the scale you want to convert the temperature to (Celsius, Fahrenheit, or Kelvin): ")

    def ConvertTemperature(tempInput, scaleInput, newScale):
        if scaleInput == "Celsius":
            if newScale == "Fahrenheit":
                return cel(tempInput).convertFahrenheit()
            elif newScale == "Kelvin":
                return cel(tempInput).convertKelvin()
        elif scaleInput == "Fahrenheit":
            if newScale == "Celsius":
                return fah(tempInput).convertCelsius()
            elif newScale == "Kelvin":
                return fah(tempInput).convertKelvin()
            return fah(tempInput).convertCelsius()
        elif scaleInput == "Kelvin":
            if newScale == "Celsius":
                return kel(tempInput).convertCelsius()
            elif newScale == "Fahrenheit":
                return kel(tempInput).convertFahrenheit()

    newTemp = ConvertTemperature(tempInput, scaleInput, newScale)
    if newTemp.temp.is_integer() == True:
        newTemp.temp = int(newTemp.temp)
    print(f"Temperature in {newScale}: {newTemp}")
except ValueError:
    print("Invalid input. Please enter a number for the temperature.")
except AttributeError:
    print("Invalid scale. This scale supports Celsius, Fahrenheit, and Kelvin. Please try again.")