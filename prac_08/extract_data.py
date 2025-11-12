# Data extraction program

# Define the record as a dictionary for clarity
record = {
    "first_name": "Mercy",
    "last_name": "Korir",
    "birthdate": (8, 12, 2001),
    "profession": "piano"
}

def extract_and_print_data(record):
    """
    Extracts and prints specific data from the record.

    Parameters:
    record (dict): A dictionary containing personal information.

    """
    # Extract and print specific data
    print(f"Last name: {record['last_name']}")
    print(f"Born: {record['birthdate']}")
    print(f"{record['first_name']} was born in {record['birthdate'][2]} and was a great {record['profession']} player.")

# Main program flow
if __name__ == "__main__":
    extract_and_print_data(record)
