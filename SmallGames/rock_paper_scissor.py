import random

# define a rock paper scissor game
class Rps:
    def start(self):
        while True:
            print("Press '0' to Go Main Menu")
            print("")
            #computer choosing
            rps = ["r", "p", "s"]
            computer = random.choice(rps)

            print("In This Game 'r > s , s > p , p > r'")
            print("")

            #player choosing
            player = input("So Which One You Wanna Choose ?? (R) For Rock, (P) For Paper, (S) For Scissor ?? ").lower()
            print("")

            if player == '0':
                break
            else:
                print(f"You Choosed '{player}' And The Computer Choosed '{computer}'.")
                print("")
                
                # r > s , s > p , p > r
                if (player == "r" and computer == "s") or (player == "s" and computer == "p") or (player == "p" and computer == "r"):
                    print("So You Won Dude!!")
                    print("")

                elif (player == "r" and computer == "r") or (player == "s" and computer == "s") or (player == "p" and computer == "p"):
                    print("Oops It's A Tie!!")
                    print("")
                    
                elif (player == "s" and computer == "r") or (player == "p" and computer == "s") or (player == "r" and computer == "p"):
                    print("Ahh You Loose!!")
                    print("")

                else:
                    print("You Choosed Wrong. Only Choose (R) For Rock, (P) For Paper, (S) For Scissor ??")
                    print("")
