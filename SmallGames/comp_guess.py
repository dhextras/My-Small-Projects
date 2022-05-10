import random

# define a game where computer guess ur number
def computer_guess(first, second):
    feedback = ""

    while feedback != "c":
        guess = random.randint(first, second)
        feedback = str(input(f"I Think Its {guess}. If Its High (H) and If Low (L) Or If Correct (C) Tell Me??  ").lower())
        print("")

        if feedback == "h":
            second = guess - 1

        elif feedback == "l":
            first = guess + 1

        else:
            if feedback == "c":
                print(f"The Correct Answer Is {guess}. I Guessed It Perfectly")
                print("")

            else:    
                print("Your FeedBack Is Wrong. Give FeedBack Correctly!!")
                print("")