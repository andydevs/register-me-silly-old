"""
Register Me Silly

Repeatedly checks Drexel's Term Master Schedule for availability of class sections

Author:  Anshul Kharbanda
Created: 9 - 21 - 2018
"""
from tkinter import *

class Class(Frame):
    """
    Docstring for Class
    """
    def __init__(self, master=None, klass={'classid':'', 'url':''}):
        """
        Initializes instance
        """
        super(Class, self).__init__(master, borderwidth=1, relief='solid')

        # Class ID label
        self.class_id_label = Label(self, text=klass['classid'])
        self.class_id_label.pack(anchor=W, padx=1, pady=1)

        # Class URL Label
        self.url_label = Label(self, text=klass['url'], justify=LEFT)
        self.url_label.pack(anchor=W, padx=1, pady=1)

        # Delete Class Button
        self.delete_button = Button(self,
            text='Delete',
            command=self.delete)
        self.delete_button.pack(anchor=NW, padx=1, pady=1)

    def delete(self):
        """
        Docstring for delete
        """
        self.destroy()

    @property
    def value(self):
        """
        Docstring for value property
        """
        return {
            'classid': self.class_id_label['text'],
            'url': self.url_label['text']
        }
