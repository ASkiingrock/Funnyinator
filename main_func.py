import json
import random
import string
import re


def funnyinator(input_string):
    with open("words.json", "r") as input_file:  # Words to be replaced are extracted from JSON file
        words = json.load(input_file)

    words_list = words["replacements"].keys()  # The list of words to be replaced

    replaced_string = input_string
    for word in words_list:
        replaced_string = replaced_string.lower().replace(word,words["replacements"][word])  # Replace words in input string
    
    re_S = re.compile(r'(\S+)')
    replaced_string = re_S.split(replaced_string) # maintain whitespace characters

    for i in range(len(replaced_string)-1):
        if replaced_string[i] == ' ':
            if random.randint(1, 25) == 1:  # Add in random 'funny' word given 1/25 chance
                funny_word = random.choice(words["funny_words"])
                replaced_string[i] = f' {funny_word} '
    return ''.join(replaced_string)

if __name__ == "__main__":
    unfunny_input = input("Enter your words:\n")  # Get input
    print(funnyinator(unfunny_input))  # Print outputted 'funny' string
