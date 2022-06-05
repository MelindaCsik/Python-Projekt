from tkinter import LEFT, RIGHT, TOP, Button
from tkinter.tix import Tk
from turtle import right

#a gombok programjai
def pitagorasz():
    
    #Maga a gomba írt szöveget és a command amit tovább küld és a beírt feladatát elvégzi
    button1p = Button(pit, text="átfogó", command = atfogo)
    #Itt a gomb kinézeti beállításai
    button1p.config(font = ("Ariel", 25, "bold"))
    button1p.config(bg = "#787878")
    button1p.config(fg = "#ffffff")
    #A gomb elhelyezkedése
    button1p.pack(side = LEFT)
    
    #Maga a gomba írt szöveget és a command amit tovább küld és a beírt feladatát elvégzi
    button2p = Button(pit, text="befogó", command = befogo)
    #Itt a gomb kinézeti beállításai
    button2p.config(font = ("Ariel", 25, "bold"))
    button2p.config(bg = "#787878")
    button2p.config(fg = "#ffffff")
    #A gomb elhelyezkedése
    button2p.pack(side = RIGHT)
    
def atfogo():
    a4 = int(input("Adja meg az ""\"a""\" szakaszt: "))
    b3 = int(input("Adja meg a ""\"b""\" szakaszt: "))
    cnegyzet = (a4**2)+(b3**2)
    print(cnegyzet**0.5)

def befogo():
    c4 = int(input("Adja meg az ""\"c""\" szakaszt: "))
    aorb = int(input("Adja meg az ""\"a""\" vagy a ""\"a""\" szakaszt: "))
    aorbnegyzet = (c4**2)-(aorb**2)
    print(aorbnegyzet**0.5)
    
    
def terulet():
    #Maga a gomba írt szöveget és a command amit tovább küld és a beírt feladatát elvégzi
    button1t = Button(ter, text="háromszög", command = haromszog)
    #Itt a gomb kinézeti beállításai
    button1t.config(font = ("Ariel", 25, "bold"))
    button1t.config(bg = "#787878")
    button1t.config(fg = "#ffffff")
    #A gomb elhelyezkedése
    button1t.pack(side = LEFT)
    
    #Maga a gomba írt szöveget és a command amit tovább küld és a beírt feladatát elvégzi
    button2t = Button(ter, text="négyzet", command = negyzet)
    #Itt a gomb kinézeti beállításai
    button2t.config(font = ("Ariel", 25, "bold"))
    button2t.config(bg = "#787878")
    button2t.config(fg = "#ffffff")
    #A gomb elhelyezkedése
    button2t.pack(side = TOP)
    
    #Maga a gomba írt szöveget és a command amit tovább küld és a beírt feladatát elvégzi
    button3t = Button(ter, text="téglalap", command = tegla)
    #Itt a gomb kinézeti beállításai
    button3t.config(font = ("Ariel", 25, "bold"))
    button3t.config(bg = "#787878")
    button3t.config(fg = "#ffffff")
    #A gomb elhelyezkedése
    button3t.pack(side = RIGHT)

def tegla():
    a3 = int(input("Adja meg az ""\"a""\" szakaszt: "))
    b2 = int(input("Adja meg a ""\"b""\" szakaszt: "))
    print(a3 + b2)
 
def negyzet():
    a2 = int(input("Adja meg az ""\"a""\" szakaszt: "))
    print(a2 * a2)

def haromszog():
    a1 = int(input("Adja meg az ""\"a""\" szakaszt: "))
    b1 = int(input("Adja meg a ""\"b""\" szakaszt: "))
    ab = 0
    ab = a1 + b1
    print(ab / 2)
    
 
