#----------------------*Zadatak 1*--------------------------
def sumn(niz):
    i=0
    zbir=0
    for el in niz:
        i=i+1
        if i%2==0:
         zbir=zbir+el
    return zbir

#Glavni program
niz=input("Unesite niz brojeva, elemente odvajati zarezom  ")
sumapr=sumn(niz)
print "Suma parnih elemenata niza: =", sumapr

#----------------------*Zadatak 2*--------------------------
def sumn(niz):
    zbir=0
    for el in niz:
        zbir=zbir+el
    return zbir
#Glavni program
niz=input("Unesite niz brojeva, elemente odvajati zarezom  ")
suman=sumn(niz)
print "Suma elementa niza: =", suman

#----------------------*Zadatak 3*--------------------------
def proizvod(niz):
    pr=1
    for el in niz:
        pr=pr*el
    return pr

#Glavni program
niz=input("Unesite niz brojeva, elemente odvajati zarezom ")
proizvodn=proizvod(niz)
print "Proizvod elemenata niza: =", proizvodn

#----------------------*Zadatak 4*--------------------------
def niz(niz1,niz2):
    niz=[]
    d1=len(niz1)
    d2=len(niz2)
    d3=0
    n=0
    if d1>d2:
        while n<d2:
            niz.insert(d3,niz2[n])
            d3=d3+1
            niz.insert(d3,niz1[n])
            n=n+1
            d3=d3+1
        while n<d1:
            niz.insert(d3,niz1[n])
            d3=d3+1
            n=n+1
    elif d2>d1:
        while n<d1:
            niz.insert(d3,niz1[n])
            d3=d3+1
            niz.insert(d3,niz2[n])
            n=n+1
            d3=d3+1
        while n<d2:
            niz.insert(d3,niz2[n])
            n=n+1
            d3=d3+1
    else:
        while n<d1:
            niz.insert(d3,niz1[n])
            d3=d3+1
            niz.insert(d3,niz2[n])
            d3=d3+1
            n=n+1
    return niz

#Glavni program
niz1=input("Unesite prvi niz, elemente odvajati zarezom ")
niz2=input("Unesite drugi niz, elemente odvajati zarezom ")
opcija=raw_input("Unesite opciju (p-prvi niz ili d-drugi niz) ")
n3=[]
if opcija=="p":
    n3=niz(niz1, niz2)
    print "Novi niz je:",n3
elif opcija=="d":
    n3=niz(niz2,niz1)
    print "Novi niz je:", n3
else:
    print "Uneo si pogresan broj!"

#----------------------*Zadatak 5*--------------------------
recenica=raw_input("Unesi recenicu!")
i=0
for el in recenica:
    print recenica[i]
    i=i+1

#----------------------*Zadatak 6*--------------------------
    import numpy as np
    b=int(input("Unesi broj tacaka:"))
    xniz=[]
    yniz=[]
    i=0
    k=0
    while i<b:
        x=raw_input("Unesi koordinate u formi X,Y")
        xlista=list(x.split(","))
        xniz.insert(k,(float(xlista[0])))
        yniz.insert(k,(float(xlista[1])))
        i=i+1

    s=int(input("Unesi stepen polinoma:"))
    fit_xy = np.polyfit(xniz, yniz, s)
    fit_fn_xy = np.poly1d(fit_xy)
    print "Polinom p(x)=",fit_fn_xy

#----------------------*Zadatak 7*--------------------------
print "---------------------\nDobro dosao\n--------------------- \nAJNC\n---------------------\n"
ime =raw_input("Unesi tvoje ime!")
from random import randint
def spil():
    #Tipovi i vrednosti karata
    karte_vrednost = ['As','2','3','4','5','6','7','8','9','10','J','Q','K']
    karte_tip = ['Herc','Pik','Tref','Karo']
    spil = []
    #Prolazak korz sve karte u spilu
    for i in karte_tip:
        for j in karte_vrednost:
            spil.append(j + ':' + i)
    return spil
