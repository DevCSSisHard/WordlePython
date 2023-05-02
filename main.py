"""
Dumb wordle game in console.
Using ANSI for color coding text.
"""

import random
ANSI_RESET = "\u001B[0m"
ANSI_GREEN = "\u001B[32m"
ANSI_YELLOW = "\u001B[33m"
ANSI_WHITE = "\u001B[37m"

debug = False

def letterCheck(word, guessList):
    correctLetters = []
    if debug:
        print('[DEBUG] word and guessList :', word, guessList)

    for i, ch in enumerate(word):
        if debug:
            print('[DEBUG] Internal values i, ch, guessList[i]:', i, ch, guessList[i])
            print('[DEBUG] i and ch: ', i, ch)

        if ch == guessList[i]:
            correctLetters.append(i)

    return correctLetters
"""
Local list of 5 letter words, formatted as just one word per line. 
"""
with open('words.txt') as f:
    wordlist = f.read().splitlines()
    print(wordlist)

pickedWord = random.choice(wordlist)
print('[DEBUG] Word selected : ' + pickedWord)

if debug:
    print('[DEBUG] Word selected : ' + pickedWord)

wordChrList = []

for letter in pickedWord:
    wordChrList.append(letter)

if debug:
    print('[DEBUG] Word character list : ', wordChrList)

playAgain = True

while playAgain:
    userGuessCount = 0
    print('You have 6 guesses to guess the 5 letter word.')
    userGuess = str(input('Enter your guess :'))
    if userGuess == 'quit':
        playAgain = False
        break

    if debug:
        print('[DEBUG] Guessed Word and length : ', userGuess, len(userGuess))
    while not len(userGuess) == 5:
        print('Must be 5 characters in length.')
        userGuess = str(input('Enter your guess :'))

    c = ANSI_RESET

    while userGuessCount < 5:
        userGuessCount = userGuessCount + 1

        if userGuess == pickedWord:
            print(f"{ANSI_GREEN}{userGuess}{ANSI_RESET}")
            break

        correctindex = letterCheck(pickedWord, userGuess)
        """
        The painful meat and logic. If its not in the correct list, its wrong no matter what
        If the letter is in the word, it may be in the right spot -
        If the index is also the correct index, then its in the right spot!
        """
        for i, letter in enumerate(userGuess):
            if i not in correctindex:
                c = ANSI_WHITE
            if letter in pickedWord:
                c = ANSI_YELLOW
            if i in correctindex:
                c = ANSI_GREEN
            # What the hell.
            print(f"{c}{letter}{ANSI_RESET}", end = "")

        userGuess = str(input('Enter your guess :'))

        if debug:
            print('[DEBUG] Guessed Word and length : ', userGuess, len(userGuess))
        while not len(userGuess) == 5:
            print('Must be 5 characters in length.')
            userGuess = str(input('Enter your guess :'))
    # Any speed testers.
    print("Playing again, enter quit to stop.")
