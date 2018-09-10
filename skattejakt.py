# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 21:12:59 2018

@author: krisg
"""

import time
import random 

trekknr = 0
seier = False
spiller = 13
skatterute = random.randint(1,25)
poeng = 100
liv = 3

def Rutenett():
    print("")
    print("1   -  2   -  3   -  4   -  5")
    print("6   -  7   -  8   -  9   -  10")
    print("11  -  12  -  13  -  14  -  15")
    print("16  -  17  -  18  -  19  -  20")
    print("21  -  22  -  23  -  24  -  25")

def Trekk():
    global spiller
    global trekknr
    global seier
    global poeng
    global liv 
    
    trekknr+=1
    
    
    print("")
    print("")
    print("Du befinner deg i rute", spiller,". Hva vil du gjøre? opp/ned/høyre/venstre/grave")
    Rutenett()
    valg = input("")

    if valg == "opp" or valg =="Opp" or valg=="OPP":
        if spiller >= 6:
            time.sleep(2)
            spiller-=5
            print("Du er nå i rute", spiller)
            print("")
            time.sleep(2)
        else:
            time.sleep(2)
            print("Opp er ikke mulig")
            trekknr-=1
    elif valg=="NED" or valg=="ned" or valg=="Ned":
        if spiller < 21:
            time.sleep(2)
            spiller+=5
            print("Du er nå i rute", spiller)
            print("")
            time.sleep(2)
        else:
            time.sleep(2)
            print("Ned er ikke mulig")
            trekknr-=1
    elif valg == "høyre" or valg =="Høyre" or valg=="HØYRE":
        if spiller != 5 or spiller != 10 or spiller != 15 or spiller != 20 or spiller != 25:
            time.sleep(2)
            spiller+=1
            print("Du er nå i rute", spiller)
            print("")
            time.sleep(2)
        else:
            time.sleep(2)
            print("Høyre er ikke mulig")
            trekknr-=1
    elif valg=="Venstre" or valg=="VENSTRE" or valg=="venstre":
        if spiller != 1 or spiller != 6 or spiller != 11 or spiller != 16 or spiller != 21:
            time.sleep(2)
            spiller-=1
            print("Du er nå i rute", spiller)
            print("")
            time.sleep(2)
        else:
            time.sleep(2)
            print("Venstre er ikke mulig")
            trekknr-=1
    elif valg=="grave" or valg=="GRAVE" or valg=="Grave":
        if spiller == skatterute:
            time.sleep(2)
            print("DU VANT!!! SKATTEN VAR I RUTE", skatterute)
            seier = True
            poeng+=100
        else:
            time.sleep(2)
            liv -=1
            print("")
            print("Du gravde i feil rute... Du har", liv, "sjanser igjen...")
            if liv == 0:
                print("Du har ingen sjanser igjen... Du er død...")
                seier = True
            time.sleep(2)
    poeng-=10
    

"Hint"
global plasseringshint
global figurhint
global kolonnehint
global rekkehint

if skatterute == 1 or skatterute == 5 or skatterute == 21 or skatterute == 25:
    plasseringshint = "Skatten grenser til 2 ruter..."
elif skatterute == 2 or skatterute ==3 or skatterute ==4 or skatterute ==6 or skatterute ==11 or skatterute ==16 or skatterute ==10 or skatterute ==15 or skatterute ==20 or skatterute ==22 or skatterute ==23 or skatterute ==24:
    plasseringshint = "Skatten grenser til 3 ruter..."
else:
    plasseringshint = "Skatten grenser til 4 ruter..."
    
if skatterute == 1 or skatterute ==3 or skatterute ==5 or skatterute ==7 or skatterute ==9 or skatterute ==11 or skatterute ==13 or skatterute ==9 or skatterute ==15 or skatterute ==17 or skatterute ==19 or skatterute ==21 or skatterute ==23 or skatterute ==25:
    tallhint = "Skatten ligger i et tall som får 0.5 i rest når det heltalldivideres ..."
else:
    tallhint = "Skatten ligger i et tall som blir et heltall når det deles på det eneste primtallet som ikke er et oddetall..."

if skatterute == 1 or skatterute ==2 or skatterute ==3 or skatterute ==4 or skatterute ==5:
    radhint = "Skatten ligger i 5!..."
elif skatterute == 6 or skatterute ==7 or skatterute ==8 or skatterute ==9 or skatterute ==10:
    radhint = "Skatten ligger i tidsrommet når man står opp på hverdager..." 
elif skatterute == 11 or skatterute ==12 or skatterute ==13 or skatterute ==14 or skatterute ==15:
    radhint = "Skatten ligger mellom himmel og jord..." 
elif skatterute == 21 or skatterute ==22 or skatterute ==23 or skatterute ==24 or skatterute ==25:
    radhint = "Skatten ligger i hamburgerbrødet..." 
else:
    radhint = "Skatten ligger i stratosfæren..."

print("")
print("")
print("")
print("VELKOMMEN TIL SKATTEJAKTEN!!!")
print("")
time.sleep(2)
print("ER DU KLAR??? ja/nei")
print("")
time.sleep(3)
 
while True:
    ja=input("")
    if ja == "ja" or ja == "JA" or ja == "Ja":
        print("")
        time.sleep(2)
        print("DA BEGYNNER VI!")
        time.sleep(2)
        break
    else:
        print("")
        print("Det er ikke riktig innstilling")
           
time.sleep(4)  
print("")
print("")      
print("REGLER:")
print("Du blir plassert i en rute og må finne ruten med skatten i, ved bruk av ulike hint...")
print("Du står på en 5 x 5 rutenett, 1 - 25, og ved hver rute får man valget om å bevege seg til en av rutene som er ved siden av eller om å grave i ruten du befinner deg på...") 
print("Man får ett hint etter hvert trekk, men jo flere hint man får, jo færre poeng får man...")
print("Bruk færrest trekk og få den høyeste poengsummen...")
print("Du har 3 sjanser på å grave og finne skatten...")
print("") 
print("SKJØNNER DU??? ja/nei")

while True:
    regler=input("")
    if regler == "ja" or regler == "JA" or regler == "Ja":
        print("")
        time.sleep(2)
        print("LA SKATTEJAKTEN BEGYNNE!!!")
        time.sleep(5)
        break
    else:
        print("")
        print("Du får lese dem igjen...")

print("---------------------------------------------------------------------")
print("Ditt første hint er:", radhint)
print("")
print("Hvor vil du starte? Velg ett tall mellom 1 og 25")
print("")
Rutenett()
start=int(input(""))
spiller=start
        
while True:
    if seier == True:
        print("Du brukte", trekknr, "trekk")
        print("Du fikk", poeng, "poeng")
        break
    else:
        if trekknr == 1:
            print("")
            print("Ditt andre hint er:", tallhint)
        elif trekknr == 2:
            print("")
            print("Ditt tredje hint er:", plasseringshint)
        Trekk()
        
