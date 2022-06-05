from tkinter import LEFT, RIGHT, TOP, Button
from tkinter.tix import Tk


def pitagorasz():
    #Maga a gomba írt szöveget és a command amit tovább küld és a beírt feladatát elvégzi
    button1p = Button(root, text="atfogo", command = atfogo)
    #Itt a gomb kinézeti beállításai
    button1p.config(font = ("Ink Free", 25, "bold"))
    button1p.config(bg = "#787878")
    button1p.config(fg = "#ffffff")
    #A gomb elhelyezkedése
    button1.pack(side = LEFT)
    
    #Maga a gomba írt szöveget és a command amit tovább küld és a beírt feladatát elvégzi
    button2p = Button(root, text="befogo", command = befogo)
    #Itt a gomb kinézeti beállításai
    button2p.config(font = ("Ink Free", 25, "bold"))
    button2p.config(bg = "#787878")
    button1.config(fg = "#ffffff")
    #A gomb elhelyezkedése
    button2p.pack(side = RIGHT)
    
def atfogo():
    print("Helló")

def befogo():
    print("Helló")
    
    
def terulet():
    #Maga a gomba írt szöveget és a command amit tovább küld és a beírt feladatát elvégzi
    button1t = Button(root, text="háromszög", command = haromszog)
    #Itt a gomb kinézeti beállításai
    button1t.config(font = ("Ink Free", 25, "bold"))
    button1t.config(bg = "#787878")
    button1t.config(fg = "#ffffff")
    #A gomb elhelyezkedése
    button1t.pack(side = RIGHT)
    
    #Maga a gomba írt szöveget és a command amit tovább küld és a beírt feladatát elvégzi
    button2t = Button(root, text="négyzet", command = negyzet)
    #Itt a gomb kinézeti beállításai
    button2t.config(font = ("Ink Free", 25, "bold"))
    button2t.config(bg = "#787878")
    button2t.config(fg = "#ffffff")
    #A gomb elhelyezkedése
    button2t.pack(side = RIGHT)
    
    #Maga a gomba írt szöveget és a command amit tovább küld és a beírt feladatát elvégzi
    button3t = Button(root, text="téglalap", command = tegla)
    #Itt a gomb kinézeti beállításai
    button3t.config(font = ("Ink Free", 25, "bold"))
    button3t.config(bg = "#787878")
    button3t.config(fg = "#ffffff")
    #A gomb elhelyezkedése
    button3t.pack(side = RIGHT)

def kerulet():
    print("Helló")

def egyenlet():
    print("Helló")

def szazalek():
    print("Helló")


#----CSOPORT----
#A gomb csoportjai amivel később dolgozhatunk
root = Tk()


#----GOMBOK----
#Maga a gomba írt szöveget és a command amit tovább küld és a beírt feladatát elvégzi
button1 = Button(root, text="Pitagorasz", command = pitagorasz)
#Itt a gomb kinézeti beállításai
button1.config(font = ("Ink Free", 25, "bold"))
button1.config(bg = "#787878")
button1.config(fg = "#ffffff")
#A gomb elhelyezkedése
button1.pack(side = TOP)

#Maga a gomba írt szöveget és a command amit tovább küld és a beírt feladatát elvégzi
button2 = Button(root, text="Terület", command = terulet)
#Itt a gomb kinézeti beállításai
button2.config(font = ("Ink Free", 25, "bold"))
button2.config(bg = "#787878")
button2.config(fg = "#ffffff")
#A gomb elhelyezkedése
button2.pack(side = TOP)

#Maga a gomba írt szöveget és a command amit tovább küld és a beírt feladatát elvégzi
button3 = Button(root, text="Kerület", command = kerulet)
#Itt a gomb kinézeti beállításai
button3.config(font = ("Ink Free", 25, "bold"))
button3.config(bg = "#787878")
button3.config(fg = "#ffffff")
#A gomb elhelyezkedése
button3.pack(side = TOP)

#Maga a gomba írt szöveget és a command amit tovább küld és a beírt feladatát elvégzi
button4 = Button(root, text="Másodfokú egyenlet", command = egyenlet)
#Itt a gomb kinézeti beállításai
button4.config(font = ("Ink Free", 25, "bold"))
button4.config(bg = "#787878")
button4.config(fg = "#ffffff")
#A gomb elhelyezkedése
button4.pack(side = TOP)

#Maga a gomba írt szöveget és a command amit tovább küld és a beírt feladatát elvégzi
button5 = Button(root, text="Százalékszámítás", command = szazalek)
#Itt a gomb kinézeti beállításai
button5.config(font = ("Ink Free", 25, "bold"))
button5.config(bg = "#787878")
button5.config(fg = "#ffffff")
#A gomb elhelyezkedése
button5.pack(side = TOP)


#----MEGJELENÍTÉS----   
#Megjeleniti a gombokat/gombot   
root.mainloop()