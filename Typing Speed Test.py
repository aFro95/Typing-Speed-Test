import tkinter as tk

import time

class TypingSpeedApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.sample_text = "The quick brown fox jumps over the lazy dog."
        self.words_per_minute = 0
        self.start_time = None
        self.label_instruction = tk.Label(root, text="Type the following text:")
        self.label_instruction.pack(pady=10)
        self.label_text = tk.Label(root, text=self.sample_text, wraplength=400)
        self.label_text.pack(pady=10)
        self.entry_typing = tk.Entry(root, width=50)
        self.entry_typing.pack(pady=10)
        self.button_start = tk.Button(root, text="Start Typing", command=self.start_typing)
        self.button_start.pack(pady=10)
        self.label_result = tk.Label(root, text="")
        self.label_result.pack(pady=10)

    def start_typing(self):
        self.start_time = time.time()
        self.button_start.config(state=tk.DISABLED)
        self.entry_typing.bind('<KeyRelease>', self.check_typing)

    def check_typing(self, event):
        typed_text = self.entry_typing.get()
        if typed_text == self.sample_text:
            elapsed_time = time.time() - self.start_time
            words_typed = len(typed_text.split())
            self.words_per_minute = int((words_typed / elapsed_time) * 60)
            self.display_result()
        elif self.sample_text.startswith(typed_text):
            pass
        else:
            self.entry_typing.delete(0, tk.END)
            self.entry_typing.insert(0, self.sample_text[:len(typed_text)])

    def display_result(self):
        self.label_result.config(text=f"Words per minute: {self.words_per_minute}")
        self.button_start.config(state=tk.NORMAL)
        self.entry_typing.unbind('<KeyRelease>')

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedApp(root)
    root.mainloop()