def karte_vrednost(karta):
    if karta[:1] in ('J','Q','K','1'):
        return int(10)
    elif karta[:1] in ('2','3','4','5','6','7','8','9'):
        return int(karta[:1])
    elif karta[:1] == 'A':
        print ("\n"+ str(karta))
        num = int(input("Da li zelis da ovo ima vrednost 1 ili 1?  Unesi 1 ili 11!\n>"))
        while num !='1' or num !='11':
            if num == '1':
                return int(1)
            elif num == '11':
                return int(11)

def nova_karta(spil):
    return spil[randint(0,len(spil)-1)]

def brisi_kartu(spil,karta):
    return spil.remove(karta)

play_again = ''
while play_again != 'KRAJ':
    novi_spil = spil()
    karta1 = nova_karta(novi_spil)
    brisi_kartu(novi_spil, karta1)
    karta2 = nova_karta(novi_spil)
    brisi_kartu(novi_spil, karta2)
    print ("\n\n\n\n" + karta1 + " i " + karta2)
    vr1=karte_vrednost(karta1)
    vr2 = karte_vrednost(karta2)
    ukupno = vr1+vr2
    print(str(ime)+ ", imaš ukupno:" + str(ukupno))

    karta1_racunar = nova_karta(novi_spil)
    brisi_kartu(novi_spil, karta1_racunar)
    karta2_racunar = nova_karta(novi_spil)
    brisi_kartu(novi_spil, karta2_racunar)
    vr1_racunar =karte_vrednost(karta1_racunar)
    vr2_racunar = karte_vrednost(karta2_racunar)
    ukupno_racunar = vr1_racunar + vr2_racunar
    print ("Racunar ima u zbiru:" + str(ukupno_racunar))

    if ukupno == 21:
        print("AJNC!!!!")
    else:
        while ukupno < 21:  #
            answer = input("Da li želiš da nastaviš ili odustaneš? Unesite Da ili Ne! \n> ")
            if answer == 'Da':
                sl_karta = nova_karta(novi_spil)
                brisi_kartu(novi_spil, sl_karta)
                sl_vr = karte_vrednost(sl_karta)
                ukupno += int(sl_vr)
                print (str(ime)+ ", tvoja nova karta je:"+sl_karta + ",a tvoj novi rezultat je: " + str(ukupno))
                if ukupno > 21:
                    print("Zao mi je! Igubio si! Više sreće drugi put! :D ")
                    igraj_opet = input("Da li želiš da igraš novu igru? Unesi KRAJ da napustiš igru...\n")
                elif ukupno == 21:
                    print("Pobedio si! Cestitam!")
                    play_again = input("Da li želiš da igraš novu igru? Unesi KRAJ da napistiš igru...\n")
                else:
                    continue
            elif answer == 'Ne':
                print("Računar otkriva drugu kartu!")
                print("Karta je" + karta2_racunar + "! Računar ima u zbiru: " + str(ukupno_racunar))
                if ukupno_racunar < 17:
                    print("Računar igra opet!")
                    racunar_vise=nova_karta(novi_spil)
                    racunar_vise_vr = karte_vrednost(racunar_vise)
                    print("Ova karta je: " + str(racunar_vise))
                    ukupno_racunar += int(racunar_vise_vr)
                    if ukupno_racunar > 21 and ukupno <= 21:
                        print("Pobedio si! Računar je izgubio!")
                    elif ukupno_racunar < 21 and ukupno_racunar > ukupno:
                        print("Računar ima ukupno" + str(ukupno_racunar) + " Izgubio si!")
                    else:
                        continue
                elif ukupno_racunar == ukupno:
                    print("Nema pobednika! I ti i racunar imate ukupnu vrednost u zbiru od 21!")
                elif ukupno_racunar < ukupno:
                    print("Pobedio si!")
                else:
                    print("Izgubio si!")
                play_again = input("\nDa li želiš da igraš novu igru? Unesi KRAJ ili Da! \n")
                break
print(str(ime)+ "Hvala što si igrao!")

