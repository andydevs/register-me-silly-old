"""
Register Me Silly

Repeatedly checks Drexel's Term Master Schedule for availability of class sections

Author:  Anshul Kharbanda
Created: 9 - 21 - 2018
"""
from . import LabeledInput
from tkinter import *

class LabeledSpinbox(LabeledInput):
    """
    Docstring for LabeledSpinbox
    """
    def __init__(self, master=None, title='Label', value=''):
        """
        Initializes instance
        """
        super(LabeledSpinbox, self).__init__(master, title)

        # Value for entry
        self.entry = Spinbox(self, from_=0, to=10000)
        self.entry.pack(side=TOP, anchor=W, fill=X)
        self.entry.insert(0, value)
