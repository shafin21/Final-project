def decode_hex_message(hex_value, secret_key, filename):
    """Converts hexadecimal into binary and retrieves a hidden message.

    Args:
        hex_value (str): The hexadecimal value entered by the user.
        secret_key (str): The correct binary access key.
        filename (str): The name of the file containing the message.

    Returns:
        str: The hidden message retrieved from the text file.

    Raises:
        ValueError: If the hexadecimal value is invalid or incorrect.
        FileNotFoundError: If the text file cannot be found.

    Side effects:
        Reads the text file to retrieve the hidden message.
    """

    from hex_validation import validate_hex

    validate_hex(hex_value)

    binary_value = ""

    for character in hex_value:
        binary_digit = bin(int(character, 16))[2:]
        binary_value += binary_digit.zfill(4)

    if binary_value != secret_key:
        raise ValueError("Incorrect secret key.")

    with open(filename, "r") as file:
        message = file.read()

    if message == "":
        return "The secret file is empty."

    return message



