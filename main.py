import tkinter as tkinter

class GUIApplication(tkinter.Tk):
    def __init__(self, title):
        super().__init__()
        self.title(title)


if __name__ == "__main__":
    app = GUIApplication("tkGraf")
    app.mainloop()