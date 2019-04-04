from abc import abstractmethod, ABC

class Temperature (ABC):
    @abstractmethod
    def __init__(self, temperature):
        pass
    
    @abstractmethod
    def __str__(self):
        pass
    
    @abstractmethod
    def aboveFreezing(self):
        pass
    
    @abstractmethod
    def convertToFahrenheit(self):
        pass
    
    @abstractmethod
    def convertToCelsius(self):
        pass
    
    @abstractmethod
    def convertToKelvin(self):
        pass
    


