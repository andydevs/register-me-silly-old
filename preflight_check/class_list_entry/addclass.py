"""
Register Me Silly

Repeatedly checks Drexel's Term Master Schedule for availability of class sections

Author:  Anshul Kharbanda
Created: 9 - 21 - 2018
"""
from tkinter import *
from ..labeled.entry import LabeledEntry

class AddClass(Frame):
    """
    Docstring for AddClass
    """
    def __init__(self, master=None, add_command=None):
        """
        Initializes instance
        """
        super(AddClass, self).__init__(master)
        self.add_command = add_command

        # Class ID Entry Widget
        self.id_entry = LabeledEntry(self, 'Class ID')
        self.id_entry.pack(padx=2, pady=2, fill=X)

        # Class URL Text Area Widget
        self.url_entry = LabeledEntry(self, 'TMS URL')
        self.url_entry.pack(padx=2, pady=2, fill=X)

        # Add button
        self.add_button = Button(self,
            text='Add Class',
            command=self.handle_add_button)
        self.add_button.pack(padx=2, pady=2, anchor=E)

    def handle_add_button(self):
        """
        Docstring for add_class
        """
        if self.add_command:
            self.add_command({
                'classid': self.id_entry.value,
                'url': self.url_entry.value
            })
