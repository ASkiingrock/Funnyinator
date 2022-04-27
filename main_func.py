import json
import random
# import traceback # debugging

def Funnyinator(i):
    output = ""
    with open("Funnyinator/words.json", "r") as inputfile:  # The words to be swapped out are contained in the .JSON file, so they need to be taken out of it, which is what this does
        words = json.load(inputfile)

    wordsList = list(words.items())

    for j in range(0, len(wordsList)-1):
        i = i.replace(wordsList[j][0], wordsList[j][1])  # This replaces all the words

    i = i.split(" ") # Split the result


    for word in i: # This function just adds the funny words periodically
        word = word.replace(" ","")
        end = " "
        if word[-1] not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ": # takes into account if the word has punctuation or something else at the end of it
            end = word[-1] + " "
            word = word[:-1]
            
        ran = random.randint(1,25)   # This will add one of the "funny words" in the JSON file randomly every 25 words
        output += f"{word}{end}"
        if ran == 1:
            funny = random.choice(words["funny words"])
            output += f"{funny} "

    return output # Output the result to the console

if __name__ == "__main__":
    i = input("Enter your words:\n\n")  # get input
    i = i.lower()
    i = i.replace("  ", " ")
    # stuff only to run when not called via 'import' here
    print(Funnyinator(i))
