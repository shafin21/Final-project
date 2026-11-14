def create_secret_file(message, filename):
    
    """Creates a text file and saves a hidden message inside it.

    Args:
        message (str): The hidden message to save.
        filename (str): The name of the text file.

    Returns:
        str: The name of the created text file.

    Side effects:
        Creates and writes to a text file.
    """

    words = message.split()
    format_message = ""
    
    for word in words: 
        if format_message != "":
            format_message += ""
        format_message += word
        
    if format_message == "":
        format_message = "No hidden message"
        
    with open(filename, "w") as file:
        file.write(format_message)
        
    return filename