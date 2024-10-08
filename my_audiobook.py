import tkinter as tk
from tkinter import filedialog, messagebox
import pyttsx3


class AudioBook:
    def __init__(self, window):
        self.window = window
        self.window.title("AudioBook")
        self.window.configure(bg="dark green")

        self.text_box = tk.Text(self.window, wrap="word", width=70, height=30)
        self.text_box.pack(pady=20)

        self.open_file_button = tk.Button(self.window, text="Open Text File", command=self.open_text_file)
        self.open_file_button.pack(pady=10)

        self.play_audio_button = tk.Button(self.window, text="Play Audio", command=self.play_audio)
        self.play_audio_button.pack(pady=10)

        self.engine = pyttsx3.Engine()

    def open_text_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")], title="Choose a text file.")
        try:
            file = open(file_path, "rt")
            text = file.read()
            file.close()
            self.text_box.insert(0.0, text)
        except IOError:
            messagebox.showerror("Error", "Could not open file.")

    def play_audio(self):
        text = self.text_box.get(0.0, tk.END).strip()
        if text == "":
            messagebox.showinfo("Warning", "TextBox is empty!")
        else:
            self.engine.say(text)
            self.engine.runAndWait()


def main():
    window = tk.Tk()
    AudioBook(window)
    window.mainloop()


main()
