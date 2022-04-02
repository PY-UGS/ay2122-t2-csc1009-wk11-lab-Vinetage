class Calculator:
    # Constructor
    def __init__(self):
        self.input1 = 0.0
        self.input2 = 0.0
    # Adding function
    def adder(self):
        return self.input1 + self.input2
    # Subtracting function
    def subtractor(self):
        return self.input1 - self.input2
    # Multiplication function
    def multiplier(self):
        return self.input1 * self.input2
    # Division Function
    def divider(self):
        return self.input1 / self.input2
    # Clear Function
    def clear(self):
        self.input1 = 0.0
        self.input2 = 0.0

# Main
if __name__ == "__main__":
    print("Welcome to lab 11 calculator python...")
    # Create calculator object
    calculator = Calculator()
    # Ask user for input 1
    calculator.input1 = float(input("Please input a number: "))
    # Ask user for input 2
    calculator.input2 = float(input("Please input a second number: "))
    # Do all class methods
    print(calculator.input1," + ",calculator.input2," = ",calculator.adder())
    print(calculator.input1," - ",calculator.input2," = ",calculator.subtractor())
    print(calculator.input1," * ",calculator.input2," = ",calculator.multiplier())
    print(calculator.input1," / ",calculator.input2," = ",calculator.divider())
    print("The values input 1 and 2 will be reset..")
    calculator.clear()
    print("Input 1 = ",calculator.input1)
    print("Input 2 = ",calculator.input2)

