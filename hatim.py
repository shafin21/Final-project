
"""Hatim Gawiesh
GitHub: WorkingHatim
Function: validate_hex
"""

def validate_hex(user_input):
    """Checks whether user input is a valid hexadecimal value.

    Args:
        user_input (str): The value entered by the user.

    Returns:
        bool: True if the hexadecimal value is valid.

    Raises:
        ValueError: If the input is empty or invalid.
    """

    valid_characters = "0123456789ABCDEFabcdef"

    if user_input == "":
        raise ValueError("Input cannot be empty.")

    for character in user_input:
        if character not in valid_characters:
            raise ValueError("Invalid hexadecimal value.")

    return True



