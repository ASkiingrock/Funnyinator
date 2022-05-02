import main_func

with open("alternate_input.txt", "r") as f:  # Read alternate input file and load contents
    alternate_input = f.readlines()

with open("alternate_output.txt", "w") as f:  # Write to alternate output file
    for line in alternate_input:  # Run function for each line
        f.write(main_func.funnyinator(line))
