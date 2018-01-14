# -*- coding: utf-8 -*-
#----------------------*Zadatak 1*--------------------------
print "Здраво геоинформатичари!"

#----------------------*Zadatak 2*--------------------------
a=int(raw_input("Unesi vrednost prvog broja:"))
b=int(raw_input("Unesi vrednost drugog broja:"))
print "Rezultat \nPrvi broj:{0}\nDrugi broj:{1}\nZbir:{2}\nRazlika:{3}\nProizvod:{4}\nCelobrojni ostatak:{5}\nCeo deo:{6}".format(a,b,a+b,a-b,a*b,a%b,a//b)

#----------------------*Zadatak 3*--------------------------
a = raw_input('Unesite prvi pravac u formatu stepeni:minute:sekunde :')
(stepeni, minute, secunde) = map(float, a.split(':'))
b = raw_input('Unesite drugi pravac u formatu stepeni:minute:sekunde : ')
(stepeni2, minute2, secunde2) = map(float, b.split(':'))

p1=stepeni+minute/60+secunde/3600
p2=stepeni2+minute2/60+secunde2/3600
if p1<p2:
    print "Ugao izmedju dva pravca iznosi: {0} stepeni".format(round((p2-p1),4))
else:
    print "Ugao izmedju dva pravca iznosi: {0} stepeni".format(round((p2-p1+360),4))

#----------------------*Zadatak 4*--------------------------
br=int(raw_input("Unesi prvi cetvorocifren broj: "))
br1=int(raw_input("Unesi drugi cetvorocifren broj: "))
a=int((br1/1000))
b=int(((br1%1000)/100))
c=int(((br1%100)/10))
d=int((br1%10))
zbir=a+b+c+d

a1=int((br/1000))
b1=int(((br%1000)/100))
c1=int(((br%100)/10))
d1=int((br%10))
parne=b1+d1
neparne=a1+c1
razlika=abs(parne-neparne)
print "Zbir cifara drugog broja: {0}\nRazlika zbira cifara na parnim i neparnim pozicijama: {1}".format(zbir,razlika))

#----------------------*Zadatak 5*--------------------------
a=raw_input("Unesi petocifren broj:")
x=-1
for c in a:
    i=int(c)
    if i>x:
        x=i
print x

print "\n Najveća cifru u broju je:",x,

#----------------------*Zadatak 6*--------------------------
s=raw_input("Unesi pet karaktera:")
numbers = sum(c.isdigit() for c in s)
print "Broj cfara koji se pojavio u unetom karakteru je:",numbers

#----------------------*Zadatak 7*--------------------------
xa = int(input("Unesi X koordinatu tačke A:"))
ya = int(input("Unesi Y koordinatu tačke A:"))
xb = int(input("Unesi X koordinatu tačke B:"))
yb = int(input("Unesi Y koordinatu tačke B:"))
xc = int(input("Unesi X koordinatu tačke C:"))
yc = int(input("Unesi Y koordinatu tačke C:"))
xm = int(input("Unesi X koordinatu tačke M:"))
ym = int(input("Unesi Y koordinatu tačke M:"))

pu1 = abs((xa * (yb - yc)) + (xb * (yc - ya)) + (xc * (ya - yb)))
pu = pu1 / 2

p11 = abs((xa * (yb - ym)) + (xb * (ym - ya)) + (xm * (ya - yb)))
p1 = (p11 / 2)
p22 = abs((xm * (yb - yc)) + (xc * (ym - yb)) + (xb * (yc - ym)))
p2 = p22 / 2
p33 = abs((xa * (ym - yc)) + (xc * (ya - ym)) + (xm * (xc - ya)))
p3 = p33 / 2

pp3 = p1 + p2 + p3
if pu == pp3:
 print "Tačka M se nalazi unutar trougla ABC"
else:
 print "Tačka M se nalazi izvan trougla ABC"

# ----------------------*Zadatak 8*--------------------------
import random
ZB=random.randint(0,100)
print "--------IGRA:Pogodi broj---------\n"
ime =raw_input("Unesi ime:")
print( ime + ' zamisljeni broj se nalazi u intervalu izmedju 1 i 100')
pokusaj=0

while pokusaj < 50:
    broj=int(input("Unesite Vaš broj:"))
    pokusaj = pokusaj + 1
    if broj < ZB:
        print("Vas broj je manji od zamisljenog broja")
    elif broj > ZB:
        print("Vas broj je veci od zamisljenog broja")
    elif broj==ZB:
        pokusaj = str(pokusaj)
        print('Bravo, ' + ime + '! Pogodio si moj broj iz ' + pokusaj + ' puta!')
