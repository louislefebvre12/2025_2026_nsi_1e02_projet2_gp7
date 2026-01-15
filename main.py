from tkinter import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class Testing : 
    def __init__(self, root):
        self._root = root 
        root.title('Test')

        self.plot_types = ['Linear Plot' , 'Bar Plot', 'Scatterer Plot']
        self.plot_type_var = StringVar ("Tata")  #StringVar(value =self.plot_type_var[0])
        plot_menu = OptionMenu(self.root , self.plot_type_var , command=self.update_plot)
        plot_menu.pack(padx= 10 , pady = 10)


        load_button = Button(self.root, text = 'Testeur', command = self.xlsx)
        load_button.pack(padx=10, pady = 10)



        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master = self.root)
        self.widget = self.canvas.get_tk_widget()
        self.widget.pack(padx = 10, pady = 10)

        self.df = None

    def load_xlsx(self) : 
        file.path = filedialog.askopenfilename()
        if file_path:
            self.df = pd.read_xlsx(file_path)
            self.update_plot()


    def update_plot(self, event = None) : 
        if self.df is not None :
            plot_type = self.plot_type_var.get()
            x = self.df.columns[0]
            y = self.df.columns[1]

            self.ax.clear()
            if plot_type == 'Line Plot' : 
                self.ax.plot(self.df[x], self.df[y], label = f'{y} en fonction de {x}') 
            elif plot_type == 'Bar Plot': 
                self.ax.bar(self.df[x], self.df[y], label = f'{y} en fonction de {x}')
            elif plot_type == 'Scatter  Plot' : 
                self.ax.scatter(self.df[x], self.df[y], label = f'{y} en fonction de {x}')

            self.ax.set_xlabel(x)
            self.ax.set_ylabel(y)
            self.ax.legend()
            self.canvas.draw()


if __name__ == '__main__' : 
    root = Tk()
    app = Testing(root)


















        
