#----------------------*Zadatak 1*--------------------------
import math
class Sfera:
    br = 0
    def __init__(self, r=1, x=0, y=0, z=0):
        self.poluprecnik = r
        self.xCentar = x
        self.yCentar = y
        self.zCentar = z
        Sfera.br += 1

    @staticmethod
    def brojKreiranihObjekata():
        return Sfera.br

    def zapremina(self):
        if (self.poluprecnik == 1):
            self.volume =1.3333333333 *math.pi
            return (self.volume)
        else:
            r = self.poluprecnik
            self.volume = 1.3333333333 * math.pi*(r*r*r)
            return (self.volume)

#Glavni program
print "Broj kreiranih objekata: ", Sfera.brojKreiranihObjekata()
sfera=Sfera(4.0,0,0,0)
globus=Sfera(12,1.0,1.0,1.0)
bilijarska_lopta=Sfera(10.0,10.0,0)
jedinicna_sfera=Sfera()
print "Broj kreiranih objekata: ",Sfera.brojKreiranihObjekata()
print "Zapremina sfere je: ", sfera.zapremina()
print "Zapremina globusa je: ", globus.zapremina()
print "Zapremina bilijarske_lopte je: ", bilijarska_lopta.zapremina()
print "Zapremina jedinicne_sfere je: ", jedinicna_sfera.zapremina()

#----------------------*Zadatak 2*--------------------------
class Tacka:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def pomeranje(self, x_pom, y_pom):
        self.x = x_pom + self.x
        self.y = y_pom + self.y
        tacka = Tacka(self.x, self.y)
        return tacka

    def rastojanje(self,t):
        dx=(self.x-t.x)**2
        dy = (self.y - t.y)**2
        return math.sqrt(dx+dy)

class Duz:
    def __init__(self,pt=0,kt=0):
        self.pt=pt
        self.kt=kt

    def kreiranje_duzi(self,xp,yp,xk,yk):
        pt=Tacka(xp,yp)
        kt=Tacka(xk,yk)
        d=Duz(pt,kt)
        return d

    def duzinaDuzi(self):
        return self.pt.rastojanje(self.kt)

    def str(self):
        print "Koordinate početne tačke(X i Y) su: "+str(self.pt.x) +", "+ str(self.pt.y) + "\nKoordinate krajnje tačke (X i Y) su: "+str(self.kt.x) + ", "+ str(self.kt.y)

#Glavni program
xp=float(input("Unesite x koordinatu pocetne tacke: "))
yp=float(input("Unesite y koordinatu pocetne tacke: "))
xk=float(input("Unesite x koordinatu krajnje tacke: "))
yk=float(input("Unesite y koordinatu krajnje tacke: "))
p=Tacka(xp,yp)
k=Tacka(xk,yk)
duz=Duz(k,p)
druga_duz=duz.kreiranje_duzi(10,12,15,16)
print "Prva duz je definisana sledecim koordinatama:\n" ,duz.str()
print "Druga duz je definisana sledećim koordinatama:\n",druga_duz.str()
dx=float(input("Unesite dx: "))
dy=float(input("Unesite dy: "))
k.pomeranje(dx,dy)
nduz=Duz(p,k)
print "Nova duz je definisana sledecim koordinatama:\n", nduz.str()

#----------------------*Zadatak 3*--------------------------
import random
import math
import itertools

class Povrs:
    ime = raw_input("Unesite ime: ")
    prezime = raw_input("Unesite prezime: ")
    metadataO = []
    metadataO.append(ime)
    metadataO.append(prezime)

    def __init__(self, c):
        self.c = c
        self.i = 0
        self.povrs = []
        while (self.i < self.c):
            self.x = random.randint(0, 100)
            self.y = random.randint(0, 100)
            self.z = random.randint(0, 100)
            self.tacka = (self.x, self.y, self.z)
            self.povrs.append(self.tacka)
            self.i = self.i + 1

    def br(self):
        return self.i

    def areaPoligona(self):
        n = len(self.povrs)
        self.area = 0.0
        for i in range(n):
            j = (i + 1) % n
            self.area += self.povrs[i][0] * self.povrs[j][1]
            self.area -= self.povrs[j][0] * self.povrs[i][1]
        self.area = abs(self.area) / 2.0
        return self.area

    def centroid(self):
        self.centroide = ((sum(d[0] for d in self.povrs)) / len(self.povrs), (sum(d[1] for d in self.povrs)) / len(self.povrs))
        return self.centroide

    def max(self):
        self.maksimalnu = max(self.povrs, key=lambda item: item[0:1])
        return self.maksimalnu

    def min(self):
        self.minimalnu = min(self.povrs, key=lambda item: item[0:1])
        return self.minimalnu

    def index(self):
        self.metadata = [(ix, self.povrs[ix]) for ix in range(len(self.povrs))]
        return self.metadata

    def rastojanje(self):
        p0 = self.povrs
        p1 = self.povrs
        return math.sqrt((p0[0] - p1[0]) ** 2 + (p0[1] - p1[1]) ** 2)

    def minPar(self):
        self.minP = min(itertools.combinations(self.povrs, 2))
        return self.minP

    def minRastojanje(self):
        p0 = self.minP[0]
        p1 = self.minP[1]
        return math.sqrt((p0[0] - p1[0]) ** 2 + (p0[1] - p1[1]) ** 2)

    def elevacija(self):
        p0, p1 = self.povrs
        return (p0[2] - p1[2])

    def maxPar(self):
        self.maxP = max(itertools.combinations(self.povrs, 2))
        return self.maxP

    def maxElevacija(self):
        p0 = self.maxP[0]
        p1 = self.maxP[1]
        return (p0[2] - p1[2])

