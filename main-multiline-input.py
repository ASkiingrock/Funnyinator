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

# with open("words.json", "r") as inputfile:  # The words to be swapped out are contained in the .JSON file, so they need to be taken out of it, which is what this does
#     words = json.load(inputfile)

# wordsList = list(words.items())

# for j in range(0, len(wordsList)-1):
#     i = i.replace(wordsList[j][0], wordsList[j][1])  # This replaces all the words

# i = i.split(" ") # Split the result


# for word in i: # This function just adds the funny words periodically
#     end = " "
#     if word[-1] not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ": # takes into account if the word has punctuation or something else at the end of it
#         end = word[-1] + " "
#         word = word[:-1]
        
#     ran = random.randint(1,25)   # This will add one of the "funny words" in the JSON file randomly every 25 words
#     output += f"{word}{end}"
#     if ran == 1:
#         funny = random.choice(words["funny words"])
#         output += f"{funny}{end}"

# print(output) # Output the result to the console