from tkinter import *
from tkinter import ttk
import string
import random

upper = string.ascii_uppercase
lower = string.ascii_lowercase
digits = string.digits


class PasswordVault:
    def __init__(self, root) -> None:
        self.app_list = {}

        root.title("Password Vault")
        self.mainframe = ttk.Frame(root, padding="8 8 8 12")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        generate = False
        ttk.Label(self.mainframe, text="welcome").grid(
            column=1, row=5, sticky=E)
        self.create = ttk.Button(self.mainframe, text="Create",
                   command=self.generate_password)
        self.create.grid()
        self.retrieve = ttk.Button(self.mainframe, text="Retrieve",
                   command=self.retrieve)
        self.retrieve.grid()

    def generate_password(self):
        print("here")
        self.name = StringVar()
        name_entry = ttk.Entry(self.mainframe, width=20,
                               textvariable=self.name)
        name_entry.grid(column=2, row=1, sticky=(E, W))
        ttk.Label(self.mainframe, text="name").grid(column=1, row=1, sticky=E)

        self.min_length = StringVar()
        length_entry = ttk.Entry(
            self.mainframe, width=20, textvariable=self.min_length)
        length_entry.grid(column=2, row=2, sticky=(E, W))
        ttk.Label(self.mainframe, text="min. length").grid(
            column=1, row=2, sticky=E)

        self.min_lower = StringVar()
        lower_entry = ttk.Entry(self.mainframe, width=20,
                                textvariable=self.min_lower)
        lower_entry.grid(column=2, row=3, sticky=(E, W))
        ttk.Label(self.mainframe, text="min. lowercase").grid(
            column=1, row=3, sticky=E)

        self.min_upper = StringVar()
        upper_entry = ttk.Entry(self.mainframe, width=20,
                                textvariable=self.min_upper)
        upper_entry.grid(column=2, row=4, sticky=(E, W))
        ttk.Label(self.mainframe, text="min. uppercase").grid(
            column=1, row=4, sticky=E)

        self.min_digits = StringVar()
        digits_entry = ttk.Entry(
            self.mainframe, width=20, textvariable=self.min_digits)
        digits_entry.grid(column=2, row=5, sticky=(E, W))
        ttk.Label(self.mainframe, text="min. digits").grid(
            column=1, row=5, sticky=E)

        self.create.configure(text='')
        ttk.Button(self.mainframe, text="Generate",
                   command=self.password_generator).grid()
        self.generated_password = StringVar()

        # ttk.Label(self.mainframe, textvariable=self.generated_password).grid(column=2, row=6, sticky=E)

        ttk.Button(self.mainframe, text="Save",
                   command=self.save_password).grid()

        for child in self.mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)
        name_entry.focus()

    def retrieve(self):
        print(self.app_list)
        

    def password_generator(self, *args):
        value = ''
        try:
            min_lower = int(self.min_lower.get())
            min_upper = int(self.min_upper.get())
            min_digits = int(self.min_digits.get())
            min_length = int(self.min_length.get())
        except ValueError:
            pass
        for _ in range(min_lower):
            value += random.choice(lower)

        for _ in range(min_upper):
            value += random.choice(upper)

        for _ in range(min_digits):
            value += random.choice(digits)

        min_length += random.randint(0, 9)
        while len(value) <= min_length:
            value += random.choice(upper+lower+digits)

        self.generated_password.set(
            ''.join(random.sample(value, k=len(value))))
        ttk.Label(self.mainframe, text="Password copied to clipboard").grid(
            column=1, row=6, sticky=E)

    def save_password(self):
        self.app_list[self.name.get()] = self.generated_password.get()
        ttk.Label(self.mainframe, text="Password saved").grid(
            column=1, row=7, sticky=E)
        self.name.set('')
        self.min_digits.set('')
        self.min_upper.set('')
        self.min_length.set('')
        self.min_lower.set('')
        print(self.app_list)


root = Tk()
PasswordVault(root)
root.mainloop()
