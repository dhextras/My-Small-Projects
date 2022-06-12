import you_guess
import comp_guess
import rock_paper_scissor
import mine_sweeper
            
#Choose The Game
print("""Which One You Wanna Play??
           1. For You Guess Computer's Number
           2. For Computer Guess Yours
           3. For Rock Paper Scissor Game
           4. For Mine Sweeper Game
""")

game = int(input("Choose?? "))
print("")

while game < 6:
    main_menu = True
    if game == 1:
        while main_menu == True:
            #Choose The Range
            print("Input 2 Numbers Below Which Is Going To Be The Range For Random Number{Only Input '0' If You wanna Go Main Menu}")
            print("""
* Press '0' To Go To Main Menu
""")

            first_no = int(input("Enter The 1 st Number : "))
            second_no = int(input("Enter The 2 nd Number : "))
            print("")

            if first_no == 0 or second_no == 0:
                main_menu = False
            else:
                if first_no < second_no:
                    guessing = you_guess.guess(first_no, second_no)
                    print(guessing)
                elif first_no > second_no:
                    guessing = you_guess.guess(second_no, first_no)
                    print(guessing)

    elif game == 2:
        while main_menu == True:
            #Choose The Range
            print("Input 2 Numbers Below Which Is Going To Be The Range For Random Number{Only Input '0' If You wanna Go Main Menu}")
            print("""
* Press '0' To Go To Main Menu
""")

            first_no = int(input("Enter The 1 st Number : "))
            second_no = int(input("Enter The 2 nd Number : "))
            print("")

            if first_no == 0 or second_no == 0:
                    main_menu = False
            else:
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
        ms = mine_sweeper.start()
        print(ms)

    elif game == 5:
        exit()

    else:
        print("Choose The Right Game Bakayaro!!")

    if game < 5:
        print("""Do You Wanna Play Again??
           1. For You Guess Computer's Number
           2. For Computer Guess Yours
           3. For Rock Paper Scissor Game
           4. For Mine Sweeper Game
           5. If You Wanna Quit
""")
        game = int(input("Choose?? "))
        print("")
