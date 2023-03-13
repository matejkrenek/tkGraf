import tkinter as tkinter

class MyEntry(tkinter.Entry):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)

        if not "textvariable" in kw:
            self.variable = tkinter.StringVar()
            self.config(textvariable=self.variable)
        else:
            self.variable = kw["textvariable"]

    @property
    def value(self):
        return self.variable.get()

    @value.setter
    def value(self, new: str):
        self.variable.set(new)

class GUIApplication(tkinter.Tk):
    x = list(map(float, "0 0.3 0.5 0.8 1 2 3".split()))
    y = list(map(float, "0 0.1 0.5 1 3 10 30".split()))


    def __init__(self, title):
        super().__init__()
        self.title(title)

        self.RADIO_VARIABLE = tkinter.StringVar(value='cols')

        self.FileFrame = tkinter.LabelFrame(self, text='Soubor')
        self.FileFrame.pack()

        self.FileEntry = MyEntry(self.FileFrame)
        self.FileEntry.pack()

        self.FileButton = tkinter.Button(self.FileFrame, text='...')
        self.FileButton.pack(expand=True, fill='x')

        self.ColsRadio = tkinter.Radiobutton(self.FileFrame, text='Data jsou ve sloupcích', variable=self.RADIO_VARIABLE, value='cols')
        self.ColsRadio.pack(anchor='w')

        self.RowsRadio = tkinter.Radiobutton(self.FileFrame, text='Data jsou v řádcích', variable=self.RADIO_VARIABLE, value='rows')
        self.RowsRadio.pack(anchor='w')

        self.GraphFrame = tkinter.LabelFrame(self, text='Parametry grafu')
        self.GraphFrame.pack()

        self.QuitButton = tkinter.Button(self, text='Quit', command=self.quit)
        self.QuitButton.pack(expand=True, fill='x')

    def quit(self, event=None):
        super().quit()

if __name__ == "__main__":
    app = GUIApplication("tkGraf")
    app.mainloop()