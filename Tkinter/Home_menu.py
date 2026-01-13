from tkinter import * 

root = Tk()

photo = photoimage = PhotoImage(file = "cartedep.png")

def click():
    print("Le bouton a été cliqué")

button = Button(root, text = "Commencer",
                command = click,
                compound='bottom',)


my_label = Label (root, text = "Bienvenue", font = ("Arial", 24, "bold"), fg = "White", bg = "black", \
                  relief = RAISED, bd = 10, padx= 20, pady=20, image=photo, compound = 'bottom')
# my_label.pack() ou my_label.place(x=0, y=0)

button.pack()

my_label.pack()

root.mainloop()


