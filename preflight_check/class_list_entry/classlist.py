"""
Register Me Silly

Repeatedly checks Drexel's Term Master Schedule for availability of class sections

Author:  Anshul Kharbanda
Created: 9 - 21 - 2018
"""
from tkinter import *
from .klass import Class

class ClassList(Frame):
    """
    Docstring for ClassList
    """
    def __init__(self, master=None, classes=[]):
        """
        Initializes instance
        """
        super(ClassList, self).__init__(master)

        # Set classes
        for class_id, class_url in classes:
            self.add_class(class_id, class_url)

    def add_class(self, class_id, class_url):
        """
        Docstring for add_class
        """
        klass = Class(self, class_id=class_id, url=class_url)
        klass.pack(padx=2, pady=2, fill=X)

    @property
    def value(self):
        """
        Docstring for value property
        """
        return [klass.value for klass in self.winfo_children()]
