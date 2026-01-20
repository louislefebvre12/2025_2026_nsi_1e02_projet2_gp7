from tkinter import *

fenetre = Tk()
fenetre.geometry("1000x600")
fenetre.title("Graphique du baccalauréat")

label = Label(fenetre,text="Courbe des garçons en fonction des filles",font=('Arial',20,'bold'))
label.place(x=235,y=560)

def clique():
    print("Mange")

bouton = Button(fenetre,text='Master Poulet')
bouton.config(command=clique)
bouton.pack()



fenetre.mainloop()