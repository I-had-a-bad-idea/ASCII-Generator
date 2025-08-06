

def text_to_ascii(text, font):

    lines = [""] * 5  # Initialize a list for 5 lines of ASCII art

    for char in text:
        if char in font:
            for i in range(5):
                lines[i] += font[char][i]
                lines[i] += "  "  # Add space between characters
        else:
            for i in range(5):
                lines[i] += font[" "][i]
                lines[i] += "  "  # Add space for unknown characters

    return lines