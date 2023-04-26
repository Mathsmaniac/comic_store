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
        ttk.Label(self.mainframe, text="Comic Book Store", font=("Arial", 25)).grid(row=0, column=0, columnspan=2, padx=15, pady=15)
        self.superlabel = ttk.Label(self.mainframe, text=f"Number of {comic_info[0].name} in stock: {comic_info[0].amount}")
        self.superlabel.grid(row=1, column=0, sticky=("n", "w"), padx=10, pady=5)
        self.lizardlabel = ttk.Label(self.mainframe, text=f"Number of {comic_info[1].name} in stock: {comic_info[1].amount}")
        self.lizardlabel.grid(row=2, column=0, sticky=("n", "w"), padx=10, pady=5)
        self.waterlabel = ttk.Label(self.mainframe, text=f"Number of {comic_info[2].name} in stock: {comic_info[2].amount}")
        self.waterlabel.grid(row=3, column=0, sticky=("n", "w"), padx=10, pady=5)


class Comic():
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount


# Class data
comic_info = [Comic("Super Dude", 8), Comic("Lizard Man", 12),
              Comic("Water Woman", 3)]


if __name__ == '__main__':
    root = Root()
    tk.mainloop()
