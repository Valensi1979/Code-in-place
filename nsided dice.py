"""Write a program which takes as input the number of sides on a dice.  Then, simulate rolling a dice with that many sides. Print the outcome of the roll. When you're done, click on the "Check Correct" button.



Here is the terminal output for an example run of the program (user input in blue):

How many sides does your dice have? 10  
Your roll is 8"""

import random

def main():
    num_sides = int(input("How many sides does your dice have? "))
    rand_num = str(random.randint(1, num_sides))
    print (f"Your roll is {rand_num}") 
if __name__ == '__main__':
    main()