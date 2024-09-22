from datetime import datetime
import random

def greet(bot_name, birth_year, creator_name):
    hour = datetime.now().hour
    if hour < 12:
        time_greeting = "Good morning"
    elif hour < 18:
        time_greeting = "Good afternoon"
    else:
        time_greeting = "Good evening"
    print(f'{time_greeting}! My name is {bot_name}.')
    print(f'I was created in {birth_year} by {creator_name}.')

def remind_name():
    print('Please, remind me your name.')
    name = input()
    print(f'What a great name you have, {name}!')
    remember = input('Should I remember your name for the rest of the session? (yes/no) ')
    if remember.lower() == 'yes':
        print(f'Alright, {name}, I will remember you!')
        return name
    else:
        print('No problem!')
        return None

def guess_age():
    print('Let me guess your age. I have some math tricks up my sleeve!')
    print('Enter remainders of dividing your age by 3, 5, and 7.')

    try:
        rem3 = int(input())
        rem5 = int(input())
        rem7 = int(input())
        age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

        print(f"You're {age} years old? Wow, that's a fantastic age for exploring new horizons!")
    except ValueError:
        print("Oops! Please enter valid numbers.")

def count():
    print('Now I will prove to you that I can count to any number you want.')

    try:
        num = int(input())
        curr = 0
        while curr <= num:
            print(curr, '!')
            curr = curr + 1
    except ValueError:
        print("Please enter a valid number.")

def test():
    print("Let's test your programming knowledge.")
    questions = [
        ('Why do we use methods?', 
         ['1. To repeat a statement multiple times.', 
          '2. To decompose a program into several small subroutines.', 
          '3. To determine the execution time of a program.', 
          '4. To interrupt the execution of a program.'], 2),
        ('What is the result of 3 + 2?', 
         ['1. 3', '2. 4', '3. 5', '4. 6'], 3),
        ('Which language is used for web development?', 
         ['1. Python', '2. HTML', '3. C++', '4. Java'], 2)
    ]
    
    question, answers, correct = random.choice(questions)
    print(question)
    for answer in answers:
        print(answer)
    
    possible_answer = 0
    while possible_answer != correct:
        try:
            possible_answer = int(input())
            if possible_answer != correct:
                print('Please, try again.')
        except ValueError:
            print('Please enter a valid number.')

    print('Correct!')

def end():
    print('Thank you for your time! Have a nice day!')

def interact():
    greet('Xpo', 'May 2024', 'Dennis the ChiefEngineer')
    name = remind_name()
    while True:
        choice = input("What would you like to do next? (1: Guess Age, 2: Count, 3: Test, 4: End) ")
        if choice == '1':
            guess_age()
        elif choice == '2':
            count()
        elif choice == '3':
            test()
        elif choice == '4':
            end()
            break
        else:
            print("I don't understand that option. Please try again.")

# Start the interaction
interact()
