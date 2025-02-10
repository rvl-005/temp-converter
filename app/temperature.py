class Temperature:
    def __init__(self, temp, scale):
        self.temp = temp
        self.scale = scale
        
    def __str__(self):
        return f"{self.temp}\u00B0{self.scale}"
