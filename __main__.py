import Fonts.font_stadard as font_stadard
import ASCII_generator


def print_ascii(ascii_lines):
    for line in ascii_lines:
        print(line)

if __name__ == "__main__":
    text = input("Enter text to convert to ASCII: ")

    print_ascii(ASCII_generator.text_to_ascii(text.upper(), font_stadard.font))