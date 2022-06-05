def open():
    #Ismétel (ha elrontja a felhasználó akkor is úrja próbálhatja)
    while True:
        megold1 = input("Megoldás: ")
        #Ha sikerült eltalálnia akkor tovább jut
        if megold1 == "auto" or megold1 == "Auto" or megold1 == "autó" or megold1 == "Autó" or megold1 == "kocsi" or megold1 == "Kocsi":
            print()
            print()
            code1 = random.randint(1,3)
            print( code1 )    
            break
        
        else:
            print()
            print()
            print()
            print()
