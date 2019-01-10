"""
Register Me Silly

Repeatedly checks Drexel's Term Master Schedule for availability of class sections

Author:  Anshul Kharbanda
Created: 9 - 21 - 2018
"""
from tkinter import *
from .classlist import ClassList
from .addclass import AddClass

class ClassListEntry(Frame):
    """
    Docstring for ClassListEntry
    """
    def __init__(self, master=None, classes=[]):
        """
        Initializes instance
        """
        super(ClassListEntry, self).__init__(master)

        # ClassList label
        self.class_label = Label(self, text='Add Classes...', anchor=W)
        self.class_label.pack(fill=X, pady=1)

        # Classes list
        self.class_list = ClassList(self, classes)
        self.class_list.pack(fill=X, pady=1)

        # Add Class
        self.add_class = AddClass(self, add_command=self.handle_add_class)
        self.add_class.pack(side=BOTTOM, fill=X, pady=1)

    def handle_add_class(self, klass):
        """
        Docstring for handle_add_class
        """
        self.class_list.add_class(klass)

    @property
    def value(self):
        """
        Docstring for value property
        """
        return self.class_list.value
