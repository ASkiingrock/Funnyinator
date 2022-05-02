import json
import random
import string
import re


# The main function, takes a string as input, and returns an output string with words replaced
def funnyinator(input_string: str):
    with open("words.json", "r", encoding="utf-8") as input_file:  # Words to be replaced are extracted from JSON file
        words = json.load(input_file)

    words_list = words["replacements"].keys()  # The list of words to be replaced

    replaced_string = input_string
    for word in words_list:
        replaced_string = replaced_string.lower()
        replaced_string = re.sub(f"\\b{word}\\b", words["replacements"][word], replaced_string)

    output_string = replaced_string.split(" ")
    for word_count, word in enumerate(output_string):
        if random.randint(1, 25) == 1 and "\n" not in word:  # Add in random 'funny' word given 1/25 chance
            funny_word = random.choice(words["funny_words"])
            output_string[word_count] += f" {funny_word}"
            print(output_string)

    return " ".join(output_string)


if __name__ == "__main__":
    unfunny_input = input("Enter your words:\n")  # Get input
    print(funnyinator(unfunny_input))  # Print outputted 'funny' string
