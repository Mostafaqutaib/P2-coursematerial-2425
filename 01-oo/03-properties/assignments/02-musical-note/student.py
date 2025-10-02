class MusicalNote:
    def __init__(self, name, pitch):
        self.__name = name
        self.__pitch = pitch
    
    @property
    def name(self):
        return self.__name
    @property
    def pitch(self):
        return self.__pitch
    

note = MusicalNote('a4', 440)
print(note.pitch)
