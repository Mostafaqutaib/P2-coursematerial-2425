class LengthConverter:
    def __init__(self):
        self.__meter = 0.0
    
    @property
    def meter(self):
        return self.__meter

    @meter.setter
    def meter(self, value):
        
        self.__meter = float(value)


    @property
    def feet(self):
        self.__feet = self.__meter * 3.28084
        return self.__feet

    @feet.setter
    def feet(self, value):
        self.__meter = float(value) / 3.28084

    @property
    def inch(self):
        self.__inch = self.__meter * 39.3701
        return self.__inch
    
    @inch.setter
    def inch(self, value):
        self.__meter = float(value) / 39.3701

converter = LengthConverter()
converter.meter = 100
print(converter.meter)
print(converter.feet)