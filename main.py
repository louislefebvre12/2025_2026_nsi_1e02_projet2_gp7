
from tkinter import messagebox
from tkinter import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import tkinter as tk
from controller import Controller

if __name__ == "__main__":
    root = tk.Tk()
    app = Controller(root)
    root.mainloop()






