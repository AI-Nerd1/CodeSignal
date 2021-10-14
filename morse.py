#!/usr/bin/env python3
import time
from playsound import playsound

mp3File = "/home/logan/VS Code Projects/Python/others/single beep.mp3"

playsound(mp3File)


for x in range(2):
    playsound(mp3File)
    
from playsound import playsound
import time
single_beep = "/home/logan/VS Code Projects/Python/others/single_beep2.mp3"
double_beep = "/home/logan/VS Code Projects/Python/others/double_beep2.mp3"

def dit():
    playsound(single_beep)

def dah():
    playsound(double_beep)

morse_code = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.", 
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    " ": " ",
}
def sound():
    if letter == "A": 
        dit()
        dah()
    elif letter == "B":
        dah()
        dit()
        dit()
        dit()
    elif letter == "C":
        dah()
        dit()
        dah()
        dit()
    elif letter == "D":
        dah()
        dit()
        dit()
    elif letter == "E":
        dit()
    elif letter == "F":
        dit()
        dit()
        dah()
        dit()
    elif letter == "G":
        dah()
        dah()
        dit()
    elif letter == "H":
        dit()
        dit()
        dit()
        dit()
    elif letter == "I":
        dit()
        dit()
    elif letter == "J":
        dit()
        dah()
        dah()
        dah()
    elif letter == "K":
        dah()
        dit()
        dah()
    elif letter == "L":
        dit()
        dah()
        dit()
        dit()
    elif letter == "M":
        dah()
        dah()
    elif letter == "N":
        dah()
        dit()
    elif letter == "O":
        dah()
        dah()
        dah()
    elif letter == "P":
        dit()
        dah()
        dah()
        dit()
    elif letter == "Q":
        dah()
        dah()
        dit()
        dah()
    elif letter == "R":
        dit()
        dah()
        dit()
    elif letter == "S":
        dit()
        dit()
        dit()
    elif letter == "T":
        dah()
    elif letter == "U":
        dit()
        dit()
        dah()
    elif letter == "V":
        dit()
        dit()
        dit()
        dah()
    elif letter == "W":
        dit()
        dah()
        dah()
    elif letter == "X":
        dah()
        dit()
        dit()
        dah()
    elif letter == "Y":
        dah()
        dit()
        dah()
        dah()
    elif letter == "Z":
        dah()
        dah()
        dit()
        dit()

         
 
     
    
out = []
word = input('Statement: ')
word = word.upper()
for letter in word:
    out.append(morse_code[letter])
    sound()
    out.append("|")
    time.sleep(0.2)
out = "".join(out)
print(f"Morse Encryption : {out}")





