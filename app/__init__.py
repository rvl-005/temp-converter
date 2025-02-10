import temperature as temp
    
tempInput = int(input("Enter the temperature you want to convert: "))
scaleInput = input("Enter the scale of the temperature you entered (C/F): ")
newTemp = temp.Temperature(tempInput, scaleInput)
print(f"Temperature in {scaleInput}: {newTemp}")