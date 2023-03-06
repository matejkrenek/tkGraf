import tkinter as tkinter
from scipy import interpolate
import pylab as pl

class GUIApplication(tkinter.Tk):
    x = list(map(float, "0 0.3 0.5 0.8 1 2 3".split()))
    y = list(map(float, "0 0.1 0.5 1 3 10 30".split()))
    

    def __init__(self, title):
        super().__init__()
        self.title(title)
        newX = pl.linspace(0, 3, 333)
        spl = interpolate.CubicSpline(self.x, self.y)
        newY = spl(newX)
        pl.plot(newX, newY, ':', label="Interpolace")
        pl.plot(self.x, self.y, label="Origin chart")
        pl.show()


if __name__ == "__main__":
    app = GUIApplication("tkGraf")
    app.mainloop()