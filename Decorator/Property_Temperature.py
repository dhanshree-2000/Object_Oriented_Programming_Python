class Temp:
    def __init__(self,celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        """Getter for the celsius property."""
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        """Setter for the celsius property."""
        if value < -273.15:
            raise ValueError("Temperature cannot be below -273.15 Celsius")
        self._celsius = value

    @celsius.deleter
    def celsius(self):
        """Deleter for the celsius property."""
        del self._celsius

    @property
    def fahrenheit(self):
        """Getter for the fahrenheit property."""
        return self._celsius * 9/5 + 32
    
temp = Temp(25)
print(temp.celsius)         # Output: 25
print(temp.fahrenheit)      # Output: 77.0

temp.celsius = 30           # Set new temperature
print(temp.fahrenheit)      # Output: 86.0

del temp.celsius            # Delete the celsius attribute
# print(temp.celsius) 