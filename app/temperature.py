class Temperature:
    def __init__(self, temp, scale):
        self.temp = temp
        self.scale = scale
        
    def __str__(self):
        return f"{self.temp}\u00B0{self.scale}"

class Celsius(Temperature):
    def __init__(self, temp):
        super().__init__(temp, "C")
        
    def __str__(self):
        return super().__str__()
    
    def convertFahrenheit(self):
        return Fahrenheit((self.temp * 1.8) + 32)
    
class Fahrenheit(Temperature):
    def __init__(self, temp):
        super().__init__(temp, "F")
        
    def __str__(self):
        return super().__str__()
    
    def convertCelsius(self):
        return Celsius((self.temp - 32) / 1.8)