"""
CP1401 Practical 8 - Lists - Example
Julie is planning a holiday and wants to record all the places she goes in the order she visits them.
Once she returns, she wants to be able to display the list of places and also which place had the longest name (because she likes that sort of thing).
"""
places = []
place = input("Place: ").title()
while place != "":
    places.append(place)
    place = input("Place: ").title()

if len(places) > 0:
    print("On my holiday, I went to: ")
    longest_place = ""
    for place in places:
        print(place)
        if len(place) > len(longest_place):
            longest_place = place
    print(f"The place with the longest name was {longest_place}")
else:
    print("I went nowhere :(")
