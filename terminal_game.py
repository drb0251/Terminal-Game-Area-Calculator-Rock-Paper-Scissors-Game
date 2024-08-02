import time
import random
import math

# basic terminal game in python, day in the life of a computer sciene nerd :)

print('Welcome to your first day of Computer Science!\n')
time.sleep(2)
print('You arrive to the entrance of the university, and find a map:\n')
time.sleep(2)
print("##### Map of the Campus #####\n# A-block: Arts             #\n# E-block: Engineering      #\n# C-block: Computer Science #\n# P-block: Politics         #\n ###########################\n")
time.sleep(3)
print("Where would you like to go?\n1) A-block\n2) E-block\n3) C-block\n4) P-block\n")

# map choice segment
map_choice = ''
while map_choice != '3':
    map_choice = input("Enter the number of the location you wish to travel to: ")
    if map_choice == '1':
        print("Idiot! You're not an arts student lol. Try again.\n")
        time.sleep(2)
    elif map_choice == '2':
        print("Lol, you ain't building no bridge loser. Try again.\n")
        time.sleep(2)
    elif map_choice == '4': 
        print("Ew you definitely don't wanna get into that! Try again.\n")
        time.sleep(2)
    elif map_choice == '3':
        print("Nice one you found where you need to go!\n")
        time.sleep(2)
        map_choice = '3'
    else:
        print("Fine don't go to class then, your money not mine.\n")

# using time delay for 'making my way to the class'
print('You begin walking to class: ')
time.sleep(2)
print('Almost there...')
time.sleep(2)
print('Doo doo do doo\n')
time.sleep(2)

print('You arrive to class!\n')
time.sleep(2)
print('Tutor: "Hey pleb you are late, you need to build a Paper Scissors Rock game, if you do not finish in 15 minutes, you fail the course!"\n')
time.sleep(5)
print('You: "O_O okay this should take me around 5 seconds..."\n')
time.sleep(5)
print('5 seconds later...\n')
time.sleep(1)
print('You: "Okay finished, now I need to test the damn thing..."\n')

# Rock paper scissors game :)
play_again = 'y'
while play_again != 'n':
    print('Loading game...\n')
    time.sleep(3)
    print('Welcome to the game of Rock Paper Scissors!')
    time.sleep(1)
    choice = input('Choose your weapon: \n1) Rock\n2) Paper\n3) Scissors\nEnter selection here: ').lower().strip()
    player = ''
    if choice == 'rock' or choice == '1':
        player = 'rock'
    elif choice == 'paper' or choice == '2':
        player = 'paper'
    elif choice == 'scissors' or choice == '3':
        player = 'scissors'
    else:
        print('invalid input, try again.')
    time.sleep(2)
    print(f"Hmmm, you chose {player}.\n")
    time.sleep(3)

    ran_num = random.randint(1,3)
    if ran_num == 1:
        npc = 'rock'
    elif ran_num == 2:
        npc = 'paper'
    elif ran_num == 3:
        npc = 'scissors'
    else:
        print('error')
    print(f'Your opponent has chosen {npc}\n')
    time.sleep(3)

    # game logic
    result = ''
    if npc == player:
        result = 'draw'
    elif (npc == 'scissors' and player == 'rock') or \
        (npc == 'rock' and player == 'paper') or \
        (npc == 'paper' and player == 'scissors'):
        result = 'win'
    else:
        result = 'lose'
    
    if result == 'win':
        print(f'Congratulations! you {result}.\n')
    elif result == 'lose':
        print(f"Sorry, you {result}. lol.\n")
    else:
        print(f"It's a {result}!\n")
    time.sleep(2)
    play_again = input('Would you like to play again? (y/n) \n')
    time.sleep(2)

print('Your tutor sees your game works properly...\n')
time.sleep(3)
print('Tutor: "hmm looks nice buddy!"\n')
time.sleep(3)
print('Tutor: "Guess what?"\n')
time.sleep(3)
print('You wait, staring, then ask "What?"\n')
time.sleep(3)
print('Tutor: "Okay now build an area calculator BIG SHOT!"\n')
time.sleep(3)
print('You begin coding again. Another 5 seconds pass...\n')
time.sleep(5)
print('5 seconds later...\n')
print('You: "DONE! Now I gotta test this too!"\n')
time.sleep(3)
print('Loading game...\n')
time.sleep(3)

print('Welcome to the area calculator!\n')
play_game = 'y'
while play_game != 'n':
    shape_desired = input('Please choose a shape:\n1) Circle\n2) Triangle\n3) Square\nChoose number: \n').lower().strip()
    if shape_desired == 'circle' or shape_desired == '1':
        radius = float(input('Please enter the radius (cm) of the cirle here: \n'))
        circle_area = math.pi * (radius ** 2)
        print('Calculating area of the circle...\n')
        time.sleep(2)
        print(f'The area of the circle is {circle_area}cm squared.\n') 
        play_game = input('Would you like to calculate something else? (y/n): \n') 

    elif shape_desired == 'triangle' or shape_desired == '2':
        base = float(input('Enter the base (cm) of the tringle: \n'))
        height = float(input('Enter the height (cm) of the triangle: \n'))
        triangle_area = 0.5 * (base * height)
        print('Calculating area of the triangle...\n')
        time.sleep(2)
        print(f'The area of the triangle is {triangle_area}cm squared.\n')
        play_game = input('Would you like to calculate something else? (y/n): \n')

    elif shape_desired == 'square' or shape_desired == '3':
        side_a = float(input('Enter the length of the first side (cm) of the square: \n'))
        side_b = float(input('Enter the length of the second side (cm) of the square: \n'))
        sqaure_area = side_a * side_b
        print('Calculating area of the square...\n')
        time.sleep(2)
        print(f'The are of the square is {sqaure_area}cm squared.\n')
        play_game = input('Would you like to calculate something else? (y/n): \n') 
    
    else:
        print('error')
        play_game = input('Would you like to calculate something else? (y/n): \n')

print('A minute has now passed. Class is over.\n')
time.sleep(3)
print('Tutor: "Hey you actually did some good work today, you want a job interview?"\n')
time.sleep(3)
print('You: "Of course I do yaaayyyyy"\n')
time.sleep(3)
print('You have completed your first day at university. Congratulations!!!\n')
print('############# The end #############')
