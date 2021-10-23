"""
CP1401 Checkpoint 2
Subject List - Extended Version
See the demonstration videos for details and explanations
"""


def main():
    """Get and display subject codes."""
    subjects = []
    subject = get_subject()
    while subject != "":
        subjects.append(subject)
        subject = get_subject()
    number_of_subjects = len(subjects)
    if number_of_subjects == 0:
        print("You do no subjects")
    else:
        if number_of_subjects > 1:
            subjects.sort()
            print(f"You do these {number_of_subjects} subjects: ")
            for subject in subjects:
                print(subject)
        else:
            print("You do this subject: ")
            print(subjects[0])
        if "CP1401" in subjects:
            print("You are cool")


def get_subject():
    """Get a valid subject or empty string."""
    subject = input("Enter subject code: ")
    while len(subject) != 6 and subject != "":
        print("Invalid subject code")
        subject = input("Enter subject code: ")
    return subject


main()
