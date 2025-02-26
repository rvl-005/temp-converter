from temperature import Celsius as cel, Fahrenheit as fah


tempInput = float(input("Enter the temperature you want to convert: "))
scaleInput = input("Enter the scale of the temperature you entered (Celsius/Fahrenheit): ")

def ConvertTemperature(tempInput, scaleInput):
    if scaleInput == "Celsius":
        return cel(tempInput).convertFahrenheit()
    elif scaleInput == "Fahrenheit":
        return fah(tempInput).convertCelsius()
    else:
        return "Invalid scale"
newTemp = ConvertTemperature(tempInput, scaleInput)
if newTemp.temp.is_integer() == True:
    newTemp.temp = int(newTemp.temp)
print(f"Temperature in {newTemp.scale}: {newTemp}")