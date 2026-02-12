
from tkinter import messagebox
from tkinter import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from model import Model
from view import MainView
from window1 import Window1
from window2 import Window2
from window3 import Window3


class Controller:
    def __init__(self, root):
        self.model = Model()
        self.view = MainView(root, self)

    def open_window1(self):
        Window1()

    def open_window2(self):
        Window2()

    def open_window3(self):
        Window3()

