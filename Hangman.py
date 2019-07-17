import random
#list of words
ans = ["encourage", "ruthless", "gleaming", "balance", "endurable", "ring", "grateful", "quiver", "spoil", "scintillating", "bucket", "stupendous", "borrow", "border", "force", "geese", "lackadaisical", "art", "cruel", "cagey",
"replace", "idea", "superb", "lumpy", "fanatical", "roll", "birthday", "grandmother", "pull", "check", "absurd", "willing", "wipe", "sail", "uptight", "price", "rake", "mom", "fertile", "load", "embarrassed", "lyrical", "worm", "erect", "present", "numerous", "addicted", "watery", "warm", "jump"]
#Selects a random word from list(ans)
ans = random.choice(ans)
#makes a list of each letter in the word selected
ans = list(ans)
#player has 10 lives
lives = 10
#sets up correctGuess variable to declare if user guessed correctly or not
correctGuess = False
#create list for storing guesses
alreadyGuessed = []
correct = []
play = True
def hasGuessed(x, y):
    hasMatched = False
    value = False
    if (len(y) != 0):
        for a in range(len(y)):
            if (x == y[a]):
                hasMatched = True
                if (hasMatched):
                    value = False
            else:
                if (hasMatched):
                    value = False
                else:
                    value = True
    else:
        value = True
    return(value)
def isCorrect(x, y):
    if x == y:
        return True
    else:
        return False

def winner(x,y):
    count = 0
    for z in range(len(ans)):
        if (x[z] == y[z]):
            count += 1
            if (count == len(x)):
                return(True)
        else:
            return(False)
def reset():
    global ans, lives, correctGuess, alreadyGuessed, correct
    ans = ["encourage", "ruthless", "gleaming", "balance", "endurable", "ring", "grateful", "quiver", "spoil", "scintillating", "bucket", "stupendous", "borrow", "border", "force", "geese", "lackadaisical", "art", "cruel", "cagey",
    "replace", "idea", "superb", "lumpy", "fanatical", "roll", "birthday", "grandmother", "pull", "check", "absurd", "willing", "wipe", "sail", "uptight", "price", "rake", "mom", "fertile", "load", "embarrassed", "lyrical", "worm", "erect", "present", "numerous", "addicted", "watery", "warm", "jump"]
    ans = random.choice(ans)
    ans = list(ans)
    lives = 10
    correctGuess = []
    alreadyGuessed = []
    correct.clear()
    play = True
    for x in range(len(ans)):
        correct.append('_ ')
for x in range(len(ans)):
    correct.append('_ ')
while play:
    print(' '.join(correct))
    if (lives > 1):
        inpt = input("Guess a letter: ").lower()
    else:
        inpt = input("Last chance: ").lower()
    if (len(inpt) == 1):
        if (hasGuessed(inpt, alreadyGuessed)):
            alreadyGuessed.append(inpt)
            for y in range(len(ans)):
                if (isCorrect(inpt, ans[y].lower())):
                    correct[y] = ans[y]
                    correctGuess = True
                if (y == len(ans)-1):
                    if (isCorrect(inpt, ans[y].lower())):
                        correct[y] = ans[y]
                        correctGuess = True
                    if(correctGuess):
                        print("Correct!")
                        print("You have guessed: %s" %(', '.join(alreadyGuessed)))
                        if (winner(ans, correct)):
                            print("YOU WIN!!! The word was %s" %(''.join(ans)))
                            print("Do you want to play again (Yes or No)?")
                            inpt = input().lower()
                            while play:
                                if inpt == 'yes':
                                    reset()
                                    break
                                elif inpt == 'no':
                                    play = False
                                else:
                                    inpt = input("Please enter yes or no: ")
                        else:
                            correctGuess = False
                    else:
                        lives -= 1
                        if lives == 1:
                            print("Incorrect")
                            print("You have guessed: %s" %(', '.join(alreadyGuessed)))
                        elif lives == 0:
                            print("Sorry, you lose. The word was %s." %(''.join(ans)))
                            print("Do you want to play again (Yes or No)?")
                            inpt = input().lower()
                            while play:
                                if inpt == 'yes':
                                    reset()
                                    break
                                elif inpt == 'no':
                                    play = False
                                else:
                                    inpt = input("Please enter yes or no: ")
                        else:
                            print("Incorrect")
                            print("You have guessed: %s" %(', '.join(alreadyGuessed)))
        else:
            print("You've already guessed that. Try again.")
            print("You have guessed: %s" %(', '.join(alreadyGuessed)))
    else:
        print("Please enter one letter per guess.")
