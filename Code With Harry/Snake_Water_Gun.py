import random
name = input("Enter your name: ")
# li = ['snake', 'water', 'gun']
li = ['s', 'w', 'g']
user_score = 0
comp_score = 0
user_choice = 'a'
comp_choice = ''
while True:
    comp = random.choice(li)
    if comp == 's':
        comp_choice = 'snake'
    elif comp == 'w':
        comp_choice = 'water'
    elif comp == 'g':
        comp_choice = 'gun'
    print("""Enter 's' for snake, 'w' for water, 'g' for gun and e for exit""")
    c = input()

    # user choice
    if c == 's':
        user_choice = 'snake'
    elif c == 'w':
        user_choice = 'water'
    elif c == 'g':
        user_choice = 'gun'
    elif c == 'e':
        user_choice = 'exit'

    if user_choice == comp_choice:
        print(f"You chose {user_choice} and computer chose {comp_choice}")
    elif user_choice == 'snake' and comp_choice == 'gun':
        print(f"You chose {user_choice} and computer chose {comp_choice}")
        comp_score += 1
    elif user_choice == 'water' and comp_choice == 'snake':
        print(f"You chose {user_choice} and computer chose {comp_choice}")
        comp_score += 1
    elif user_choice == 'gun' and comp_choice == 'water':
        print(f"You chose {user_choice} and computer chose {comp_choice}")
        comp_score += 1
    elif user_choice == 'exit':
        break
    else:
        print(f"You chose {user_choice} and computer chose {comp_choice}")
        user_score += 1
print("Your score is: ", user_score)
print("Computer's score is:", comp_score)