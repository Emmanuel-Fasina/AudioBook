A lightweight desktop application that turns any `.txt` file into spoken audio, built with Python, Tkinter, and `pyttsx3`.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Notes](#notes)
- [License](#license)

## Overview
AudioBook is a simple GUI tool that loads a plain text file, displays its contents in an editor pane, and reads it aloud using offline text-to-speech — no internet connection or API key required.

## Features
- 📂 Open and load any `.txt` file
- 📝 View the loaded text in a built-in editor pane
- 🔈 Convert text to speech and play it aloud with one click
- 🖥️ Minimal, distraction-free Tkinter interface

## Tech Stack
| Component | Technology |
|---|---|
| Language | Python 3 |
| GUI | Tkinter |
| Text-to-Speech | pyttsx3 (offline TTS engine) |

## Installation
```bash
git clone https://github.com/Emmanuel-Fasina/AudioBook.git
cd AudioBook
pip install pyttsx3
```

## Usage
```bash
python main.py
```
1. Click **Open Text File** and select a `.txt` file.
2. The contents load into the text box automatically.
3. Click **Play Audio** to hear the text read aloud.

## Project Structure
```
AudioBook/
├── main.py       # Application logic and GUI
└── README.md     # Project documentation
```

## Notes
- Only `.txt` files are currently supported.
- Attempting to play with an empty text box triggers a warning dialog.

## License
This project was built for educational purposes.

---
Built by [Emmanuel Fasina](https://github.com/Emmanuel-Fasina)
