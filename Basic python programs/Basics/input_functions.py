# getting input from a user using input() functions 
name = input("Enter your name:")
print("Hi, " + name + "!")

# adding two numbers using int() function
def addNum(num1, num2):
    total = num1 + num2
    return(total)

num1 = int(input("Please enter your first number:"))
num2 = int(input("Please enter your second number:"))

print("Your two numbers are:", num1, "and", num2)
print("The total is:", addNum(num1, num2))

