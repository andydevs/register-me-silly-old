"""
Register Me Silly

Repeatedly checks Drexel's Term Master Schedule for availability of class sections

Author:  Anshul Kharbanda
Created: 9 - 21 - 2018
"""
from .config import read_config_file
from tkinter import Tk, X
from . import App

if __name__ == '__main__':
    window = Tk()
    key, interval, classes = read_config_file()
    app = App(window,
        key=key,
        interval=interval,
        classes=classes)
    app.pack(fill=X)
    window.title('Configure Register-Me-Silly')
    window.geometry('300x400')
    window.resizable(False, True)
    window.mainloop()
