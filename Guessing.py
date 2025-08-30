Number = 8

while True: 
    try:
        UserNumber = int(input("Guess the number between 1 and 100: "))
        
        if UserNumber > Number:
            print("Too High!")
        elif UserNumber < Number:
            print("Too Low!")
        else:  # UserNumber == Number
            print("Congratulations! You guessed the number.")
            break  # exit the loop when guessed correctly

    except ValueError:
        print("Invalid input! You have to enter numbers only.")
