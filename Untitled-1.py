from tkinter import LEFT, RIGHT, TOP, Button
from tkinter.tix import Tk
from turtle import right

#a gombok programjai
def pitagorasz():
    
    #Maga a gomba írt szöveget és a command amit tovább küld és a beírt feladatát elvégzi
    button1p = Button(pit, text="átfogó", command = atfogo)
    #Itt a gomb kinézeti beállításai
    button1p.config(font = ("Ink Free", 25, "bold"))
    button1p.config(bg = "#787878")
    button1p.config(fg = "#ffffff")
    #A gomb elhelyezkedése
    button1p.pack(side = LEFT)
    
    #Maga a gomba írt szöveget és a command amit tovább küld és a beírt feladatát elvégzi
    button2p = Button(pit, text="befogó", command = befogo)
    #Itt a gomb kinézeti beállításai
    button2p.config(font = ("Ink Free", 25, "bold"))
    button2p.config(bg = "#787878")
    button2p.config(fg = "#ffffff")
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
    button1t.pack(side = LEFT)
    
    #Maga a gomba írt szöveget és a command amit tovább küld és a beírt feladatát elvégzi
    button2t = Button(root, text="négyzet", command = negyzet)
    #Itt a gomb kinézeti beállításai
    button2t.config(font = ("Ink Free", 25, "bold"))
    button2t.config(bg = "#787878")
    button2t.config(fg = "#ffffff")
    #A gomb elhelyezkedése
    button2t.pack(side = TOP)
    
    #Maga a gomba írt szöveget és a command amit tovább küld és a beírt feladatát elvégzi
    button3t = Button(root, text="téglalap", command = tegla)
    #Itt a gomb kinézeti beállításai
    button3t.config(font = ("Ink Free", 25, "bold"))
    button3t.config(bg = "#787878")
    button3t.config(fg = "#ffffff")
    #A gomb elhelyezkedése
    button3t.pack(side = RIGHT)

def tegla():
 print("helló")
 
def negyzet():
    print("helló")

def haromszog():
     print("helló")
 
def kerulet():
    print("Helló")

def egyenlet():
    print("Helló")

def szazalek():
    print("Helló")

def alap():
    #Maga a gomba írt szöveget és a command amit tovább küld és a beírt feladatát elvégzi
    button1a = Button(root, text="Összeadás", command = add)
    #Itt a gomb kinézeti beállításai
    button1a.config(font = ("Ink Free", 25, "bold"))
    button1a.config(bg = "#787878")
    button1a.config(fg = "#ffffff")
    #A gomb elhelyezkedése
    button1a.pack(side = LEFT)
    
    #Maga a gomba írt szöveget és a command amit tovább küld és a beírt feladatát elvégzi
    button1s = Button(root, text="Kivonás", command = von)
    #Itt a gomb kinézeti beállításai
    button1s.config(font = ("Ink Free", 25, "bold"))
    button1s.config(bg = "#787878")
    button1s.config(fg = "#ffffff")
    #A gomb elhelyezkedése
    button1s.pack(side = RIGHT)
    
    #Maga a gomba írt szöveget és a command amit tovább küld és a beírt feladatát elvégzi
    button1s = Button(root, text="Szorzás", command = szor)
    #Itt a gomb kinézeti beállításai
    button1s.config(font = ("Ink Free", 25, "bold"))
    button1s.config(bg = "#787878")
    button1s.config(fg = "#ffffff")
    #A gomb elhelyezkedése
    button1s.pack(side = LEFT)
    
    #Maga a gomba írt szöveget és a command amit tovább küld és a beírt feladatát elvégzi
    button1 = Button(root, text="Osztás", command = oszt)
    #Itt a gomb kinézeti beállításai
    button1s.config(font = ("Ink Free", 25, "bold"))
    button1s.config(bg = "#787878")
    button1s.config(fg = "#ffffff")
    #A gomb elhelyezkedése
    button1s.pack(side = RIGHT)

def add():
    numm1 = 0
    num1 = 0
    #bekérem az adatokat
    fut1 = int(input("Hány számot szeretne összeadni: "))
    #lefuttatom annyiszor amennyiszer kérte a felhasználó és a végén kiiratom
    while True:
        add = int(input("Összeadandó szám: "))
        num1 = num1 + add
        numm2 = numm2 + 1
        if fut1 == numm1:
            print(num1)
            break
    
def von():
    numm = 0
    #bekérem az adatokat
    fut2 = int(input("Hány számot szeretne kivonni: "))
    num2 = int(input("Milyen számból szeretne kivonni: "))
    #lefuttatom annyiszor amennyiszer kérte a felhasználó és a végén kiiratom
    while True:
        von = int(input("Kivonandó szám: "))
        num2 = num2 - von
        numm = numm + 1
        if fut2 == numm:
            print(num2)
            break


def szor():
    #bekérjük az adatokat
    szam1 = int(input("Írja be az első számot:"))
    szam2 = int(input("Írja be a második számot:"))
    
    #végrehajtjuk a kért műveletet
    eredmeny1 = szam1 * szam2
    print(eredmeny1)


def oszt():
    #bekérjük a az adatokat
    szam3 = int(input("Melyik számot szerné elosztani:"))
    szam4 = int(input("Melyik számmal szertné elosztani:"))
   
    #végrehajtjuk a kért műveletet
    eredmeny2 = szam3 / szam4
    print(eredmeny2)


#----CSOPORT----
#A gomb csoportjai amivel később dolgozhatunk
root = Tk()
pit = Tk()


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

#Maga a gomba írt szöveget és a command amit tovább küld és a beírt feladatát elvégzi
button6 = Button(root, text="Alap műveletek", command = alap)
#Itt a gomb kinézeti beállításai
button6.config(font = ("Ink Free", 25, "bold"))
button6.config(bg = "#787878")
button6.config(fg = "#ffffff")
#A gomb elhelyezkedése
button6.pack(side = TOP)


#----MEGJELENÍTÉS----   
#Megjeleniti a gombokat/gombot   
root.mainloop()