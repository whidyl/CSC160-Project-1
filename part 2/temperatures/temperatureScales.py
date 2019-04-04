from temperature import Temperature

class Fahrenheit(Temperature):
    """ Represents fahrenheit temperature 
    Attributes
    ----------
    temperature : float
        degrees in fahrenheit
    """
    def __init__(self, temperature):
        self.temperature = temperature
    
    def __str__(self):
        """ returns string representation"""
        freezingInfo = ""
        if self.aboveFreezing():
            freezingInfo = "[above freezing] "
        return str(self.temperature) + " degrees fahrenheit " + freezingInfo

    def aboveFreezing(self):
        """ Returns true if temperature is above freezing point of water """
        return self.temperature > 32

    def convertToCelsius(self):
        """ returns converted celsius object """
        return Celcius((self.temperature - 32) * (5/9))
    
    def convertToKelvin(self):
        """ returns converted kelvin object """
        return Kelvin((self.temperature - 32) * (5/9) + 273.15)
    
    def convertToFahrenheit(self): 
        """ returns self because it's redundant """
        return self
    
class Celcius(Temperature):
    """ Represents celcius temperature 
    Attributes
    ----------
    temperature : float
        degrees in celcius
    """
    def __init__(self, temperature):
        self.temperature = temperature
    
    def __str__(self):
        """ returns string representation"""
        freezingInfo = ""
        if self.aboveFreezing():
            freezingInfo = "[above freezing] "
        return str(self.temperature) + " degrees celcius " + freezingInfo


    def aboveFreezing(self):
        """ Returns true if temperature is above freezing point of water """
        return self.temperature > 0

    def convertToKelvin(self):
        """ returns converted kelvin object """
        return Kelvin(self.temperature +  273.15)
    
    def convertToFahrenheit(self):
        """ returns converted fahrenheit object """
        return Fahrenheit((self.temperature * (9/5)) + 32)
    
    def convertToCelsius(self):
        """ returns self because it's redundant """
        return self
  
class Kelvin(Temperature):
    """ Represents kelvin temperature 
    Attributes
    ----------
    temperature : float
        degrees in kelvin
    """
    def __init__(self, temperature):
        self.temperature = temperature  
    
    def __str__(self):
        """ returns string representation"""
        freezingInfo = ""
        if self.aboveFreezing():
            freezingInfo = "[above freezing] "
        return str(self.temperature) + " degrees kelvin " + freezingInfo

    def aboveFreezing(self):
        """ Returns true if temperature is above freezing point of water """
        return self.temperature > 0

    def convertToCelsius(self):
        """ returns converted celsius object """
        return Celcius(self.temperature - 273.15)
    
    def convertToFahrenheit(self):
        """ returns converted fahrenheit object """
        return Fahrenheit((self.temperature  - 273.15)*(9/5) + 32)
    
    def convertToKelvin(self):
        """ returns self because it's redundant """
        return self


temperatures = [Fahrenheit(20), Fahrenheit(76), Celcius(-200), Celcius(78), Kelvin(-8), Kelvin(90223)]
for temperature in temperatures:
    print(temperature)

for i, temperature in enumerate(temperatures):
    temperatures[i] = temperature.convertToFahrenheit()

print()

for temperature in temperatures:
    print(temperature)