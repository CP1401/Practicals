"""
CP1401 - Files
Suggested Solutions
Please do not use/view these solutions until you have attempted
the checkpoint challenges yourself!
Use these solutions as a guide to review and improve your completed work.
"""


def question_4():
    """Read a name from a file."""
    in_file = open("name.txt", "r")
    name = in_file.read().strip()
    print(f"Greetings {name}!")
