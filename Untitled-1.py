from tkinter import TOP, Button
from tkinter.tix import Tk
from turtle import left, right


def pitagorasz():
   print("helló")

#----CSOPORT----
#A gomb csoportjai amivel később dolgozhatunk
root = Tk()

button1 = Button(root, text="Szekrény", command = pitagorasz)
#Itt a gomb kinézeti beállításai
button1.config(font = ("Ink Free", 25, "bold"))
button1.config(bg = "#787878")
button1.config(fg = "#ffffff")
#A gomb elhelyezkedése
button1.pack(side = TOP)
    
#----MEGJELENÍTÉS----   
#Megjeleniti a gombokat/gombot   
root.mainloop()