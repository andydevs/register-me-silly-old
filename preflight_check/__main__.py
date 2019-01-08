"""
Register Me Silly

Repeatedly checks Drexel's Term Master Schedule for availability of class sections

Author:  Anshul Kharbanda
Created: 9 - 21 - 2018
"""
import config
from tkinter import Tk, X
from . import App

if __name__ == '__main__':
    window = Tk()
    app = App(window,
        key=config.key,
        interval=config.interval,
        classes=config.classes)
    app.pack(fill=X)
    window.title('Configure Register-Me-Silly')
    window.minsize(400, 300)
    window.mainloop()
