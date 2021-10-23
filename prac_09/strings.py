"""
CP1401 - Strings
Suggested Solutions
Please do not use/view these solutions until you have attempted
the checkpoint challenges yourself!
Use these solutions as a guide to review and improve your completed work.
"""

REFERENCE_YEAR = 2021


# 6. Data Strings
def question_6():
    """Program to extract values from strings."""
    data_strings = ["Result = 95%", "Final Score = 8%", "Relative Value = 178%",
                    "Something else that's very important = 9.2%", "x = 42%"]
    for string in data_strings:
        start_index = string.find("= ")
        value = float(string[start_index + 2:-1])
        print(value)


# 7. Date Strings
def question_7():
    """Program that gets year from date of birth string."""
    dob_string = input("DOB: ")
    birth_year = int(dob_string[-4:])  # Extract the last 4 characters
    age = REFERENCE_YEAR - birth_year
    print(f"You were born in {birth_year}")
    print(f"You turn/ed {age} in {REFERENCE_YEAR}")


# 8. Subject Code Strings
def question_8():
    """Program to get and display subject code details."""
    subject = input("Enter subject code: ")
    while subject != "":
        if len(subject) == 6:
            it_string = ""
            if subject.startswith("CP"):
                it_string = " IT"
            if subject[2] == '1':
                year_string = "first-year"
            elif subject[2] == '2':
                year_string = "second-year"
            elif subject[2] == '3':
                year_string = "third-year"
            else:
                year_string = "Masters or other"
            print(f"That is a {year_string}{it_string} subject.")
        else:
            print("Invalid subject code")
        subject = input("Enter subject code: ")
