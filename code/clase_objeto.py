#Jorge Ortega Badilla
#Class: Python
#Topic: Method (A method is like a funtion)

class Calculator:
    def __init__(self, n1, n2):
        self.addition = n1 + n2
        self.subtraction = n1 - n2
        self.multiplication = n1 * n2
        self.division = n1 / n2

operation = Calculator(2, 3)
print("El resultado es:", operation.multiplication)

