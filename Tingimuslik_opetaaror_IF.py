from math import *
import datetime
from random import *
from time import sleep
#21/12/22
#n=int(input("Mitu toa korteris? "))
#for i in range(1,n+1,1):
#    t=float(input(f"{i}. toa Temperatuur: "))
#    if t>18:
#        print("Soe(Teplo)")
#    else:
#        print("Külm(Holodno)")

#6
#try:
#    p=k=l=0
#    kogus=randint(1,20)
#    print(kogus)
#    for i in range(1,kogus+1,1):
#        a=randint(1,20)
#        if a<=0:
#            print("Error")
#        else:
#            if a<=165:
#                print("Lühike")
#                l+=1
#            elif a>165 and a<180:
#                print("Keskmine")
#                k+=1
#            elif a>=180:
#                print("Pikk")
#                p+=1
#    print("Pikka kasvu",p,'inimes')
#    print("Keskmine kasvu",k,'inimes')
#    print("Lühike kasvu",l,'inimes')
#except:
#    print("Vale Andmetüüp")


#p=k=l=0
#kogus=randint(1,20)
#print(kogus)
#while kogus>0:
#        kogus-=1
#        sleep(1)
#        a=randint(56,256)
#        if a<=0:
#            print("Error")
#        else:
#            if a<=165:
#                print("Lühike")
#                l+=1
#            elif a>165 and a<180:
#                print("Keskmine")
#                k+=1
#            elif a>=180:
#                print("Pikk")
#                p+=1
#print("Pikka kasvu",p,'inimes')
#print("Keskmine kasvu",k,'inimes')
#print("Lühike kasvu",l,'inimes')



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
#try:
#    hind=float(input("Mis on hind?"))
#    if hind>700:
#        print("sul on soodus 30%",hind-hind*0.3)
#    else:
#        print(hind)
#except:
#    print("Error")

#5
#try:
#    a=float(input("mis on teie toatemperatuur: "))
#    if a>=18:
#        print("teie toatemperatuur on keskmisest kõrgem, 18 kraadi celsiuse järgi.")
#    else:
#        print("teie toatemperatuur on keskmisest madalam, 18 kraadi celsiuse järgi.")
#except:
#    print("vale andmetüüp")

#6
#try:
#    a=float(input("Mis on su pikkus?(Sentimeetrites): "))
#    if a<=0:
#        print("Error")
#    else:
#        if a<=165:
#            print("Teie pikkus on madal")
#        elif a>165 and a<180:
#            print("Teie pikkus on keskmine")
#        elif a>=180:
#            print("Teie pikkus on kõrge")
#except:
#    print("Vale Andmetüüp")

#7
#try:
#    a=float(input("Mis soost te olete? 0-naine 1-mees => \n"))
#    if a==0:
#        b=float(input("Kui pikk te olete? "))
#        if b<0:
#            print("Error")
#        elif b<=150:
#            print("Sa oled madal")
#        elif b>=150 and b<=160:
#            print("Te olete keskmist kasvu")
#        elif b>160 and b<=200:
#            print("Te olete pikk")
#        elif b>200:
#            print("Te olete illuminaat")
#    else:
#         print("Kes te olete?")
#    if a==1:
#        b=float(input("Kui pikk te olete? "))
#        if b<0:
#            print("Error")
#        elif b<=150:
#            print("Sa oled madal")
#        elif b>=150 and b<=160:
#            print("Te olete keskmist kasvu")
#        elif b>160 and b<=200:
#            print("Te olete pikk")
#        elif b>200:
#            print("Te olete illuminaat")
#except:
#    print("Value Error")

#8
#try:
#    a=int(input("Kas soovite piima osta?(jah-1 või ei-0): "))
#    b=int(input("Kas soovite saia osta?(jah-1 või ei-0): "))
#    c=int(input("Kas soovite leiba osta?(jah-1 või ei-0): "))
#    if a<0 and b<0 and c<0:
#        print("Error")
#    if a==1 and b==0 and c==0:
#        piim=0.79
#        sai=0
#        leib=0
#        S=piim+sai+leib
#        print("Kõik ostetud asjad maksavad",S)
#    elif a==0 and b==1 and c==0:
#        piim=0
#        sai=0.8
#        leib=0
#        P=piim+sai+leib
#        print("Kõik ostetud asjad maksavad",P)
#    elif a==0 and b==0 and c==1:
#        piim=0
#        sai=0
#        leib=0.8
#        F=piim+sai+leib
#        print("Kõik ostetud asjad maksavad",F)
#    elif a==1 and b==1 and c==0:
#        piim=0.79
#        sai=0.8
#        leib=0
#        L=piim+sai+leib
#        print("Kõik ostetud asjad maksavad",L)
#    elif a==0 and b==1 and c==1:
#        piim=0
#        sai=0.8
#        leib=0.8
#        O=piim+sai+leib
#        print("Kõik ostetud asjad maksavad",O)
#    elif a==1 and b==0 and c==1:
#        piim=0.79
#        sai=0
#        leib=0.8
#        U=piim+sai+leib
#        print("Kõik ostetud asjad maksavad",U)
#    elif a==1 and b==1 and c==1:
#        piim=0.79
#        sai=0.8
#        leib=0.8
#        A=piim+sai+leib
#        print("Kõik ostetud asjad maksavad",A)
#except:
#    print("Vale Andmetüüp")


#9
while True:
    try:
        a=float(input("Utle pool a "))
        b=float(input("Utle pool b "))
        if a==b:
            print("See on ruut")
            break
        elif a<0 and b<0:
            print("Error")
        else:
            print("See ei ole ruut")
    except:
        print("Value Error")


#10
#try:
#    a=float(input("1 number "))
#    b=float(input("1 number "))
#    c=input("mis märk sa oled +-*/ \n ")
#    if c==("+"):
#        print(a+b)
#    elif c==("-"):
#        print(a-b)
#    elif c==("*"):
#        print(a*b)
#    elif c==("/"):
#        if b==0:
#            print("Väiksem kui 0")
#        else:
#            print(a/b)
#except:
#    print("Value Error")

#11
#now = datetime.datetime.now()
#try:
#    a=int(input("Sisesta sünniaasta. "))
#except:
#    print("Value Error")
#b=int(now.year)
#c=int(b-a)
#print(c)
#f=c%5
#if f==0:
#    print("teil on juubel")
#else:
#    print("Kui kaju")

#12
#try:
#    a=float(input("sisesta toote hind "))
#    if a<=10:
#        print("sul on soodus 10%",a-a*0.1)
#    elif a>10:
#        print("sul on soodus 20%",a-a*0.2)
#except:
#    print("Value Error")

#13
#try:
#    a=int(input("Kas sa oled mees?(jah-1 või ei-0) \n"))
#    if a==1:
#        b=int(input("Kui vana sa oled? "))
#        if b>=16 and b<=18:
#            print("sa sobid")
#    else:
#        print("sa oled naine sest, et sa ei sobi")
#except:
#    print("Value Error")