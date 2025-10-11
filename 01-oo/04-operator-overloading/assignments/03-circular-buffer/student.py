class CircularBuffer:
    def __len__(self, n):
        self.__n = n
    @property
    def n(self):
        return self.__n
    def __len__(self):
        return len(self.__n)
    
    def __add__(self, other):
        if not isinstance(other, CircularBuffer):
            return NotImplemented
        if other.n != self.__n:
            raise RuntimeError("Not the same object")