#Glavni program
    c = int(input("Unesi broj tacaka: "))
    p = Povrs(c)
    print "\nBroj tacaka: ", p.br()
    print "Poligon: ", p.povrs, "ima povrsinu od: ", p.areaPoligona()
    print "\nSredina poligona je:", p.centroid()
    print "\nMaksimalne vrednosti koordinata tačaka površi:", p.max()
    print "Minimalne vrednosti koordinata tačaka površi:", p.min()
    print "\n ID-ovi tacaka\n", p.index()
    print "\nDve najbliže tacke su: ", p.minPar(), ",a rastojanje izmedju njih je: ", p.minRastojanje()
    print "Interpolcija između dve tacke: ", p.maxPar(), "je", p.maxElevacija()
    print "\nOperator: ", p.metadataO
#----------------------*Zadatak 4*--------------------------
class Inzenjer:

    def __init__(self, ime="Bojana", prezime="Obrenovic", maticnibroj="021199477", licenca="Nema licencu"):
        self._ime = ime
        self._prezime = prezime
        self._maticnibroj = maticnibroj
        self._licenca=licenca

    def dajIme(self):
        return self._ime

    def dajPrezime(self):
        return self._prezime

    def dajMaticnibroj(self):
        return self._maticnibroj

    def dajLicencu(self):
        return self._licenca

    def postaviIme(self,ime):
        self._ime = ime

    def postaviPrezime(self,prezime):
        self._prezime = prezime

    def postaviLicencu(self,licenca):
        self._licenca = licenca

    def postaviIme(self,maticnibroj):
        self._maticnibroj = maticnibroj

    def info(self):
        print "Ime: "+self._ime+ "Prezime: " +self._prezime +"Maticni broj: " + self._maticnibroj+ "Broj licence: "+self._licenca

class GeodetskiInzenjer(Inzenjer):

    def __init__(self, ime="Bojana", prezime="Obenovic", maticnibroj="021199477", licenca="Nema licencu",radni_staz=0):
        Inzenjer.__init__(self,ime,prezime,maticnibroj,licenca)
        self.radni_staz = radni_staz

    def dajGodStaz(self):
        return self.radni_staz

    def postaviGodStaz(self,radni_staz):
        self.radni_staz = radni_staz

    def inf_licenca(self):
        a=self.dajLicencu()
        if a=="Nema licencu":
            print "Inzenjer nema licencu"
        else:
            print "Licenca inzenjera je ",a

    def info(self):
        print "Ime: {0} Prezime: {1} JMBG: {2} Licenca {3} Radni staz {4}".format(self._ime,self._prezime,self._maticnibroj,self._licenca,self.radni_staz)

class ElektrotehnickiInzenjer(Inzenjer):

    def __init__(self, ime="Marko", prezime="Markovic", maticnibroj="00664", licenca="Nema licencu", br_projekata=0):
        Inzenjer.__init__(self, ime, prezime, maticnibroj, licenca)
        self._br_projekata = br_projekata

    def dajBrProjekata(self):
        return self._br_projekata

    def postaviBrProjekata(self, br_projekata):
        self._br_projekata = br_projekata

    def licenca_info(self):
        a = self.dajLicencu()
        if a == "Nema licencu":
            print "Inzenjer nema licencu"
        else:
            print "Licenca inzenjera je ",a

    def info(self):
        print "Ime: {0} \nPrezime: {1} \nJMBG: {2} \nLicenca {3} \nRadni staz {4}". format(self._ime, self._prezime, self._maticnibroj, self._licenca, self._br_projekata)

