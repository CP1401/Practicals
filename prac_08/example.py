# Example program to collect and display places visited on holiday

def collect_places():
    """
    Collects a list of places visited on holiday.

    Returns:
    list: A list of places entered by the user.
    """
    places = []
    while True:
        place = input("Place (press Enter to finish): ")
        if place == "":  # Break the loop if input is empty
            break
        places.append(place.title())  # Ensure title case
    return places


def display_places(places):
    """
    Displays the list of places visited on holiday.

    Parameters:
    places (list): A list of places visited.
    """
    if places:
        print("On my holiday, I went to:")
        for place in places:
            print(place)

        # Find and display the longest place
        longest_place = max(places, key=len)
        print(f"The place with the longest name was: {longest_place}")
    else:
        print("I went nowhere :(")


# Main program flow
if __name__ == "__main__":
    places = collect_places()  # Collect places
    display_places(places)  # Display places and the longest place