def kerulet():
    #Maga a gomba írt szöveget és a command amit tovább küld és a beírt feladatát elvégzi
    button1tt = Button(ker, text="Háromszög", command = haromszogg)
    #Itt a gomb kinézeti beállításai
    button1tt.config(font = ("Ariel", 25, "bold"))
    button1tt.config(bg = "#787878")
    button1tt.config(fg = "#ffffff")
    #A gomb elhelyezkedése
    button1tt.pack(side = LEFT)
    
    #Maga a gomba írt szöveget és a command amit tovább küld és a beírt feladatát elvégzi
    button1z = Button(ker, text="Négyzet", command = negyzett)
    #Itt a gomb kinézeti beállításai
    button1z.config(font = ("Ariel", 25, "bold"))
    button1z.config(bg = "#787878")
    button1z.config(fg = "#ffffff")
    #A gomb elhelyezkedése
    button1z.pack(side = TOP)
    
    #Maga a gomba írt szöveget és a command amit tovább küld és a beírt feladatát elvégzi
    button1u = Button(ker, text="Téglalap", command = teglaa)
    #Itt a gomb kinézeti beállításai
    button1u.config(font = ("Ariel", 25, "bold"))
    button1u.config(bg = "#787878")
    button1u.config(fg = "#ffffff")
    #A gomb elhelyezkedése
    button1u.pack(side = RIGHT)

def haromszogg():
    aHk = int(input("Adja meg a háromszög ""\"a""\" oldalát:"))
    bHk = int(input("Adja meg a háromszög ""\"b""\" oldalát ugyanazzal a mértékegységgel amivel az ""\"a""\"-t:"))
    cHk = int(input("Adja meg a háromszög ""\"c""\" oldalát ugyanazzal a mértékegységgel amivel az ""\"a""\"-t és a ""\"b""\"-t :"))

    eredmenyHk = aHk + bHk + cHk
    print("A háromszög területe:" , eredmenyHk)

def negyzett():
    aNk = int(input("Adja meg a négyzet ""\"a""\" oldalát:"))

    eredmenyNk = 4 * aNk
    print("A négyzet kerülete:" , eredmenyNk)

def teglaa():
    aTk = int(input("Adja meg a téglalap ""\"a""\" oldalát:"))
    bTk = int(input("Adja meg a téglalap ""\"b""\" oldalát ugyanazzal a mértékegységgel amivel az ""\"a""\"-t:"))
    
    szamitasTk = aTk + bTk
    eredmenyTk = 2 * szamitasTk
    print("A téglalap kerület:" , eredmenyTk)


def egyenlet():
    a = int(input("Adja meg az ""\"a""\" értékét: "))
    b = int(input("Adja meg az ""\"b""\" értékét: "))
    c = int(input("Adja meg az ""\"c""\" értékét: "))
    negyzetalat = (b**2)-(4*a*c)
    print(negyzetalat)
    elagaz = negyzetalat**0.5
    egyut = (b-elagaz) / (2*a)
    ketut = (b+elagaz) / (2*a)
    print("első eset: ", egyut)
    print("második eset: ", ketut)
    
    

def szazalek():
    #bekérjük az adatokat
    eszam = int(input("Adja meg azt a számot aminek a százalékát kiszertnéd számítani:"))
    szszam = int(input("Adja meg a szám hány százalékát szeretné meg kapni:"))

    szamitas = eszam / 100
    eredmenySz = szszam * szamitas

    print(eszam, "a/az" , szszam, "százaléka" , eredmenySz)


