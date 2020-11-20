# Importing the os library
import os
import re

print(fullitems := [filename for filename in os.listdir(".")])

print(particularitems := [
    filename for filename in os.listdir(".")
    if (filename.endswith(".png")) or (filename.endswith(".jpg"))
])

spacecount = 0
string = input("Enter the string :")
for i in range(0, len(string)):
    if string[i] == " ":
        spacecount += 1

print(f"spacecount in the string:{spacecount}")

print(novowels := re.sub("[aeiouAEIOU]", "", input("Enter the sentence:")))

print(
    strval := [s for s in input("Enter the sentence:").split() if 4 > len(s)])

print(strlen := [len(s) for s in input("Enter the sentence:").split()])
