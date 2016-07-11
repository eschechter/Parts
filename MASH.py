from random import *
from Myro import *


spouses = []
for i in range(0,2):
    speak("Name someone you want to marry.", 0)
    spouses.append(raw_input("Name someone you want to marry. \n"))

for i in range(0,2):
    speak("Name someone you wouldn't want to marry.", 0)
    spouses.append(raw_input("Name someone you wouldn't want to marry. \n"))

spouse = spouses[randint(0,2)]



pets = []
for i in range(0,2):
    speak("Name a pet you want to have.", 0)
    pets.append(raw_input("Name a pet you want to have. \n"))

for i in range(0,2):
    speak("Name a pet you wouldn't want to have.", 0)
    pets.append(raw_input("Name a pet you wouldn't want to have. \n"))

pet = pets[randint(0,2)]



speak("You will marry " + spouse + ". You will own a " + pet + ".", 0)