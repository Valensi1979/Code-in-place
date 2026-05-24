"""Write a function that takes a list of numbers and returns the sum of those numbers."""

def add_many_numbers(numbers):
    total = 0
    for number in numbers:
        total += number
    return(total)

# There is no need to edit code beyond this point

def main():
    numbers = [1, 2, 3, 10, 5]  # Make a list of numbers
    sum_of_numbers = add_many_numbers(numbers)  # Find the sum of the list
    print(sum_of_numbers)  # Print out the sum above
    

if __name__ == '__main__':
    main()