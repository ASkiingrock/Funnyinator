import json
import random
import string


def funnyinator(input_string):
    with open("words.json", "r") as input_file:  # Words to be replaced are extracted from JSON file
        words = json.load(input_file)

    words_list = words["replacements"].keys()  # The list of words to be replaced

    replaced_string = input_string
    for word in words_list:
        replaced_string = replaced_string.lower().replace(word,
                                                          words["replacements"][word])  # Replace words in input string

    replaced_string = replaced_string.split(" ")  # Split the replaced string by word

    output_string = ""
    for word in replaced_string:  # This function just adds the funny words periodically
        output_string += f"{word} "
        try:
            if word[-1] not in string.punctuation:
                if random.randint(1, 25) == 1:  # Add in random 'funny' word given 1/25 chance
                    funny_word = random.choice(words["funny_words"])
                    output_string += f"{funny_word} "
        except IndexError:
            pass

    return output_string  # Return output


if __name__ == "__main__":
    unfunny_input = input("Enter your words:\n")  # Get input
    print(funnyinator(unfunny_input))  # Print outputted 'funny' string
