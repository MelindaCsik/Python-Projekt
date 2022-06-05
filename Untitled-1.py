
from tkinter.tix import Tk
from turtle import left, right


def pitagorasz():
    #megkérdi a felhaSZNÁLÓT hogy átfogót vagy befogót akar számolni
    button = Button(pitagorasz, text="Szekrény", command = atfogo)
    #Itt a gomb kinézeti beállításai
    button.config(font = ("Ink Free", 25, "bold"))
    button.config(bg = "#787878")
    button.config(fg = "#ffffff")
    #A gomb elhelyezkedése
    button.pack(side = left)
    button = Button(pitagorasz, text="Szekrény", command = befogo)
    #Itt a gomb kinézeti beállításai
    button.config(font = ("Ink Free", 25, "bold"))
    button.config(bg = "#787878")
    button.config(fg = "#ffffff")
    #A gomb elhelyezkedése
    button.pack(side = right)

#----CSOPORT----
#A gomb csoportjai amivel később dolgozhatunk
root = Tk  

button1 = Button(root, text="Szekrény", command = pitagorasz)
#Itt a gomb kinézeti beállításai
button1.config(font = ("Ink Free", 25, "bold"))
button1.config(bg = "#787878")
button1.config(fg = "#ffffff")
#A gomb elhelyezkedése
button1.pack(side = right)
    
#----MEGJELENÍTÉS----   
#Megjeleniti a gombokat/gombot   
root.mainloop()