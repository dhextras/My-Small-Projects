import random

#define a game where u guess computer number
def guess(first, second):
    random_number = random.randint(first, second)
    guess = ""
    while guess != random_number:
        print("")
        guess = int(input(f"Guess A number Between {first} and {second} : "))
        print("")

        if guess < random_number and guess >= first:
            print(f"Sorry Guessed Wrong. Try Guessing Higher Then {guess} Dude!!")
            print("")
        elif guess > random_number and guess <= second:
            print(f"Sorry Guessed Wrong. Guess Lower Then {guess} Dude!!")
            print("")
        elif guess < first or guess > second:
            print(f"Idiot {guess} Is Not Between {first} And {second}. Don't Guess Above {second} Or Below {first}")
            print("")

    print("")
    print(f"You Guessed The Number {random_number} Correctly. Congrats Dude")
    print("")
