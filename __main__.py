import Fonts.font_stadard as font_stadard
import ASCII_generator



if __name__ == "__main__":
    text = input("Enter text to convert to ASCII: ")

    ASCII_generator.text_to_ascii(text.upper(), font_stadard.font)

    image_path = input("Enter image path to convert to ASCII: ")
    ascii_image = ASCII_generator.image_to_ascii(image_path)
    
    video_path = input("Enter video path to convert to ASCII: ")
    ASCII_generator.play_video_as_ascii(video_path)