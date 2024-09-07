class Calculator:
    def __init__(self):
        self._last_result = 0
    
    @property
    def last_result(self):
        return self._last_result

    @last_result.setter
    def last_result(self, value):
        self._last_result = value

    def add(self, x, y):
        result = x + y
        self.last_result = result
        return result

    def subtract(self, x, y):
        result = x - y
        self.last_result = result
        return result

    def multiply(self, x, y):
        result = x * y
        self.last_result = result
        return result

    def divide(self, x, y):
        if y != 0:
            result = x / y
            self.last_result = result
            return result
        else:
            return "Error! Division by zero."