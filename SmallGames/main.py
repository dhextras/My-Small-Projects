import you_guess
import comp_guess
import rock_paper_scissor
            
#Choose The Game
print("Which One You Wanna Play??")
print("           1. For You Guess Computer's Number")
print("           2. For Computer Guess Yours")
print("           3. For Rock Paper Scissor Game")
print("")

game = int(input("Choose?? "))
print("")

while game < 5:
    if game == 1:
        #Choose The Range
        print("Input 2 Numbers Below Which Is Going To Be The Range For Random Number")
        print("")

        first_no = int(input("Enter The 1 st Number : "))
        second_no = int(input("Enter The 2 nd Number : "))
        print("")

        if first_no < second_no:
            guessing = you_guess.guess(first_no, second_no)
            print(guessing)
        elif first_no > second_no:
            guessing = you_guess.guess(second_no, first_no)
            print(guessing)

    elif game == 2:
        #Choose The Range
        print("Input 2 Numbers Below Which Is Going To Be The Range For Random Number")
        print("")

        first_no = int(input("Enter The 1 st Number : "))
        second_no = int(input("Enter The 2 nd Number : "))
        print("")

        if first_no == second_no:
            print(f"The Number Is {first_no}")#it can also be no_for_b bcs both same
            print("")

        else:
            if first_no < second_no:
                comp_guessing = comp_guess.computer_guess(first_no, second_no)
                print(comp_guessing)
            else:
                comp_guessing = comp_guess.computer_guess(second_no, first_no)
                print(comp_guessing)

    elif game == 3:
        rps = rock_paper_scissor.Rps()
        rps.start()

    elif game == 4:
        exit ()

    else:
        print("Choose The Right Game Bakayaro!!")

    if game < 4:
        print("Do You Wanna Play Again??")
        print("           1. For You Guess Computer's Number")
        print("           2. For Computer Guess Yours")
        print("           3. For Rock Paper Scissor Game")
        print("           4. If You Wanna Quit")
        print("")
        game = int(input("Choose?? "))
        print("")
