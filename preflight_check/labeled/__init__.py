"""
Register Me Silly

Repeatedly checks Drexel's Term Master Schedule for availability of class sections

Author:  Anshul Kharbanda
Created: 9 - 21 - 2018
"""
from tkinter import *

class LabeledInput(Frame):
    """
    Docstring for LabeledInput
    """
    def __init__(self, master=None, title='Label'):
        """
        Initializes instance
        """
        super(LabeledInput, self).__init__(master)

        # Label for input
        self.label = Label(self, text=title, anchor=W)
        self.label.pack(side=TOP, anchor=W, fill=X)

    @property
    def value(self):
        """
        Docstring for value property
        """
        return self.entry.get()
