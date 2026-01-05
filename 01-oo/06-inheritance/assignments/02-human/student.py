class Human:
    def __init__(self, name):
        self.__name = name
    
    @property
    def name(self):
        return self.__name


class Archer:
    def __init__(self, name , num_arrows):
        super().__init__(name)
        self.__num_arrows = num_arrows
    @property
    def num_arrows(self):
        return self.__num_arrows
    
        