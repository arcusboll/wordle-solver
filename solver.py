#!/usr/bin/env python

# Authors: Kartik Shenoy, Arcus Miranda Boll

wordList = "word-list.txt"

# FIXME: discuss with Kartik the best way to handle changing the Words list in this function. It's currently operational,
# but I think there could be a cleaner way to do this. 
def DoGuess(guess, result, Words):
    filteredWords = []
    for idx,color in enumerate(result):
        if (color == "B"):
            filteredWords = [ word for word in Words if (word.find(guess[idx]) == -1) ]
            # Words = filteredWords # can't do this because it won't change the array outside of the function.
                                    # this is because Words is passed by reference, but the *reference* is passed by *value*
                                    # So to change Words outside of the function, need to call mutable functions on Words
            Words.clear()
            for word in filteredWords:
                Words.append(word)

    print("Words now has ", len(Words), " elements")
    return

# Read in the word list.
# The with statement automatically closes the file after the block 
with open(wordList) as file:
    Words = [ word.strip('\n') for word in file.readlines() ]

# TODO: make pretty instructions
print("Welcome to the Wordle solver!\n\n")

while True:
    guess, result = input("Enter a word and result: ").split()
    if not guess in Words:
        print(guess, " is not a valid word")
    else:
        DoGuess(guess, result, Words)
        break

#print("Words now has ", len(Words), " elements")
#print(Words)