def alap():
    #Maga a gomba írt szöveget és a command amit tovább küld és a beírt feladatát elvégzi
    button1a = Button(alapp, text="Összeadás", command = add)
    #Itt a gomb kinézeti beállításai
    button1a.config(font = ("Ariel", 25, "bold"))
    button1a.config(bg = "#787878")
    button1a.config(fg = "#ffffff")
    #A gomb elhelyezkedése
    button1a.pack(side = LEFT)
    
    #Maga a gomba írt szöveget és a command amit tovább küld és a beírt feladatát elvégzi
    button1s = Button(alapp, text="Kivonás", command = von)
    #Itt a gomb kinézeti beállításai
    button1s.config(font = ("Ariel", 25, "bold"))
    button1s.config(bg = "#787878")
    button1s.config(fg = "#ffffff")
    #A gomb elhelyezkedése
    button1s.pack(side = RIGHT)
    
    #Maga a gomba írt szöveget és a command amit tovább küld és a beírt feladatát elvégzi
    button1ss = Button(alapp, text="Szorzás", command = szor)
    #Itt a gomb kinézeti beállításai
    button1ss.config(font = ("Ariel", 25, "bold"))
    button1ss.config(bg = "#787878")
    button1ss.config(fg = "#ffffff")
    #A gomb elhelyezkedése
    button1ss.pack(side = LEFT)
    
    #Maga a gomba írt szöveget és a command amit tovább küld és a beírt feladatát elvégzi
    button1hh = Button(alapp, text="Osztás", command = oszt)
    #Itt a gomb kinézeti beállításai
    button1hh.config(font = ("Ariel", 25, "bold"))
    button1hh.config(bg = "#787878")
    button1hh.config(fg = "#ffffff")
    #A gomb elhelyezkedése
    button1hh.pack(side = TOP)

def add():
    numm1 = 0
    num1 = 0
    #bekérem az adatokat
    fut1 = int(input("Hány számot szeretne összeadni: "))
    #lefuttatom annyiszor amennyiszer kérte a felhasználó és a végén kiiratom
    while True:
        add = int(input("Összeadandó szám: "))
        num1 = num1 + add
        numm1 = numm1 + 1
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
alapp = Tk()
ter = Tk()
ker = Tk()

#----GOMBOK----
#Maga a gomba írt szöveget és a command amit tovább küld és a beírt feladatát elvégzi
button1 = Button(root, text="Pitagorasz", command = pitagorasz)
#Itt a gomb kinézeti beállításai
button1.config(font = ("Ariel", 25, "bold"))
button1.config(bg = "#787878")
button1.config(fg = "#ffffff")
#A gomb elhelyezkedése
button1.pack(side = TOP)

#Maga a gomba írt szöveget és a command amit tovább küld és a beírt feladatát elvégzi
button2 = Button(root, text="Terület", command = terulet)
#Itt a gomb kinézeti beállításai
button2.config(font = ("Ariel", 25, "bold"))
button2.config(bg = "#787878")
button2.config(fg = "#ffffff")
#A gomb elhelyezkedése
button2.pack(side = TOP)

#Maga a gomba írt szöveget és a command amit tovább küld és a beírt feladatát elvégzi
button3 = Button(root, text="Kerület", command = kerulet)
#Itt a gomb kinézeti beállításai
button3.config(font = ("Ariel", 25, "bold"))
button3.config(bg = "#787878")
button3.config(fg = "#ffffff")
#A gomb elhelyezkedése
button3.pack(side = TOP)

#Maga a gomba írt szöveget és a command amit tovább küld és a beírt feladatát elvégzi
button4 = Button(root, text="Másodfokú egyenlet", command = egyenlet)
#Itt a gomb kinézeti beállításai
button4.config(font = ("Ariel", 25, "bold"))
button4.config(bg = "#787878")
button4.config(fg = "#ffffff")
#A gomb elhelyezkedése
button4.pack(side = TOP)

#Maga a gomba írt szöveget és a command amit tovább küld és a beírt feladatát elvégzi
button5 = Button(root, text="Százalékszámítás", command = szazalek)
#Itt a gomb kinézeti beállításai
button5.config(font = ("Ariel", 25, "bold"))
button5.config(bg = "#787878")
button5.config(fg = "#ffffff")
#A gomb elhelyezkedése
button5.pack(side = TOP)

#Maga a gomba írt szöveget és a command amit tovább küld és a beírt feladatát elvégzi
button6 = Button(root, text="Alap műveletek", command = alap)
#Itt a gomb kinézeti beállításai
button6.config(font = ("Ariel", 25, "bold"))
button6.config(bg = "#787878")
button6.config(fg = "#ffffff")
#A gomb elhelyezkedése
button6.pack(side = TOP)


#----MEGJELENÍTÉS----   
#Megjeleniti a gombokat/gombot   
root.mainloop()