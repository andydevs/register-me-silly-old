"""
Register Me Silly

Repeatedly checks Drexel's Term Master Schedule for availability of class sections

Author:  Anshul Kharbanda
Created: 9 - 21 - 2018
"""
from tkinter import *
from tkinter import messagebox
from .labeled.entry import LabeledEntry
from .labeled.spinbox import LabeledSpinbox
from .class_list_entry import *
from .config import write_config_file

class App(Frame):
    """
    Docstring for App
    """
    def __init__(self, master=None, key='', interval=0, classes=[]):
        """
        Initializes instance
        """
        super(App, self).__init__(master)

        # Title
        self.title = Label(self, text='Configure Register-Me-Silly')
        self.title.pack(padx=1, pady=1, fill=X)

        # Key Entry
        self.key_entry = LabeledEntry(self, 'IFTTT API Key', key)
        self.key_entry.pack(padx=1, pady=1, fill=X)

        # Interval Entry
        self.interval_entry = LabeledSpinbox(self, 'Check Interval', str(interval))
        self.interval_entry.pack(padx=1, pady=1, fill=X)

        # Class List
        self.class_list_entry = ClassListEntry(self, classes)
        self.class_list_entry.pack(padx=1, pady=1, fill=X)

        # Save Button
        self.save_button = Button(self, text='Save', command=self.save_config)
        self.save_button.pack(padx=1, pady=1)

    def save_config(self):
        """
        Docstring for save_config
        """
        write_config_file(
            key=self.key_entry.value,
            interval=self.interval_entry.value,
            classes=self.class_list_entry.value)
        messagebox.showinfo("Success!", "Config file saved successfully!")
