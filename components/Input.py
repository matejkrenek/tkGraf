import tkinter as tkinter


class Input(tkinter.Entry):
    def __init__(self, master=None, cnf={}, **kwargs):
        super().__init__(master, cnf, *kwargs)

        if not "textvariable" in kwargs:
            self.variable = tkinter.StringVar()
            self.config(textvariable=self.variable)
        else:
            self.variable = kwargs["textvariable"]

    @property
    def value(self):
        return self.variable.get()

    @value.setter
    def value(self, new_value: str):
        self.variable.set(new_value)
