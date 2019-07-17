import random
#list of words
ans = ["encourage", "ruthless", "gleaming", "balance", "endurable", "ring", "grateful", "quiver", "spoil", "scintillating", "bucket", "stupendous", "borrow", "border", "force", "geese", "lackadaisical", "art", "cruel", "cagey",
"replace", "idea", "superb", "lumpy", "fanatical", "roll", "birthday", "grandmother", "pull", "check", "absurd", "willing", "wipe", "sail", "uptight", "price", "rake", "mom", "fertile", "load", "embarrassed", "lyrical", "worm", "erect", "present", "numerous", "addicted", "watery", "warm", "jump"]
ans = random.choice(ans) #Selects a random word from list(ans)
ans = list(ans) #makes a list of each letter in the word selected
lives = 10 #player has 10 lives
correctGuess = False #sets up correctGuess variable to declare if user guessed correctly or not
alreadyGuessed = [] #create list for storing guesses
correct = [] #create list for storing correct guesses
play = True #keeps the game going if the player wishes to continue
def hasGuessed(x, y): #function that checks if the player enter a letter that they've already guessed
#x = user input and y = alreadyGuessed
    hasMatched = False #sets the hasMatched to false
    value = False #sets the value to be returned
    if (len(y) != 0): #Checks if guess is first guess
        for a in range(len(y)): #loops through all of the items in alreadyGuessed
            if (x == y[a]): #if user input equals item in already alreadyGuessed
                hasMatched = True #sets hasMatched to True
                if (hasMatched): #Checks if hasMatched is true before changing the return value
                    value = False #sets return value to False
            else: #if user input does not equal item in already alreadyGuessed
                if (hasMatched): #catch to determine if one of the previous items came up as a match
                    continue #skips the else statement if a matched was previously found
                else: #if previous match not found, then last letter is not a match either
                    value = True #set Return value to True
    else: #if first guess
        value = True #set return value to true
    return(value) #return value
def isCorrect(x, y): #simple function to check if the user guessed correctly
#x = user input y = ans[y].lower()
    if x == y: #if user input is equal to ans[y].lower()
        return True
    else: #if user input does not match
        return False

def winner(x,y): #function to determine if the player won
#x = ans y = correct
    count = 0 #sets the number of correct guesses
    for z in range(len(ans)): #iterate through the values of ans
        if (x[z] == y[z]): #if ans[z] = correct[z]
            count += 1 #add 1 to count for correct guesses
            if (count == len(x)): #if count is equal to the number of letters
                return(True)
        else: #if count is not equal to the number of letters
            return(False)
def reset(): #function to reset all variables
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
    for x in range(len(ans)): #for each value in ans
        correct.append('_ ') #add _ to correct
for x in range(len(ans)): #for each value in ans
    correct.append('_ ') #add _ to correct
while play: #Loops the game while play is true
    print(' '.join(correct)) #dispays underscores for each letter in ans
    if (lives > 1): #if lives is greater than 1
        inpt = input("Guess a letter: ").lower() #tell user to guess a letter and assign user input to inpt
    else: #if lives is equal to 1
        inpt = input("Last chance: ").lower() #tell the user that this is their last guess
    if (len(inpt) == 1): #checks if user entered at least and not more than one value
        if (hasGuessed(inpt, alreadyGuessed)): #calls hasGuessed function, line 12
            alreadyGuessed.append(inpt) #adds the user input to alreadyGuessed list
            for y in range(len(ans)): #iterate through ans
                if (isCorrect(inpt, ans[y].lower())): #call isCorrect function on line #30
                    correct[y] = ans[y] #assigns the value of ans[y] to correct[y]
                    correctGuess = True #user guessed correctly
                if (y == len(ans)-1): #if on last index of ans
                    if (isCorrect(inpt, ans[y].lower())): #calls isCorrect function on line #30
                        correct[y] = ans[y] #assigns ans[y] to correct[y]
                        correctGuess = True #user guessed correctly
                    if(correctGuess): #if the user guessed correctly
                        print("Correct!") #display Correct!
                        print("You have guessed: %s" %(', '.join(alreadyGuessed))) #display the letters guessed already
                        if (winner(ans, correct)): #calls winner function line #37
                            print("YOU WIN!!! The word was %s" %(''.join(ans))) #displays to the user that the one and tells them the answer
                            print("Do you want to play again (Yes or No)?") #asks user if they want to play again
                            inpt = input().lower() #Takes user input and makes it all lower case
                            while play: #play continues to be true
                                if inpt == 'yes': #if user wants to play again
                                    reset() #call reset function line #47
                                    break #break from while loop
                                elif inpt == 'no': #if user doesn't want to play again
                                    play = False #set play to false, exiting all while loops
                                else: #catch if user enters something other than yes or no
                                    inpt = input("Please enter yes or no: ") #tells user to enter yes or no
                        else: #if user hasn't won
                            correctGuess = False #user guessed incorrectly
                    else: #if user guessed incorrectly
                        lives -= 1 #lose one life
                        if lives >= 1: #if the player has at least 1 life
                            print("Incorrect") #tell the user they guessed incorrectly
                            print("You have guessed: %s" %(', '.join(alreadyGuessed))) #display the letters they've guessed
                        else: #if lives = 0
                            print("Sorry, you lose. The word was %s." %(''.join(ans))) #tell the player they lose and tell them the answer
                            print("Do you want to play again (Yes or No)?") #asks the user if they want to play again
                            inpt = input().lower() #assigns user input to inpt in lower case
                            while play: #play continues to be true
                                if inpt == 'yes': #if user wants to play again
                                    reset() #call reset function line #47
                                    break #break from while loop
                                elif inpt == 'no': #if user doesn't want to play
                                    play = False #set play to false, exiting all while loops
                                else: #if user enters something other than yes or no
                                    inpt = input("Please enter yes or no: ") #tell user to enter yes or no
        else: #if inpt = a value in already guessed
            print("You've already guessed that. Try again.") #tell the user they already guess that
            print("You have guessed: %s" %(', '.join(alreadyGuessed))) #display the guessed letters
    else: #if user enters more or less than one chracter
        print("Please enter one letter per guess.") #tells the user to enter one letter
