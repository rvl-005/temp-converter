from temperature import Temperature as temp, Celsius as cel, Fahrenheit as fah


tempInput = float(input("Enter the temperature you want to convert: "))
scaleInput = input("Enter the scale of the temperature you entered (C/F): ")

def ConvertTemperature(tempInput, scaleInput):
    if scaleInput == "C":
        return cel(tempInput).convertFahrenheit()
    elif scaleInput == "F":
        return fah(tempInput).convertCelsius()
    else:
        return "Invalid scale"
newTemp = ConvertTemperature(tempInput, scaleInput)
print(f"Temperature in {newTemp.scale}: {newTemp.temp}")