import random

def main():
   # Generate the number
   number = random.randint(0,99)
   # Prompt to the player
   print ("I am thinking of a number between 0 and 99...")
   guess = int(input("Enter a guess: "))
   # Game logic
   while guess != number:
        if guess > number:
            print("Your guess is too high")
        else:
            print("Your guess is too low")
        guess = int(input("Enter a guess: "))
   print (f"Congrats! The number was: {number}") 
    
if __name__ == '__main__':
    main()