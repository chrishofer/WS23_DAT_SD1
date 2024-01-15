# Unterschied abstrakte Klasse und Interface
# Abstrakte Klasse kann auch nicht abstrakte Methoden beinhalten (also implementiere Methoden)
# Ein Interface besteht üblicherweise nur aus abstrakten Methoden

# ++ Listen, Dictonaries Anwendung im Kontext Prüfungsbeispiel (zb. David Hasselhoff)
# Liste in Liste




class Hund:
    species = "Canis lupus familiaris" # Klassenattribut (oder auch stat. Attribut genannt)
    zaehler = 0 # zählen wie viele Hundeinstanzen es gibt



    @property
    def chip_nr(self):
        return self.__chip_nr

    # dürfen nur ungerade zahlen sein - sonst nichts zuweisen
    @chip_nr.setter
    def chip_nr(self, value):
        if (value % 2) != 0:
            self.__chip_nr = value

    @property
    def pulse(self):
        return self.__pulse

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value >= 0:
            self.__age = value

    # init Methode wird aufgerufen wenn neues objekt erzeugt wird
    def __init__(self, n:str, a:int, s:str):
        self.name = n #Parameter n wird auf Instanzattribut gespeichert (jedes Objekt/Instanz hat eigene Var.)
        self.age = a
        # Frage: In welchem Fall wird der property setter aufgerufen?
        self.__chip_nr = 1 # gehen direkt auf Attribut
        self.chip_nr = 1 # gehen über property setter
        self.__pulse = 80 # dürfen nur mit __ zugreifen, da es keine set methode gibt
        self.spielzeug = s
        print(self.age)
        # hier koennte beliebiger andere ganz ganz ganz komplzierter code stehen
        # (methodenaurufe, Datenbankabfrage, ...)

        Hund.zaehler += 1

    @classmethod
    def print_anzahl_hunde(cls):
        print(f"Derzeit gibt es {cls.zaehler} glückliche Hunde")


    def gib_laut(self, text: str):
        print(f'{self.name} bellt und sagt {text}')

    def __str__(self):
        return f"Hund {self.name} ist schon {self.age} Jahre alt"
    def __repr__(self):
        return f"Hund(name={self.name}, age={self.age})"

class Corgi(Hund):
    # es wird von python automatisch immer nur ein init aufgerufen
    # wenn wir kein init hätten würde automatisch das init von Hund (elternklasse) aufgerufen werden
    def __init__(self, name: str, age: int, lv: str):
        # hier müssen wir unsere initialiseirung machen - damit wir nicht code doppelt haben
        # müssen wir das init unserer elternklasse explizit aufrufen (ACHTUNG: in anderen programmirersprachen geht das manchmal automatisch rufen)
        super().__init__(name, age) # damite rufe ich die implementation meiner basisklasse auf
        self.loves_food = lv

    def gib_laut(self, text: str):
        super().gib_laut("Bin auch ein Hund") # ruft die Implementation einer Basisklasse auf
        print(f'Corgi {self.name} bellt nicht da er gerade {self.loves_food} isst')


# Klasse Hundehotel verwalte Hunde die auf Urlaub sind
class Hundehotel():
    # zum initialisieren drei leeren Listen erzeugen: Liste hunde, futter, spielzeug
    def __init__(self):
        self.__hunde = [] # list()
        self.__futter = []
        self.__spielzeug = []

    # für alle drei listen eine add method um ein entsprechendes objekts in die Liste hinzuzufügen
    def add_hund(self, h):
        self.__hunde.append(h)

    def add_futter(self, f):
        self.__futter.append(f)

    def add_spielzeug(self, s):
        self.__spielzeug.append(s)


    # Schreiben Sie eine Methode die zurückliefert wie viele Hunde (die derzeit im Hotel untergebracht sind) ihr
    # Lieblingsspielzeug im Hotel finden werden - der Rückgabewert soll eine int Zahl sein
    def hunde_die_passendes_spielzeug_bekommen(self) -> int:
        erg = 0
        for h in self.__hunde: # das wir die hund eliste nicht verändern müssen wir nicht mit range drüber iterieren
            if h.spielzeug in self.__spielzeug:
                erg = erg + 1
        return erg

    # Wir müssen uns überlegen welches Spielzeug wir als nächtse kaufen möchten
    # Deshalb erstellen wir uns ein Dictionary, das uns zeigt, was die Lieblingsspielzeuge im Hotel sind
    # Dictionary soll der Rückgabewert und soll uns zurückliefern wie oft welches Spielzeug gemoch wird
    # {"Stofftier": 2, "Knochen": 3, "Woodstock": 1}
    def welches_spielzeug_ist_am_beliebtesten(self):
        erg = {}
        for hund in self.__hunde:
            if hund.spielzeug in erg:
                erg[hund.spielzeug] = erg[hund.spielzeug] + 1
            else:
                erg[hund.spielzeug] = 1

        return erg

    # Parameter Preise ist ein Dictionary - falls Spielzeug nicht im Dictionary ist
    #
    def fuer_alle_spielzeug_kaufen(self, preise):
        preis = 0
        pass
        #for h in self.__hunde:


