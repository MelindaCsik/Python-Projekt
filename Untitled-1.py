from tkinter import TOP, Button
from tkinter.tix import Tk
from turtle import left, right


def pitagorasz():
   print("helló")


#----CSOPORT----
#A gomb csoportjai amivel később dolgozhatunk
root = Tk()


#----GOMBOK----
button1 = Button(root, text="Szekrény", command = pitagorasz)
#Itt a gomb kinézeti beállításai
button1.config(font = ("Ink Free", 25, "bold"))
button1.config(bg = "#787878")
button1.config(fg = "#ffffff")
#A gomb elhelyezkedése
button1.pack(side = TOP)

button2 = Button(root, text="Szekrény", command = )
#Itt a gomb kinézeti beállításai
button2.config(font = ("Ink Free", 25, "bold"))
button2.config(bg = "#787878")
button2.config(fg = "#ffffff")
#A gomb elhelyezkedése
button2.pack(side = TOP)

button3 = Button(root, text="Szekrény", command = )
#Itt a gomb kinézeti beállításai
button3.config(font = ("Ink Free", 25, "bold"))
button3.config(bg = "#787878")
button3.config(fg = "#ffffff")
#A gomb elhelyezkedése
button3.pack(side = TOP)

button4 = Button(root, text="Szekrény", command = )
#Itt a gomb kinézeti beállításai
button4.config(font = ("Ink Free", 25, "bold"))
button4.config(bg = "#787878")
button4.config(fg = "#ffffff")
#A gomb elhelyezkedése
button4.pack(side = TOP)

button5 = Button(root, text="Szekrény", command = )
#Itt a gomb kinézeti beállításai
button5.config(font = ("Ink Free", 25, "bold"))
button1.config(bg = "#787878")
button5.config(fg = "#ffffff")
#A gomb elhelyezkedése
button5.pack(side = TOP)


#----MEGJELENÍTÉS----   
#Megjeleniti a gombokat/gombot   
root.mainloop()