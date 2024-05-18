from datetime import datetime

# Constants for Master Numbers and Lucky Colours
MASTER_NUMBERS = {11, 22, 33}
LUCKY_COLOURS = {
    1: "Red",
    2: "Orange",
    3: "Yellow",
    4: "Green",
    5: "Blue",
    6: "Indigo",
    7: "Violet",
    8: "Gray",
    9: "White",
    11: "Gold",
    22: "Silver",
    33: "Platinum"
}

GENERATIONS = {
    "Silent Generation": (1901, 1945),
    "Baby Boomers": (1946, 1964),
    "Generation X": (1965, 1979),
    "Millennials": (1980, 1994),
    "Generation Z": (1995, 2009),
    "Generation Alpha": (2010, 2024)
}

def validate_date(date_str):
    """ Validate the input date """
    try:
        if any(char.isalpha() for char in date_str):
            date = datetime.strptime(date_str, "%B %d %Y")
        else:
            date = datetime.strptime(date_str, "%m-%d-%Y")
        if 1901 <= date.year <= 2024:
            return date
        else:
            raise ValueError("Year out of range.")
    except ValueError as e:
        print(f"Invalid date: {e}")
        return None

def calculate_life_path_number(date):
    """ Calculate the Life Path Number """
    total = sum(int(digit) for digit in date.strftime("%Y%m%d"))
    while total > 9 and total not in MASTER_NUMBERS:
        total = sum(int(digit) for digit in str(total))
    return total

def get_lucky_colour(life_path_number):
    """ Get the Lucky Colour based on Life Path Number """
    return LUCKY_COLOURS.get(life_path_number)

def is_master_number(life_path_number):
    """ Check if the Life Path Number is a Master Number """
    return life_path_number in MASTER_NUMBERS

def identify_generation(year):
    """ Identify the generation based on birth year """
    for generation, (start, end) in GENERATIONS.items():
        if start <= year <= end:
            return generation
    return None

def compare_life_path_numbers(birthday1, birthday2):
    """ Compare Life Path Numbers of two birthdays """
    date1 = validate_date(birthday1)
    date2 = validate_date(birthday2)
    if not date1 or not date2:
        return False
    return calculate_life_path_number(date1) == calculate_life_path_number(date2)

# Example Usage
if __name__ == "__main__":
    # Single birthday analysis
    birthday = "October 25 1985"
    date = validate_date(birthday)
    if date:
        life_path_number = calculate_life_path_number(date)
        print(f"Life Path Number: {life_path_number}")
        print(f"Lucky Colour: {get_lucky_colour(life_path_number)}")
        print(f"Is Master Number: {is_master_number(life_path_number)}")
        print(f"Generation: {identify_generation(date.year)}")

    # Comparing two birthdays
    birthday1 = "June 15 1990"
    birthday2 = "December 12 1985"
    print(f"Life Path Numbers are the same: {compare_life_path_numbers(birthday1, birthday2)}")

#unittest

