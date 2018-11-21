class MyTime:
    def __init__(self, hours, minutes, seconds):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds
    
    def to_seconds(self):
        return (self.__hours*60*60)+(self.__minutes*60)+(self.__seconds)
    
    def equals(self, time2):
        return self.to_seconds() == time2.to_seconds()

    def __str__(self):
        return f"{self.__hours:02d}:{self.__minutes:02d}:{self.__seconds:02d}"

    def get_str_info(self):
        return f"{self.__hours:02d}:{self.__minutes:02d}:{self.__seconds:02d}"
