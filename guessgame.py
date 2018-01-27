#This is the most fantastic game to play
import random

print("--------Wellcome to the guess game--------------")
print("................................................")
print()
print()


#__name__=="__guessgame__"

def guessgame():
    #print("Are You Want to Play(y/n)")
    #choice = input()

    if playAgain=="yes" or playAgain == "y" :

        print("What is your name?")

        myName = input()
        print("Hello"+myName+" ,I am thinking a number between 1 to 100")
        number=random.randint(1,10)

        count = 0
        while True:
            print("Guess The Number: ")
            guessNumber = input()
            guessNumber = int(guessNumber)
            count =count+1

            if guessNumber > number:
                print("You guessed too high")
                print()
            if guessNumber < number:
                print("You Guessed Too low")
                print()
            if guessNumber == number:
                count = str(count)
                print("Good job" + myName + ",You guessed my Number in " + count + " guessed!")
                print()
                break

playAgain="yes"
while playAgain == "yes" or playAgain=="y":
    guessgame()
    print("Are You want to play again?(yes/no)")
    playAgain=input()
