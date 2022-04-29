import main_func

with open("alternate_input.txt", "r") as f:
    alternate_input = f.readlines()

with open("alternate_output.txt", "w") as f:
    f.truncate(0)
    f.seek(0)
    for line in alternate_input:  # Run function for each line
        f.write(main_func.funnyinator(line))
