class Queue:
    def __init__(self):
        self.__queue = []
    
    def add(self, item):
        self.__queue.append(item)
    
    def next(self):
        if self.is_empty() == True:
            raise ValueError("Queue is empty")
        return self.__queue.pop(0)
    
    def is_empty(self):
        if len(self.__queue) == 0:
            return True
        else:
            False
