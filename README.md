ASCII-Generator is a Python tool to convert text, images, and videos into ASCII-Art. It allows users to create beautiful, text-based representations of media with customizable font options and more.

## Features

    Text to ASCII-Art: Convert plain text into stylish ASCII-Art.

    Image to ASCII-Art: Transform images into ASCII representations.

    Video to ASCII-Art: Convert videos into frame-by-frame ASCII visuals.

    Font Customization: Choose from various ASCII fonts for unique text art.

## Requirements

    Python 3.x

    Libraries:

        Pillow

        opencv-python

## Releases

Check the [releases](https://github.com/I-had-a-bad-idea/ASCII-Generator/releases) page for the latest versions. Each release includes:

    Windows executable (.exe)

    Release notes with change log

## Usage

    Download the latest release.

    Run the executable: You'll be prompted to choose the type of input:

        Text: Enter the text you want to convert into ASCII-Art.

        Image: Provide the path to your image.

        Video: Provide the path to your video.

    Font Selection (Text Only): If you choose the text option, you'll be asked to select from several ASCII fonts.


## Project Structure

    ASCII-Generator/
    ├── __main__.py           # Entry-Point + User interaction
    ├── ASCII_generator       # Core functionality
    ├── fonts.py              # All fonts for the text
    ├── pixels.py             # The characters used for image/video creation
    ├── requirements.txt      # List of dependencies
    └── README.md             # README

## Contributing

To contribute:

    Fork the repository

    Create a feature branch (git checkout -b feature/your-feature)

    Commit your changes (git commit -m 'Add a feature')

    Push to the branch (git push origin feature/your-feature)

    Open a Pull Request

## License

MIT License
