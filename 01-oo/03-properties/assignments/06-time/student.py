# Write your code here
class Time:
    def __init__(self, hours, minutes, seconds):
        self.__hours = 0
        self.__minutes = 0
        self.__seconds = 0
        
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds


    @property
    def hours(self):
        return self.__hours
        
    @hours.setter
    def hours(self, value):
        if value < 0 or value > 23:
            raise ValueError("hours must be between 0 & 23")
        else:
            self.__hours = value

        
    @property
    def minutes(self):
        return self.__minutes
        
    @minutes.setter
    def minutes(self, value):
        if value < 0 or value > 59:
            raise ValueError("minutes must be between 0 & 59")
        else:
            self.__minutes = value
                
        
    @property
    def seconds(self):
        return self.__seconds
        
    @seconds.setter
    def seconds(self, value):
        if value < 0 or value > 59:
            raise ValueError("seconds must be between 0 & 59")
        else:
            self.__seconds = value
                
        
        