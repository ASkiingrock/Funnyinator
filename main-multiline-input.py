import main_func

with open("alternate_input.txt", "r") as f:
    alternate_input = f.readlines()

for line in alternate_input:  # Run function for each line
    print(main_func.funnyinator(line.strip()))