#Glavni program
ime=raw_input("Unesite ime inzenjera: ")
prezime=raw_input("Unesite prezime inzenjera: ")
jmbg1=raw_input("Unesite maticni broj inzenjera: ")
licenca=raw_input("Unesite licencu inzenjera(Nema licencu):  ")
broj_projekata=int(input("Unesite broj projekata: "))
#Ispis informacija o inzenjeru elektrotehnike
a=ElektrotehnickiInzenjer(ime,prezime,jmbg1,licenca,broj_projekata)
a.info()
#Ispis informacija o licenci
a.licenca_info()
#----------------------*Zadatak 5*--------------------------
class Osoba:
    def __init__(self, ime, prezime,datum_rodjenja,adresa):
        self.ime = ime
        self.prezime = prezime
        self.datum_rodjenja=datum_rodjenja
        self.adresa = adresa


    def dajIme(self):
        return self._ime

    def dajPrezime(self):
        return self._prezime

    def dajDatumRodjenja(self):
        return self._datum_rodjenja

    def dajAdresu(self):
        return self._adresa

    def postaviIme(self, ime):
        self._ime = ime

    def postaviPrezime(self, prezime):
        self._prezime = prezime

    def postaviAdresu(self, adresa):
        self._adresa = adresa

    def postaviDatumRodjenja(self, datum_rodjenja):
        self._datum_rodjenja = datum_rodjenja

    def info(self):
        print "Ime: "+self._ime +"Prezime: "+self._prezime +"Datum rodjenja: "+ self._datum_rodjenja + "Adresa stanovanja: "+ self._adresa

class Djak(Osoba):
     def __init__(self, ime, prezime, datum_rodjenja, adresa, skola, odeljenje, godina_upisa):
         Osoba.__init__(self, ime, prezime,datum_rodjenja, adresa)
         self._skola=skola
         self._odeljenje=odeljenje
         self._godina_upisa=godina_upisa

     def dajNazivSkole(self):
         return self._skola

     def dajOdeljenje(self):
         return self._odeljenje

     def dajGodinuUpisa(self):
         return self._godina_upisa

     def postaviNazivSkole(self,naziv):
         self._skola=skola

     def postaviOdeljenje(self,odeljenje):
         self._odeljenje=odeljenje

     def postaviGodinuUpisa(self, godina_upisa):
         self._godina_upisa=godina_upisa

     def trenutniRazred(self):
        raz=str(self.dajOdeljenje())
        traz=raz.split("-")
        a=traz [0]
        return a

     def obnova(self,par):
        a=str(self.dajDatumRodjenja())
        aa=a.split(".")
        godinaR=int(aa[2])
        b=int(self.dajGodinuUpisa())
        brgodina=2017-godinaR
        if par==brgodina:
            print self._ime + "nije ponavljao razred."
        else:
            print self._ime + "je ponavljao razred."

     def info(self):
            print "Ime: "+self._ime + "Prezime: "+ self._prezime + "Datum rodjenja: " +self._datum_rodjenja + "Adresa stanovanja: " +self._adresa + "Naziv osnovne skole: " +self._naziv_skole +"Odeljenje: "+ self._odeljenje + "Godina upisa: "+ self._godina_upisa


class Zaposleni(Osoba):
     def __init__(self, ime, prezime, datum_rodjenja, adresa,naziv_kompanije, departman, lista_zakljucenja=[], lista_prekida=[]):
        Osoba.__init__(self, ime, prezime, datum_rodjenja, adresa)
        self._naziv_kompanije = naziv_kompanije
        self._departman = departman
        self._lista_zakljucenja = lista_zakljucenja
        self._lista_prekida = lista_prekida

     def dajKompaniju(self):
        return self._naziv_kompanije

     def dajDepartman(self):
        return self._departman

     def dajListuZakljucenja(self):
        return self._lista_zakljucenja

     def dajListuPrekida(self):
        return self._lista_prekida

     def postaviKompaniju(self,naziv_kompanije):
        self._naziv_kompanije = naziv_kompanije

     def postaviDepartman(self,departman):
        self._departman = departman

     def postaviListuZakljucenja(self,zakljucenja):
        self._lista_zakljucenja = lista_zakljucenja

     def postaviListuPrekida(self,prekidi):
        self._lista_prekida =lista_prekida

     def radniStaz(self):
        lista_zakljucenja=self.dajListuZakljucenja()
        lista_prekida=self.dajListuPrekida()
        i=0
        rd=0
        while i<len(lista_prekida):
            z=lista_zaklucenja[i]
            p=lista_prekida[i]
            z1=z.split(".")
            p1=p.split(".")
            d1=int(z1[0])
            m1=int(z1[1])
            g1 = int(z1[2])
            d2 = int(p1[0])
            m2 = int(p1[1])
            g2 = int(p1[2])
            if d1<=d2:
                d=d2-d1
            else:
                d=d2-d1+30
                m2=m2-1
            if m1 <= m2:
                 m=m2-m1
            else:
                m=m2-m1+12
                g2=g2-1
            g=g2-g1
            brm=m+g*12
            rd=rd+brm*30+d
            i+=1
        return rd

     def info(self):

        print "Ime: "+self._ime +"Prezime: "+self._prezime + "Datum rodjenja: "+self._datum_rodjenja + "Adresa stanovanja: "+self._adresa + "Naziv kompanije: "+self._naziv_kompanije + "Departman:" +self._departman +"Zaklucenja radnog odnosa: "+self._zakljucenja + "Prekidi radnog odnosa: "+self._prekidi

