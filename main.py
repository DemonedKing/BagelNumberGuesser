import random

Num_Digits = 4
Max_Guess = 10
def getsecretnumber():
    numbers = list(range(10))
    random.shuffle(numbers)
    secretnum = ''
    for i in range(Num_Digits):
        secretnum += str(numbers[i])

    return secretnum

def getclues(guess, secretnum):
    if guess == secretnum:
        return "You got it!"

    clues = []
    for i in range(len(guess)):
        if guess[i] == secretnum[i]:
            clues.append("Fermi")
        elif guess[i] in secretnum:
            clues.append('Pico')

    if len(clues) == 0:
        return "Bagels"

    return " ".join(clues)

def isonlydigit(num):
    if num == '':
        return False
    for i in num:
        if i not in "0 1 2 3 4 5 6 7 8 9".split():
            return False

    return True

print(f"I am thinking of a {Num_Digits}-digit number. Try to guess what it is.")
print('The clues I give are...')
print("When I say:     That means:")
print('Bagels          None of the digits are correct')
print('Pico            One digit is correct but in the wrong position')
print('Fermi           One digit is correct and in the right position')

while True:
    secretnum = getsecretnumber()
    print(f"I have thought up a number. You have {Max_Guess} guesses to get it.")

    guessesTaken = 1
    while guessesTaken <= Max_Guess:
        guess = ""
        while len(guess) != Num_Digits or not isonlydigit(guess):
            print("Guess #%s: " % (guessesTaken))
            guess = input()

        print(getclues(guess, secretnum))
        guessesTaken += 1

        if guess == secretnum:
            break
        if guessesTaken > Max_Guess:
            print(f"You ran out of guesses. The answer was {secretnum}")

    playagain = input('Do you want to play again? (yes or no)')
    if not playagain.lower().startswith("y"):
        break





