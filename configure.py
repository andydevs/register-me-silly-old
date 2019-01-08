"""
Register Me Silly

Repeatedly checks Drexel's Term Master Schedule for availability of class sections

Author:  Anshul Kharbanda
Created: 9 - 21 - 2018
"""
import config
from tkinter import *
from tkinter import messagebox

# Config file header
config_file_header = """
Register Me Silly

Repeatedly checks Drexel's Term Master Schedule for availability of class sections

Author:  Anshul Kharbanda
Created: 9 - 21 - 2018
"""

def write_config_file(key='', interval=1000, classes=[]):
    """
    Docstring for save_config_data
    """
    with open('config.py', 'w+') as f:
        f.write('"""' + config_file_header + '"""\n\n')
        f.write('# IFTTT Maker Key\n')
        f.write('key = \'' + key + '\'\n\n')
        f.write('# Check every interval\n')
        f.write('interval = ' + str(interval) + '\n\n')
        f.write('# Classes to check\n')
        f.write('classes = [\n' \
            + ',\n'.join(
                f"\t('{classid}', '{webpage}')"
                for classid, webpage in classes) \
            + '\n]\n\n')

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
        self.entry.insert(0, value)

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

class Class(Frame):
    """
    Docstring for Class
    """
    def __init__(self, master=None, class_id='', url=''):
        """
        Initializes instance
        """
        super(Class, self).__init__(master, borderwidth=1, relief='solid')

        # Class ID label
        self.class_id_label = Label(self, text=class_id)
        self.class_id_label.pack(anchor=W, padx=1, pady=1)

        # Class URL Label
        self.url_label = Label(self, text=url)
        self.url_label.pack(anchor=W, padx=1, pady=1)

        # Delete Class Button
        self.delete_button = Button(self, text='Delete', command=self.delete)
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
        return (
            self.class_id_label['text'],
            self.url_label['text']
        )

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
            self.add_command(
                self.id_entry.value,
                self.url_entry.value)

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

    def handle_add_class(self, class_id, class_url):
        """
        Docstring for handle_add_class
        """
        self.class_list.add_class(class_id, class_url)

    @property
    def value(self):
        """
        Docstring for value property
        """
        return self.class_list.value

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
