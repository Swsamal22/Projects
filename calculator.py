class calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def Sum(self):
        return self.a+self.b
    
    def Sub(self):
        return self.a-self.b

    def Mul(self):
        return self.a*self.b
    
    def Div(self):
        return self.a/self.b

    def Power(self):
        return self.a**self.b


print("Welcome to the Calculator !")
#highlighting the format for operation as for substraction and division the first number neeeds to be greater than the second number
print("Enter the number where A is greater than B")
num1 = float(input("Enter the first number: "))
op = input("Enter the operator: ")
num2 = float(input("Enter the second number: "))

c=calculator(num1,num2)

#choosing the operation
if op == "+":
    print("The result is: {0:.4f}".format(c.Sum()))
elif op == "-":
    print("The result is: {0:.4f}".format(c.Sub()))
elif op == "*":
    print("The result is: {0:.4f}".format(c.Mul()))
elif op == "/":
    print("The result is: {0:.4f}".format(c.Div()))
elif op == "^":
    print("The result is: {0:.4f}".format(c.Power()))
else:
    print("Invalid operator")

