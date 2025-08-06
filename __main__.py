import Fonts.font_stadard as font_stadard
import ASCII_generator


def print_ascii(ascii_lines):
    for line in ascii_lines:
        print(line)

if __name__ == "__main__":
    text = input("Enter text to convert to ASCII: ")

    print_ascii(ASCII_generator.text_to_ascii(text.upper(), font_stadard.font))

    image_path = input("Enter image path to convert to ASCII: ")
    ascii_image = ASCII_generator.image_to_ascii(image_path)
    if ascii_image:
        print(ascii_image)
    else:
        print("Failed to convert image to ASCII.")
    
    video_path = input("Enter video path to convert to ASCII: ")
    ASCII_generator.play_video_as_ascii(video_path)