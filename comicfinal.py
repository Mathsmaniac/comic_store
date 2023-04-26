import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk


class Root(ThemedTk):
    def __init__(self):
        super().__init__()
        self.set_theme("blue")
        self.title("Comic Store")
        # Style for error labels
        s = ttk.Style()
        s.configure("Error.TLabel", foreground='red')
        # Variables
        self.comics_sold = tk.IntVar()
        self.clicked = tk.StringVar()
        # Main Frame
        self.mainframe = ttk.Frame(self)
        self.mainframe.grid(row=0, column=0, ipadx=10,
                            ipady=10, padx=1, pady=10)
        # Title Label
        ttk.Label(self.mainframe, text="Comic Book Store",
                  font=("Arial", 25)).grid(row=0, column=0,
                                           columnspan=3,
                                           padx=15, pady=15)
        # Comic book stock labels
        self.superlabel = ttk.Label(self.mainframe, text="Number "
                                    f"of {comic_info[0].name} in sto"
                                    f"ck: {comic_info[0].amount}")
        self.superlabel.grid(row=1, column=0, sticky=("n", "w"),
                             padx=21, pady=10)
        self.lizardlabel = ttk.Label(self.mainframe, text="Number of"
                                     f" {comic_info[1].name} in sto"
                                     f"ck: {comic_info[1].amount}")
        self.lizardlabel.grid(row=2, column=0, sticky=("n", "w"),
                              padx=21, pady=10)
        self.waterlabel = ttk.Label(self.mainframe, text="Number of"
                                    f"{comic_info[2].name} in sto"
                                    f"ck: {comic_info[2].amount}")
        self.waterlabel.grid(row=3, column=0, sticky=("n", "w"),
                             padx=21, pady=10)
        # Error label
        self.errorlabel = ttk.Label(self.mainframe,
                                    style="Error.TLabel")
        self.errorlabel.grid(row=5, column=0)
        # Slider
        self.comicnumber = tk.Scale(self.mainframe, from_=1, to=100,
                                    bg='#6699cc', highlightthickness=0,
                                    orient=tk.HORIZONTAL, length=200)
        self.comicnumber.grid(row=3, column=1, rowspan=2, columnspan=2,
                              sticky=('n'))
        # Drop down
        self.comiclist = ttk.OptionMenu(self.mainframe, self.clicked,
                                        *[x.name for x in comic_info])
        self.comiclist.grid(row=1, column=2, sticky=('n', 'w'), pady=5)
        # Info Label for drop down
        ttk.Label(self.mainframe, text="Comic title:").grid(row=1,
                                                            column=1)
        ttk.Label(self.mainframe, text="Number of Comics"
                  ":").grid(row=2, column=1, columnspan=2)
        # Buttons
        self.buybutton = ttk.Button(self.mainframe, text="Buy Comic",
                                    command=lambda: self.purchase())
        self.buybutton.grid(row=4, column=0, padx=20, pady=20)
        self.stockbutton = ttk.Button(self.mainframe, text="Restock"
                                      " Comic(s)",
                                      command=lambda: self.restock())
        self.stockbutton.grid(row=4, column=1, padx=20, pady=20)
        # Buy counter
        self.counter = ttk.Label(self.mainframe, text="Comics sold: "
                                 f"{self.comics_sold.get()}")
        self.counter.grid(row=5, column=1)

    # Function for restocking comics and updating labels

    def restock(self):
        for comic in comic_info:
            if comic.name == self.clicked.get():
                comic.restock(self.comicnumber.get())
                self.superlabel.config(text="Number of "
                                       f"{comic_info[0].name} in sto"
                                       f"ck: {comic_info[0].amount}")
                self.lizardlabel.config(text="Number of "
                                        f"{comic_info[1].name} in sto"
                                        f"ck: {comic_info[1].amount}")
                self.waterlabel.config(text="Number of"
                                       f"{comic_info[2].name} in sto"
                                       f"ck: {comic_info[2].amount}")

    # Function for buying comics and updating the labels

    def purchase(self):
        for comic in comic_info:
            if comic.name == self.clicked.get():
                comic.buy()
                self.superlabel.config(text="Number of "
                                       f"{comic_info[0].name} in sto"
                                       f"ck: {comic_info[0].amount}")
                self.lizardlabel.config(text="Number of "
                                        f"{comic_info[1].name} in st"
                                        f"ock: {comic_info[1].amount}")
                self.waterlabel.config(text="Number of "
                                       f"{comic_info[2].name} in sto"
                                       f"ck: {comic_info[2].amount}")
                self.counter.config(text="Comics sold: "
                                    f"{self.comics_sold.get()}")

    # Displays errors

    def makeerror(self, message, label):
        label.configure(text=message)
        # Hides the text
        self.after(5000, lambda: label.configure(text=""))


# Class for comic storage
class Comic():
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    # Decreases amount of comics by one if not less than 0

    def buy(self):
        if self.amount <= 0:
            root.makeerror("Out of Stock!", root.errorlabel)
        else:
            self.amount -= 1
            root.comics_sold.set(root.comics_sold.get() + 1)

    # Restocks comics

    def restock(self, number):
        self.amount += number


# Class data
comic_info = [Comic("Super Dude", 8), Comic("Lizard Man", 12),
              Comic("Water Woman", 3)]


if __name__ == '__main__':
    root = Root()
    tk.mainloop()
