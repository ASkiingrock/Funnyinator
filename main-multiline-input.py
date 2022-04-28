import json
import random
import main_func as main_func
# import traceback # debugging


output = "" # basically the way this works is it goes through every word in the text, adds it to the output if it doesn't need to be changed, swaps it if it does
with open("Funnyinator/alternateInput.txt", "r") as f:
    i = f.readlines()

i = i[0].lower()
i = " ".join( i.split() )

print(main_func.Funnyinator(i))
