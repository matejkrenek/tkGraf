import tkinter as tkinter
from tkinter import filedialog, messagebox
from components import Input
import matplotlib.pyplot as pl

class ZrudaException(Exception):
    pass

class Application(tkinter.Tk):
    def __init__(self, title):
        super().__init__()
        self.title(title)
        self.minsize(300, 500)
        self.maxsize(300, 500)
        self.bind("<Escape>", self.quit)

        # Variables
        self.data_format = tkinter.StringVar(self, value="rows")
        self.data_splitter = tkinter.StringVar(self, value=" ")
        self.chart_grid = tkinter.BooleanVar()
        self.chart_curve_line_type = tkinter.StringVar(self, value="-")
        self.chart_curve_marker_type = tkinter.StringVar(self, value=",")
        self.chart_curve_line_color = tkinter.StringVar(self, value="black")
        self.chart_curve_marker_color = tkinter.StringVar(self, value="black")

        # File Upload Section
        self.FileFrame = tkinter.LabelFrame(self, text="Soubor")
        self.FileFrame.pack(padx=4, pady=4, fill="x")

        self.FileInput = Input(self.FileFrame)
        self.FileInput.pack(padx=4, side=tkinter.LEFT, expand=True, fill="x")

        self.FileButton = tkinter.Button(
            self.FileFrame, text='...', command=self.handleFileSelect)
        self.FileButton.pack(padx=4, side=tkinter.RIGHT)

        # File Params Adjustment Section
        self.FileParamsFrame = tkinter.LabelFrame(
            self, text="Parametry souboru")
        self.FileParamsFrame.pack(padx=4, pady=4, fill="x")

        self.FileDataFormatLabel = tkinter.Label(
            self.FileParamsFrame, text="Formát dat")
        self.FileDataFormatLabel.pack(fill="x", anchor=tkinter.W)
        
        self.FileDataFormatRadioRow = tkinter.Radiobutton(
            self.FileParamsFrame, text="Data v řádcích", variable=self.data_format, value="rows")
        self.FileDataFormatRadioRow.pack()

        self.FileDataFormatRadioColumn = tkinter.Radiobutton(
            self.FileParamsFrame, text="Data v sloupcích", variable=self.data_format, value="columns")
        self.FileDataFormatRadioColumn.pack()

        self.FileDataSplitterLabel = tkinter.Label( 
            self.FileParamsFrame, text="Splitter dat")
        self.FileDataSplitterLabel.pack(fill="x", anchor=tkinter.W)

        self.FileDataSplitterSelect = tkinter.OptionMenu(
            self.FileParamsFrame, self.data_splitter, *(" ", ";", ",", "|"))
        self.FileDataSplitterSelect.pack()

        # Chart Params Adjustment Section
        self.ChartParamsFrame = tkinter.LabelFrame(
            self, text="Parametry grafu")
        self.ChartParamsFrame.pack(padx=4, pady=4, fill="x")

        self.ChartTitleLabel = tkinter.Label(
            self.ChartParamsFrame, text="Titulek")
        self.ChartTitleLabel.grid(row=0, column=0)

        self.ChartTitleInput = Input(
            self.ChartParamsFrame)
        self.ChartTitleInput.grid(row=0, column=1)

        self.ChartLegendLabel = tkinter.Label(
            self.ChartParamsFrame, text="Legenda")
        self.ChartLegendLabel.grid(row=1, column=0)

        self.ChartLegendInput = Input(
            self.ChartParamsFrame)
        self.ChartLegendInput.grid(row=1, column=1)

        self.ChartAxisXLabel = tkinter.Label(
            self.ChartParamsFrame, text="Osa x")
        self.ChartAxisXLabel.grid(row=2, column=0)

        self.ChartAxisXInput = Input(
            self.ChartParamsFrame)
        self.ChartAxisXInput.grid(row=2, column=1)

        self.ChartAxisYLabel = tkinter.Label(
            self.ChartParamsFrame, text="Osa y")
        self.ChartAxisYLabel.grid(row=3, column=0)

        self.ChartAxisYInput = Input(
            self.ChartParamsFrame)
        self.ChartAxisYInput.grid(row=3, column=1)

        self.ChartGridLabel = tkinter.Label(
            self.ChartParamsFrame, text="Zapnout mřížku")
        self.ChartGridLabel.grid(row=4, column=0)

        self.ChartGridCheckbox = tkinter.Checkbutton(
            self.ChartParamsFrame, variable=self.chart_grid)
        self.ChartGridCheckbox.grid(row=4, column=1)

        # Chart Curve Params Adjustment Section
        self.ChartCurveParamsFrame = tkinter.LabelFrame(
            self, text="Parametry křivky grafu")
        self.ChartCurveParamsFrame.pack(padx=4, pady=4, fill="x")

        self.ChartCurveLineLabel = tkinter.Label(
            self.ChartCurveParamsFrame, text="Čára (typ, barva)")
        self.ChartCurveLineLabel.grid(row=0, column=0)

        self.ChartCurveLineType = tkinter.OptionMenu(
            self.ChartCurveParamsFrame, self.chart_curve_line_type, *("None", "-", ":", "--", "-."))
        self.ChartCurveLineType.grid(row=0, column=1)

        self.ChartCurveLineColor = tkinter.OptionMenu(
            self.ChartCurveParamsFrame, self.chart_curve_line_color, *("black", "green", "red", "blue", "purple", "pink", "yellow", "grey", "orange"))
        self.ChartCurveLineColor.grid(row=0, column=2)

        self.ChartCurveMarkerLabel = tkinter.Label(
            self.ChartCurveParamsFrame, text="Marker (typ, barva)")
        self.ChartCurveMarkerLabel.grid(row=1, column=0)

        self.ChartCurveMarkerType = tkinter.OptionMenu(
            self.ChartCurveParamsFrame, self.chart_curve_marker_type, *tuple(",.oxX+-PD123<>v"))
        self.ChartCurveMarkerType.grid(row=1, column=1)

        self.ChartCurveMarkerColor = tkinter.OptionMenu(
            self.ChartCurveParamsFrame, self.chart_curve_marker_color, *("black", "green", "red", "blue", "purple", "pink", "yellow", "grey", "orange"))
        self.ChartCurveMarkerColor.grid(row=1, column=2)

        # Action Buttons Section
        self.ActionFrame = tkinter.Frame(self)
        self.ActionFrame.pack()

        self.ActionDrawButton = tkinter.Button(
            self.ActionFrame, text="Kreslit", command=self.handleDraw)
        self.ActionDrawButton.pack(padx=8, pady=8, side=tkinter.LEFT)

        self.ActionQuitButton = tkinter.Button(self.ActionFrame, text="Quit")
        self.ActionQuitButton.pack(padx=8, pady=8, side=tkinter.RIGHT)

    def loadTXTData(self, filename):
        x = []
        y = []

        with open(filename) as file:
            if(self.data_format.get().lower() == 'columns'):
                while True:
                    line = file.readline()

                    if line == "": break

                    parsed = list(filter(lambda elm: elm != '',line.split(self.data_splitter.get())))
                    
                    x.append(float(parsed[0]))
                    y.append(float(parsed[1]))
            elif(self.data_format.get().lower() == 'rows'):
                x = [*map(float, list(filter(lambda elm: elm != '',file.readline().strip().split(self.data_splitter.get()))))]
                y = [*map(float, list(filter(lambda elm: elm != '',file.readline().strip().split(self.data_splitter.get()))))]

        return (x, y)


    def loadCSVData(self, filename):
        x, y = self.loadTXTData(filename)

        
        return (x,y)


    def handleFileSelect(self, event=None):
        self.FileInput.value = filedialog.askopenfilename(
            filetypes=[("Povolené formáty", ("*.csv", "*.txt"))])

    def handleDraw(self, event=None):
        extension = self.FileInput.value.split('.')[-1]
        x, y = ([], [])
        
        try:
            if " " in self.FileInput.value: raise ZrudaException
            
            if extension == "csv": 
                x, y = self.loadCSVData(self.FileInput.value)

            elif extension == "txt":
                x, y = self.loadTXTData(self.FileInput.value)

            else: raise FileNotFoundError

            self.drawChart(x, y)
        except FileNotFoundError:
            messagebox.showerror("Chybička", f"Soubor `{self.FileInput.value}` neexistuje")
        except ZrudaException:
            messagebox.showerror("Jsi zrůda", "Ty zrůdo, proč dáváš mezeru do názvu souboru?")
        except ValueError:
            messagebox.showerror("Chybička", "Soubor obsahuje nejspíše špatně naformátovaná data")
        except Exception:
            messagebox.showerror("Chybička", "Něco se pokazilo, asi špatně parsnutej soubor nebo idk")
        
    def drawChart(self, x = [], y = []):
        pl.cla()
        pl.plot(
            x,
            y,
            linestyle=self.chart_curve_line_type.get(),
            marker=self.chart_curve_marker_type.get(),
            color=self.chart_curve_line_color.get(),
            mec=self.chart_curve_marker_color.get(),
            mfc=self.chart_curve_marker_color.get()
        )
        pl.xlabel(self.ChartAxisXInput.value)
        pl.ylabel(self.ChartAxisYInput.value)
        pl.title(self.ChartTitleInput.value)
        pl.legend(self.ChartLegendInput.value)
        pl.grid(self.chart_grid.get())
        pl.show()

    def quit(self, event=None):
        super().quit()


if __name__ == "__main__":
    app = Application("Grafenzí")
    app.mainloop()
