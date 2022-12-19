from math import *

#1
#try:
#    nimi=input("Sisestage oma nimi ")

#    if nimi.upper()=="JUKU":
#        print("Lähme kinno")
#        vanus=int(input("Kui vana sa oled? "))
#        if vanus<=0 or vanus>100:
#            print("viga andmetega")
#        elif vanus<6:
#            print("Tasuta")
#        elif vanus>=6 and vanus<=14:
#            print("Lapse pilet")
#        elif vanus>=15 and vanus<65:
#            print("täispilet")
#        elif vanus>=65:
#            print("sooduspilet")
#    else:0
#        print("Otsime Juku")
#except:
#    print("Vale Andmetüüp")

#2
#nimi1=input("Mis sinu nimi on? ")
#nimi2=input("Mis sinu nimi on? ")
#if nimi1.isalpha()==True and nimi2.isalpha():
#    if nimi1.lower()==("maxim") and nimi2.lower()=="martin":
#        print(nimi1,',',nimi2,"Te olete täna lauanaabrid")
#    else:
#        print("")
#else:
#    print("Vale Andmetüüp")

#3
#try:
#    a=float(input("Sisestage seina pikkus "))
#    b=float(input("Sisestage seina laius "))
#except:
#    print("Error")
#if a<=0 and b<=0:
#    print("Error")
#try:
#    kusimus=float(input("Kas soovite renoveerida? 0-ei, 1-jah => \n"))
#except:
#    print("Vale Andmetüüp")
#if kusimus==1:
#    k=float(input("Kui palju on ruutmeeter? "))
#    c=float(input("Kui palju põrandavahetus maksab? "))
#    if k<0 and c<0:
#        print("Error")
#    else:
#        S=print("See läheb t eile maksma",a*b)
#        print("Head aega!")
#else:
#    print("Head aega!")

#4
try:
    hind=float(input("Mis on hind?"))
    if hind>700:
        print("sul on soodus 30%",hind-hind*0.3)
    else:
        print(hind)
except:
    print("Error")

#5
