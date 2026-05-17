"""This program adds 2 numbers provided by the user 
Utilizes variables and some basic variable type conversion7
"""
def main():
    print ("This program adds two numbers.")
    first_number = input("Enter first number: ")
    second_number = input("Enter second number: ")
    first_number = int(first_number)
    second_number = int(second_number)
    total = first_number + second_number
    print ("The total is " + str(total) + ".")

if __name__ == '__main__':
    main()