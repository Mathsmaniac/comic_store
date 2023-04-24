import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk


class Root(ThemedTk):
    def __init__(self):
        super().__init__()
        self.set_theme("blue")
        self.title("Comic Store")
        self.mainframe = ttk.Frame(self)
        self.mainframe.grid(row=0, column=0, ipadx=10,
                            ipady=10, padx=1, pady=10)
#       Population for testing:
        ttk.Label(self.mainframe, text="testing").grid(
            row=0, column=0, padx=5, pady=5, sticky=("n, e")
        )
        ttk.Button(self.mainframe, text="Button").grid(
            row=1, column=0, padx=5, pady=5, sticky=("s", "e")
        )


if __name__ == '__main__':
    root = Root()
    tk.mainloop()
