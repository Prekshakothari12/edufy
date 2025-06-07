import tkinter as tk
from tkinter import messagebox
import random

# List of words to choose from
WORDS = ['python', 'tkinter', 'hangman', 'interface', 'widget', 'canvas']

MAX_TRIES = 6

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.word = ''
        self.guessed = []
        self.tries = 0

        self.word_label = tk.Label(root, font=("Helvetica", 24))
        self.word_label.pack(pady=20)

        self.buttons_frame = tk.Frame(root)
        self.buttons_frame.pack()

        self.letter_buttons = {}
        for i, letter in enumerate("abcdefghijklmnopqrstuvwxyz"):
            btn = tk.Button(self.buttons_frame, text=letter, width=4, command=lambda l=letter: self.guess_letter(l))
            btn.grid(row=i // 9, column=i % 9, padx=2, pady=2)
            self.letter_buttons[letter] = btn

        self.status_label = tk.Label(root, text=f"Tries left: {MAX_TRIES}", font=("Helvetica", 14))
        self.status_label.pack(pady=10)

        self.restart_button = tk.Button(root, text="Restart", command=self.restart_game)
        self.restart_button.pack(pady=5)

        self.restart_game()

    def restart_game(self):
        self.word = random.choice(WORDS)
        self.guessed = []
        self.tries = 0
        for btn in self.letter_buttons.values():
            btn.config(state=tk.NORMAL)
        self.update_display()
        self.status_label.config(text=f"Tries left: {MAX_TRIES}")

    def update_display(self):
        display_word = ' '.join([letter if letter in self.guessed else '_' for letter in self.word])
        self.word_label.config(text=display_word)

    def guess_letter(self, letter):
        self.letter_buttons[letter].config(state=tk.DISABLED)
        if letter in self.word:
            self.guessed.append(letter)
            self.update_display()
            if all(l in self.guessed for l in self.word):
                messagebox.showinfo("Hangman", "You won!")
                self.disable_buttons()
        else:
            self.tries += 1
            self.status_label.config(text=f"Tries left: {MAX_TRIES - self.tries}")
            if self.tries >= MAX_TRIES:
                messagebox.showinfo("Hangman", f"You lost! The word was: {self.word}")
                self.disable_buttons()

    def disable_buttons(self):
        for btn in self.letter_buttons.values():
            btn.config(state=tk.DISABLED)

# Create the GUI window
if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