#Glavni program
recnik1 = {'Prvi razred':7, 8:'Drugi razred', 9:'Treci razred' , 10:'Cetvrti razred',11:'Peti razred',12: 'Sesti razred',13:'Sedmi razred', 14:'Osmi razred'}
recnik2 = {'I':'Prvi razred', 'II':'Drugi razred', 'III':'Treci razred' , 'IV':'Cetvrti razred','V':'Peti razred','VI': 'Sesti razred','VII':'Sedmi razred', 'VIII':'Osmi razred'}
k=raw_input("Unesite oznaku za koju vrstu osobe hocete da unosite podatke (D-djak, Z-zaposlen):  ")
if k=="D":
    ime = raw_input("Unesite ime djaka:  ")
    prezime = raw_input("Unesite prezime djaka:  ")
    datumr = raw_input("Unesite datum rodjenja djaka (dan.mesec.godina):  ")
    adresa = raw_input("Unesite adresu djaka:  ")
    skola = raw_input("Unesite naziv osnovne skole u koju djak ide:  ")
    odeljenje = raw_input("Unesite odeljenje u koje djak trenutno ide (razred - odeljenje (npr. I-1, II-2, III-3....):  ")
    datumup = raw_input("Unesite godinu upisa:  ")
    djak=Djak(ime,prezime,datumr,adresa,skola,odeljenje,datumup)
    r=djak.trenutniRazred()
    print "Djak trenutno ide u  ",recnik2[r]
    djak.obnova(recnik1[recnik2[r]])
    djak.info()


elif k=="Z":
    lista_z=[]
    lista_p=[]
    ime = raw_input("Unesite ime zaposlenog  ")
    prezime = raw_input("Unesite prezime zaposlenog  ")
    datumr = raw_input("Unesite datum rodjenja zaposlenog (dan.mesec.godina)  ")
    adresa = raw_input("Unesite adresu zaposlenog  ")
    kompanija = raw_input("Unesite naziv kompanije  ")
    departman = raw_input("Unesite naziv departmana  ")
    brf=int(input("Unesite broj firmi u kojima je zaposlen do sada radio.  "))
    i=0
    while i<brf:
        datum_zakljucenja = raw_input("Unesite datum zakljucenja radnog odnosa (dan.mesec.godina: 12.2.2008)  ")
        datum_prekida = raw_input("Unesite datum prekida radnog odnosa (dan.mesec.godina: 13.8.2010)  ")
        lista_z.append(datum_zakljucenja)
        lista_p.append(datum_prekida)
        i+=1
    nr=raw_input("Da li zaposlen trenutno negde radi(DA ili NE)  ")
    if nr=="DA":
        datum_zakljucenja=raw_input("Unesite datum zakljucenja novog ugovora (dan.mesec.godina: 12.2.2008)  ")
        datum_prekida = raw_input("Unesite danasnji datum (dan.mesec.godina: 12.8.2018)  ")
        lista_z.append(datum_zakljucenja)
        lista_p.append(datum_prekida)
    zaposl= Zaposlen(ime, prezime, datumr, adresa, kompanija, departman, lista_z,lista_p)
    lis=[zaposl.radniStaz()/30,zaposl.radniStaz()%30]
    print "Radni staz zaposlenog je tacno ",lis[0] , " meseci i ", lis[1], "dana."
    zaposl.info()
else:
    print "Pogresno ste uneli oznaku za osobu"







