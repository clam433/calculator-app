class RPNCalculator:
    def __init__(self):
        self.stack = []
    
    def push(self, value):
        self.stack.append(value)
    
    def add(self):
        if len(self.stack) < 2:
            raise ValueError("Not enough operands")
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a + b)
    
    def subtract(self):
        if len(self.stack) < 2:
            raise ValueError("Not enough operands")
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a - b)
    
    def multiply(self):
        if len(self.stack) < 2:
            raise ValueError("Not enough operands")
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a * b)
    
    def divide(self):
        if len(self.stack) < 2:
            raise ValueError("Not enough operands")
        b = self.stack.pop()
        a = self.stack.pop()
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        self.stack.append(a / b)
    
    def evaluate(self):
        if len(self.stack) == 1:
            return self.stack[-1]
        elif len(self.stack) > 1:
            raise ValueError("Too many operands remaining in the stack.")
        return None

# User input loop
calculator = RPNCalculator()
print("Reverse Polish Notation Calculator. Enter numbers and operators ('+', '-', '*', '/') one by one. Type '=' to evaluate and 'q' to quit.")

while True:
    try:
        user_input = input("Enter token: ").strip()
        if user_input.lower() == 'q':
            print("Exiting calculator.")
            break
        elif user_input.replace('.', '', 1).isdigit():  # Support for floating-point numbers
            calculator.push(float(user_input))
        elif user_input in ['+', '-', 'x', '/']:
            if user_input == '+':
                calculator.add()
            elif user_input == '-':
                calculator.subtract()
            elif user_input == '*':
                calculator.multiply()
            elif user_input == '/':
                calculator.divide()
        elif user_input.lower() == '=':
            result = calculator.evaluate()
            if result is not None:
                print("Result:", result)
            else:
                print("No result available.")
            calculator.stack.clear()  # Clear stack for the next calculation
        else:
            print("Invalid input. Please enter numbers or operators (+, -, x, /), 'enter', or 'q'.")
    except Exception as e:
        print("Error:", e)