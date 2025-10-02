#خاصية محسوبة (بدون setter) في كلاس

class Bewoner:
    def __init__(self, naam):
        self.__naam = ""
        self.naam = naam
    
    @property
    def naam(self):
        return self.__naam
    
    @property
    def aantal_letters(self):
        return len(self.naam)
    
# with setter
    @naam.setter
    def naam(self, new_name):
        if len(new_name) < 2:
            raise ValueError("Write your name fully plz")
        self.__naam = new_name

#voorbeelden
b = Bewoner("omar")
print(b.naam)
print(b.aantal_letters)
a = Bewoner("S")
print(a.naam)
print(a.aantal_letters)