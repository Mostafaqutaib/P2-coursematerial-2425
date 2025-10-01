class Queue:
    def __init__(self):
        self.__queue = []
    
    @property
    def queue(self):
        return self.__queue
    
    def add(self, item):
        self.__queue.append(item)
    
    def next(self):
        new_list = [] # I make new list to copy the list of self.__queue --> pop(0) delete the first item in the queue  
        for i in self.__queue:
            new_list.append(i)
        new_list.pop(0)
        self.__queue = new_list
    def is_empty(self):
        if len(self.__queue) == 0:
            return True
        else:
            False
        
    