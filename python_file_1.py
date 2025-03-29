def greet_user():
    print("Here is a simple Python program that adds three numbers.")

def add_three_numbers(a, b, c):
    return a + b + c

if __name__ == "__main__":
    greet_user()
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))
    result = add_three_numbers(num1, num2, num3)
    print(f"The sum of {num1} and {num2} and {num3} is {result}.")
