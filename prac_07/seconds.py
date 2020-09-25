"""CP1401 Practical 7 - Suggested Solution - Seconds."""


def main():
    """Demonstrate time display based on values in seconds."""
    time_in_seconds = 61
    time_to_display = convert_seconds_to_display(time_in_seconds)
    print(f"{time_in_seconds} seconds is {time_to_display}")

    for number_of_seconds in range(635, 13500, 3634):
        print(f"{number_of_seconds:5} seconds is {convert_seconds_to_display(number_of_seconds)}")
    number_of_seconds += 38791
    print(f"{number_of_seconds:5} seconds is {convert_seconds_to_display(number_of_seconds)}")


# Non-hours version:
# def convert_seconds_to_display(time_in_seconds):
#     """Convert time in seconds to formatted string with minutes and seconds."""
#     minutes = time_in_seconds // 60
#     seconds = time_in_seconds % 60
#     time_to_display = f"{minutes}m {seconds}s"
#     return time_to_display

# Extension version:
def convert_seconds_to_display(time_in_seconds):
    """Convert time in seconds to formatted string with hours, minutes and seconds."""
    hours = time_in_seconds // 3600  # 60 * 60
    minutes = time_in_seconds // 60
    minutes -= hours * 60
    seconds = time_in_seconds % 60
    # if hours == 0:
    #     return f"{minutes:2}m {seconds:2}s"
    return f"{hours:2}h {minutes:2}m {seconds:2}s"


main()
