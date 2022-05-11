# Wordle game. 
#    (See https://en.wikipedia.org/wiki/Wordlehttps://en.wikipedia.org/wiki/Wordle)
# Program 6, UIC CS 111 Spring 2022, in Python using Replit.
"""
Sample run:
    Enter filename, or press enter to accept default: 
    Setting default filename.
    There are 533 words in short.txt
    Secret word is: fakes
    
    1. Guess: fetid
              F^...    abc   gh jklmnopqrs uvwxyz
    2. Guess: freak
              F.^^^     bc   gh j lmnopq s uvwxyz
    3. Guess: feats
              F^^.S     bc   gh j lmnopq   uvwxyz
    4. Guess: fakes
              FAKES     bc   gh j lmnopq   uvwxyz
    Congratulations, you got it!
"""

import random
random.seed(1)

print("""Welcome to Wordle!

In each of the setup options you can press enter to accept the defaults.
The defaults are:
    - Use 'secretWords.txt' to choose a secret word to be guessed
    - Use 'guessWords.txt' to validate guesses are real words
    - Program selects secret word""")
#Getting secret word from File(from which 5 letter words would be taken randomly)
secretfile = input("Enter filename for selecting a secret word (or just enter): ")
#If enter is pressed setting default
if len(secretfile) == 0:
    secretfile = "secretWords.txt"
secretlist = []
with open(secretfile,'r') as file:
    for line in file:
        secretlist.append(line.strip())
print("There are "+str(len(secretlist))+" words in "+secretfile)
#Getting list of guess words
#Now from the chosen file we extract all words into a list
guessfile = input("Enter filename for words used in guessing (or just enter): ")
#If enter is pressed setting default
if len(guessfile) == 0:
    guessfile = "guessWords.txt"
guesslist = []
with open(guessfile,'r') as file:
    for line in file:
        guesslist.append(line.strip())
print("There are "+str(len(guesslist))+" words in "+guessfile)

secretword = input("Press enter for secret word to be chosen, or type in a word: ")
#4. Now we select a random word from the list and set it to secret word or take user input
if secretword== "":
    secretword = random.choice(secretlist)
print(secretword)


#5. we will start a for loop here(range(6))
    #6. Randomly select one word from the reduced list and check it
    #7. If word matches secret word we are done
    #8. Else Implement the idea above(in the form of a function) to update the word list based on the output

print("For any move you can also enter s to display secret word, or x to exit.")

flag = True
count = 1   #for counting rounds
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
occured = []    #we will be storing occured alphabets
exit = False
while(flag and count <7):
    word = input(str(count)+". Guess: ")
    if word == 'x':
        print('Exiting')    #if x exit game
        exit = True
        break
    if word == 's':
        print("  Secret: "+secretword)   #if s show the word
        continue
    if(word not in guesslist):
        print("                 Not a valid word.  Retry.") #user input not valid
        continue
    msg = "          "
    for i in range(5):
        if word[i] in secretword:
            if word[i] == secretword[i]:
                msg += word[i].upper()  #word[i] and secretword[i] matching 
            else:
                msg += '^'  #word[i] in secretword and not at position i
        else:
            msg += '.'
        occured.append(word[i]) #update occuredlist
    msg += "    "
    #printing allowed alphabets
    for i in range(26):
        if alpha[i] in occured:
            msg += ' '
        else:
            msg += alpha[i]
    print(msg)
    #checking if guessed word correct
    if secretword == word:
        print("Congratulations, you got it!")
        flag = False
    count += 1
if flag and not exit:
    print("Secret word was:  "+secretword)
print("Done")