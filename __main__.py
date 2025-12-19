import fonts as fonts
import ASCII_generator


if __name__ == "__main__":

    ASCII_generator.wipe_console()
    ASCII_generator.text_to_ascii("ASCII-GENERATOR", fonts.HASH_FONT)
    print("========================================================================================================================")

    while True:
        what_to_do = input("What do you want to do? (text/image/video): ").strip().lower()

        if what_to_do not in ["text", "image", "video"]:
            print("Invalid option. Please choose 'text', 'image', or 'video'.")

        save_to_file = input("Do you want to save the output to a file? (y/n): ").strip().lower()
        
        if save_to_file not in ["y", "n"]:
            print("Invalid option. Please choose 'y', or 'n'.")
        
        if save_to_file == "y":
            ASCII_generator.save_to_file = True

        if what_to_do == "video":
            video_path = input("Enter video path to convert to ASCII: ")
            ASCII_generator.play_video_as_ascii(video_path)
        
        if what_to_do == "image":
            image_path = input("Enter image path to convert to ASCII: ")
            ASCII_generator.image_to_ascii(image_path)
        
        if what_to_do == "text":
            text = input("Enter text to convert to ASCII: ")
            if not text:
                print("No text provided. Exiting.")
            print("Available fonts:")
            print("1. # Font")
            print("2. * Font")
            print("3. = Font")
            print("4. + Font")
            print("5. . Font")
            print("6. @ Font")
            print("7. & Font")
            font_choice = input("Choose a font (1-7): ").strip()
            font = None
            if font_choice == "1":
                font = fonts.HASH_FONT
            elif font_choice == "2":
                font = fonts.STAR_FONT
            elif font_choice == "3":
                font = fonts.EQUAL_SIGN_FONT
            elif font_choice == "4":
                font = fonts.PLUS_FONT
            elif font_choice == "5":
                font = fonts.DOT_FONT
            elif font_choice == "6":
                font = fonts.AT_SIGN_FONT
            elif font_choice == "7":
                font = fonts.AMPERSAND_FONT
            else:
                print("Invalid font choice. Using default font.")
                font = fonts.HASH_FONT
            ASCII_generator.text_to_ascii(text.upper(), font)