'''ode in Place is not only massive, but also super diverse! We serve a lot of students worldwide who speak many different languages. To practice our language skills, we want to make a helpful tool to help us study Spanish!









Write a program that loops over a dictionary of words and quizzes the user for their corresponding Spanish translations, keeping count of how many the user gets correct! Separate each question and answer with a blank line to help with visual clarity.



Here's a sample run of the program (user input is in blue):

What is the Spanish translation for hello? hola
That is correct!

What is the Spanish translation for dog? gato
That is incorrect, the Spanish translation for dog is perro.

... (quizzes user on the rest of the words)
That is correct!

You got 6/8 words correct, come study again soon!'''


def main():
    translations = {
        "hello": "hola",
        "dog": "perro",
        "cat": "gato",
        "well": "bien",
        "us": "nos",
        "nothing": "nada",
        "house": "casa",
        "time": "tiempo"
    }
    
    aciertos = 0

    for key in translations:
        value = translations[key]
        answer = input ('What is the Spanish translation for ' + str(key)+'? ')
        if answer == value:
            print('That is correct!')
            aciertos += 1
        else:
            print ('That is incorrect, the Spanish translation for '+ str(key)+' is '+str(value)+'.')    

    print ('You got '+ str(aciertos) +'/'+str(len(translations))+' words correct, come study again soon!')
if __name__ == '__main__':
    main()