from convertTemp import convertTemperature, tempInput, scaleInput, newScale

while True:
    try:
        newTemp = convertTemperature(tempInput, scaleInput, newScale)
        newTemp.temp = round(newTemp.temp, 2)
        if newTemp.temp.is_integer() == True:
            newTemp.temp = int(newTemp.temp)
        print(f"New Temperature: {newTemp}")
        break
    except ValueError:
        print("Invalid input. Please enter a number for the temperature.")
    except AttributeError:
        print("Invalid scale. This scale supports Celsius, Fahrenheit, and Kelvin. Please try again.")