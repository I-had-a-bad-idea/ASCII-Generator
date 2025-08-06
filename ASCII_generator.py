from PIL import Image
from PIL import ImageEnhance
from Fonts.pixels import ASCII_CHARS as ASCII_CHARS
import cv2 as cv

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


def image_to_ascii(image_path, new_width = 100):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Error: {e}")
        return

    image = resize_image(image, new_width)
    image = make_grayscale(image)

    ascii_str = pixels_to_ascii(image)
    pixel_count = len(ascii_str)
    ascii_img = "\n".join(
        ascii_str[i:(i + new_width)] for i in range(0, pixel_count, new_width)
    )
    return ascii_img


def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ''
    
    for pixel in pixels:
        # Map brightness to character index
        ascii_str += ASCII_CHARS[pixel * (len(ASCII_CHARS) - 1) // 255]
    
    return ascii_str

def resize_image(image, new_width = 100):
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width * 0.5)  # Adjust for font aspect ratio
    return image.resize((new_width, new_height), Image.Resampling.LANCZOS)


def make_grayscale(image):
    image = image.convert("L")
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2.0)  

    return image

def play_video_as_ascii(video_path, new_width = 100):
    cap = cv.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = resize_image(Image.fromarray(frame), new_width)
        # frame = Image.fromarray(frame)
        frame = make_grayscale(frame)
        ascii_frame = pixels_to_ascii(frame)
        pixel_count = len(ascii_frame)
        ascii_img = "\n".join(
            ascii_frame[i:(i + new_width)] for i in range(0, pixel_count, new_width)
        )
        
        clear_console()

        print(ascii_img)
        print("\n" + "=" * new_width + "\n")  # Separator for frames

    cap.release()

def clear_console():
    import os
    print("\033[H", end="")