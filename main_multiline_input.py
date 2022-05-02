import main_func

with open("alternate_input.txt", "r", encoding="utf-8") as f:  # Read alternate input file and load contents
    alternate_input = f.readlines()

with open("alternate_output.txt", "w", encoding="utf-8") as f:  # Write to alternate output file
    for line in alternate_input:  # Run function for each line
        f.write(main_func.funnyinator(line))
