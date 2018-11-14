import os
from tkinter import *


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title(">////<")
        self.image = PhotoImage(file=resource_path("test.png"))

        self.label5 = Label(master, image=self.image)
        self.label = Label(master, justify=LEFT,
                           text="H-hi there...\n"
                                "I really like you a-and~\n"
                                "Can I p-please have your\n"
                                "credit card information?\n"
                                "I only need it to make s-sure you're real!")
        self.label2 = Label(master, justify=LEFT,
                           text="Card number:")
        self.label3 = Label(master, justify=LEFT,
                           text="Expiry date:")
        self.label4 = Label(master, justify=LEFT,
                            text="Security code:")
        self.entry = Entry(master)
        self.entry2 = Entry(master)
        self.entry3 = Entry(master)
        self.close_button = Button(master, text="T-thanks!", command=master.quit)

        self.label5.grid(row=0, rowspan=5, column=0, sticky=NW)
        self.label.grid(row=0, column=1, columnspan=2, sticky=W)
        self.label2.grid(row=1, column=1, sticky=E)
        self.label3.grid(row=2, column=1, sticky=E)
        self.label4.grid(row=3, column=1, sticky=E)
        self.close_button.grid(row=4, column=2)
        self.entry.grid(row=1, column=2, sticky=W)
        self.entry2.grid(row=2, column=2, sticky=W)
        self.entry3.grid(row=3, column=2, sticky=W)

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
