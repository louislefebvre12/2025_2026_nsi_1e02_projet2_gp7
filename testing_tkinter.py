from tkinter import * 

window = Tk()

label = Label(window, text = "Text", font = ('Arial' , 40, 'bold'), fg = "#00FF00")

#label.pack() ou label.place(x = 0 , y = 0)
label.pack()

window.mainloop()   