# eine funktion erstelle
# die Funktion erhält als Parameter folgend: Eine Liste die besteht einzelnen Listenelementen:
# der erste Eintrag ist immer eine Jahreszahl
# der zweite Eintrag ist eine Liste mit Verkaufszehlen
# [[2010, [100, 2300, 3200, 2032030]], [2011, [100, 200]], [2012, [100, 500, 600, 700]]]

def verkaufszahlen_berechnen3(v):
    summe = 0
    # hier haben wir eigentlich 3 listen - wie viele for schleifen brauchen wir?
    # billige antwort: 3 (nicht wirklich korrekt)
    # korrekte antwort: 2
    for jahres_verkaufszahlen in v:
        for werte in jahres_verkaufszahlen[1]: # nur das 2te element beinhaltet die verkaufszahlen
            summe += werte

    return summe




# erste Ausbaustufe - Parameter: Die Verkaufszahlen fürs Jahr 2010
# [2010, [100, 2300, 3200, 200]]
# Funktion soll uns zurückliefern wie viel Stück vekrauft wurden
def verkaufszahlen_berechnen(v):
    summe = 0
    # wie viele elemente hat die liste elemente v: 2
    # Zugriff aufs erste Element: int
    # v[0]
    # Zugriff aufs zweite Element: list
    # v[1]
    #teilliste = v[1]
    #teilliste[0]
    #wert = v[1][0] # greife auf die liste v zu - nehme mir das 2te element (index 1) -> ist wieder eine liste -> von dieser liste greife ich auf das 1te element zu (Index 0)
    # wert wäre der wert 100

    #liste = [1,2,3,4,5]
    #for w in liste:
    #    summe += w

    for w in v[1]:
        summe += w

    return summe


# variante 2: liste in liste
# [[100, 10, 20], [100, 30, 40, 80], [100, 200]]
# alle verkaufszahlen aufsummieren
def verkaufszahlen_berechnen2(v):
    summe = 0
    # wie viele elemente hat die liste v? 3
    for teil_liste in v:
        # was für einen typ hat ein listenelement w1?
        for wert in teil_liste:
            summe += wert

    return summe


if __name__ == '__main__':
    rex = Hund("Kommissar Rex", 13, "Knochen")
    rexine = Hund("Kommissar Rexine", 13, "Knochen")
    lassie = Hund("Lassie", 10, "Stofftier")
    snoopy = Hund("Snoopy", 10, "Woodstock")
    Hund.print_anzahl_hunde()


    print(rex.pulse)
    rex.chip_nr = 1 # von außen (main, andere klassen) greifen wir nur über den namen direkt zu (damit über get/set properties)
    # rex.pulse = 10 # funktioniert nicht, da nur get property
    #rex._hund__chip_nr = 1 # vergessen und nicht machen


    rex.gib_laut("Achtung ein Wurstsemmel Dieb")

    #
    hhotel = Hundehotel()

    hhotel.add_hund(rex)
    hhotel.add_hund(rexine)
    hhotel.add_hund(snoopy)
    hhotel.add_hund(lassie)


    hhotel.add_spielzeug("Stofftier")
    hhotel.add_spielzeug("Knochen")

    print(hhotel.hunde_die_passendes_spielzeug_bekommen())

    d = hhotel.welches_spielzeug_ist_am_beliebtesten()
    summe_spielzeuge = 0
    print("***")
    for spielzeugname in d: # key ist der schlüssel
        #print(key)
        summe_spielzeuge = summe_spielzeuge + d[spielzeugname] # muss ich mit mir eckigen klammern den inhalt holen

    print(summe_spielzeuge)
    print("###")
    summe_spielzeuge = 0
    for spielzeugname, anzahl in d.items(): # mit items() bekomme ich ein tupel zurück - schlüssel und wert
        #print(key)
        summe_spielzeuge = summe_spielzeuge + anzahl # hier kann ich direkt den zweiten wert aus dem tupel nehmen
    print(summe_spielzeuge)


