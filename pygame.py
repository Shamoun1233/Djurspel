import time
import random

print("Hej, detta är ett spel där du ska gissa djuret.")
print("REGLER: får du fel så dras det av en chans av de tio chanserna du har,")
print("om du gissar rätt bokstav får du en notis som meddelar dig om det.")
print("UPPDATERINGAR: Spelet uppdateras snart, en annan kategori också kanske")
print("kommer ut. Så var aktiva för att inte missa något.")
print("Lycka till!")

h = ("h")

u = ("u")

n = ("n")

d = ("d")


chanser = 10
poäng = 0

while True:
    fråga = str(input("Vilken bokstav gissar du på?"))
    if fråga == h:
        print("du har gissat rätt bokstav!")
        print("rätt bokstav: H")
        poäng += 1
    if fråga == u:
        print("du har gissat rätt bokstav!")
        print("rätt bokstav: U")
        poäng += 1
    if fråga == n:
        print("du har gissat rätt bokstav!")
        print("rätt bokstav: N")
        poäng += 1
    if fråga == d:
        print("du har gissat rätt bokstav!")
        print("rätt bokstav: D")
        poäng += 1
    if fråga not in ("h", "u", "n", "d"):
        print("Du har gissat fel! Försök igen")
        chanser -= 1  # Fix: -= instead of =-


    if poäng == 4:
        print("Du har gissat alla bokstäver rätt! djuret var hund")
        
        time.sleep(5)
        break    
    
    
    if chanser == 0:
        print("Du har inga chanser kvar..")
        
        time.sleep(5)
        break