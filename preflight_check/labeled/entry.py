"""
Register Me Silly

Repeatedly checks Drexel's Term Master Schedule for availability of class sections

Author:  Anshul Kharbanda
Created: 9 - 21 - 2018
"""
from . import LabeledInput
from tkinter import *

class LabeledEntry(LabeledInput):
    """
    Docstring for LabeledEntry
    """
    def __init__(self, master=None, title='Label', value=''):
        """
        Initializes instance
        """
        super(LabeledEntry, self).__init__(master, title)

        # Value for entry
        self.entry = Entry(self)
        self.entry.pack(side=TOP, anchor=W, fill=X)
        self.entry.delete(0, END)
        self.entry.insert(0, value)
