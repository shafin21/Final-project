def create_secret_file(message, filename):
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