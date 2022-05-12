"""
CP1401 - Files
Suggested Solutions
Please do not use/view these solutions until you have attempted
the checkpoint challenges yourself!
Use these solutions as a guide to review and improve your completed work.
"""


# 4. Read a String from a File
def question_4():
    """Read a name from a file."""
    in_file = open("name.txt", "r")
    name = in_file.read().strip()
    print(f"Greetings {name}!")


# 6. File Filter
def question_6():
    """File Filter - copy filtered lines from one file to another."""
    input_filename = input("Input filename: ")
    output_filename = input("Output filename: ")
    search_string = input("Search string: ")
    input_file = open(input_filename, 'r')
    output_file = open(output_filename, 'w')
    for line in input_file:
        if search_string in line:
            print(line, file=output_file, end="")  # don't print \n since line already includes it
    input_file.close()
    output_file.close()
