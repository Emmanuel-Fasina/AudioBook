# AudioBook

A simple Python GUI application that converts text from a `.txt` file into speech using `pyttsx3`.

## Features

- Open a plain text (`.txt`) file
- Display the loaded text in a text editor area
- Play the text out loud using text-to-speech
- Simple and minimal Tkinter-based interface

## Requirements

- Python 3.7 or newer
- `tkinter` (included with most Python installations)
- `pyttsx3`

## Installation

1. Clone or download this repository.
2. Install the Python dependency:

```bash
pip install pyttsx3
```

## Usage

Run the application with:

```bash
python my_audiobook.py
```

Then:

1. Click `Open Text File` to choose a `.txt` file.
2. The file contents will appear in the text box.
3. Click `Play Audio` to hear the text read aloud.

## Notes

- If the text box is empty, the app shows a warning message.
- The application currently supports only `.txt` files.
