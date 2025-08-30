import random

while True:
    choice = input('Roll the dice : (y/n): ').lower()  # ask every loop
    
    if choice == 'y':
        die1 = random.randint(1, 6)
        print(die1)
    elif choice == 'n':
        print("Thank you")
        break  # exit loop when user types 'n'
    else:
        print("Invalid Choice")
