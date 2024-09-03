class TemperatureConverter:
    def __init__(self, celsius=0.0):
        self._celsius = celsius

    # Getter for celsius
    @property
    def celsius(self):
        return self._celsius

    # Setter for celsius
    @celsius.setter
    def celsius(self, value):
        if isinstance(value, (int, float)):
            self._celsius = value
        else:
            raise ValueError("Celsius must be a number")

    # Convert Celsius to Fahrenheit
    def to_fahrenheit(self):
        return (self._celsius * 9/5) + 32

    # Convert Celsius to Kelvin
    def to_kelvin(self):
        return self._celsius + 273.15