#!/usr/bin/env python

## Read the word list
fin = open("word-list.txt")
Words = [ word.strip('\n') for word in fin.readlines() ]
fin.close()

while True:
    guess, result = input("Enter a word and result: ").split()
    if not guess in Words:
        print(guess, " is not a valid word")
    else:
        break

filteredWords = []
for idx,color in enumerate(result):
    if (color == "B"):
        filteredWords = [ word for word in Words if (word.find(guess[idx]) == -1) ]
        Words = filteredWords

print("Words now has ", len(Words), " elements")