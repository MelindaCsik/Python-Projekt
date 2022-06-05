from tkinter import LEFT, RIGHT, TOP, Button
from tkinter.tix import Tk


def pitagorasz():
    #Maga a gomba írt szöveget és a command amit tovább küld és a beírt feladatát elvégzi
    button1 = Button(root, text="atfogo", command = atfogo)
    #Itt a gomb kinézeti beállításai
    button1.config(font = ("Ink Free", 25, "bold"))
    button1.config(bg = "#787878")
    button1.config(fg = "#ffffff")
    #A gomb elhelyezkedése
    button1.pack(side = LEFT)
    
    #Maga a gomba írt szöveget és a command amit tovább küld és a beírt feladatát elvégzi
    button1 = Button(root, text="befogo", command = befogo)
    #Itt a gomb kinézeti beállításai
    button1.config(font = ("Ink Free", 25, "bold"))
    button1.config(bg = "#787878")
    button1.config(fg = "#ffffff")
    #A gomb elhelyezkedése
    button1.pack(side = RIGHT)
    
def befogo():
    print("Helló")
    
def atfogo():
    print("Hellóó")
    
def terulet():
    #Maga a gomba írt szöveget és a command amit tovább küld és a beírt feladatát elvégzi
    button1 = Button(root, text="háromszög", command = haromszog)
    #Itt a gomb kinézeti beállításai
    button1.config(font = ("Ink Free", 25, "bold"))
    button1.config(bg = "#787878")
    button1.config(fg = "#ffffff")
    #A gomb elhelyezkedése
    button1.pack(side = RIGHT)
    
    #Maga a gomba írt szöveget és a command amit tovább küld és a beírt feladatát elvégzi
    button1 = Button(root, text="négyzet", command = negyzet)
    #Itt a gomb kinézeti beállításai
    button1.config(font = ("Ink Free", 25, "bold"))
    button1.config(bg = "#787878")
    button1.config(fg = "#ffffff")
    #A gomb elhelyezkedése
    button1.pack(side = RIGHT)
    
    #Maga a gomba írt szöveget és a command amit tovább küld és a beírt feladatát elvégzi
    button1 = Button(root, text="téglalap", command = tegla)
    #Itt a gomb kinézeti beállításai
    button1.config(font = ("Ink Free", 25, "bold"))
    button1.config(bg = "#787878")
    button1.config(fg = "#ffffff")
    #A gomb elhelyezkedése
    button1.pack(side = RIGHT)



#----CSOPORT----
#A gomb csoportjai amivel később dolgozhatunk
root = Tk()


#----GOMBOK----
#Maga a gomba írt szöveget és a command amit tovább küld és a beírt feladatát elvégzi
button1 = Button(root, text="pitagorasz", command = pitagorasz)
#Itt a gomb kinézeti beállításai
button1.config(font = ("Ink Free", 25, "bold"))
button1.config(bg = "#787878")
button1.config(fg = "#ffffff")
#A gomb elhelyezkedése
button1.pack(side = TOP)

#Maga a gomba írt szöveget és a command amit tovább küld és a beírt feladatát elvégzi
button2 = Button(root, text="Szekrény", command = terulet)
#Itt a gomb kinézeti beállításai
button2.config(font = ("Ink Free", 25, "bold"))
button2.config(bg = "#787878")
button2.config(fg = "#ffffff")
#A gomb elhelyezkedése
button2.pack(side = TOP)

#Maga a gomba írt szöveget és a command amit tovább küld és a beírt feladatát elvégzi
button3 = Button(root, text="Szekrény", command = kerulet)
#Itt a gomb kinézeti beállításai
button3.config(font = ("Ink Free", 25, "bold"))
button3.config(bg = "#787878")
button3.config(fg = "#ffffff")
#A gomb elhelyezkedése
button3.pack(side = TOP)

#Maga a gomba írt szöveget és a command amit tovább küld és a beírt feladatát elvégzi
button4 = Button(root, text="Szekrény", command = k)
#Itt a gomb kinézeti beállításai
button4.config(font = ("Ink Free", 25, "bold"))
button4.config(bg = "#787878")
button4.config(fg = "#ffffff")
#A gomb elhelyezkedése
button4.pack(side = TOP)

#Maga a gomba írt szöveget és a command amit tovább küld és a beírt feladatát elvégzi
button5 = Button(root, text="Szekrény", command = k)
#Itt a gomb kinézeti beállításai
button5.config(font = ("Ink Free", 25, "bold"))
button5.config(bg = "#787878")
button5.config(fg = "#ffffff")
#A gomb elhelyezkedése
button5.pack(side = TOP)


#----MEGJELENÍTÉS----   
#Megjeleniti a gombokat/gombot   
root.mainloop()