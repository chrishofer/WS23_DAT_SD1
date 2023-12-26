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
    def __init__(self, n:str, a:int):
        self.name = n #Parameter n wird auf Instanzattribut gespeichert (jedes Objekt/Instanz hat eigene Var.)
        self.age = a
        # Frage: In welchem Fall wird der property setter aufgerufen?
        self.__chip_nr = 1 # gehen direkt auf Attribut
        self.chip_nr = 1 # gehen über property setter
        self.__pulse = 80 # dürfen nur mit __ zugreifen, da es keine set methode gibt
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
        print(f'Corgi {self.name} bellt nicht da er gerade {self.loves_food} isst')


if __name__ == '__main__':

    # statische oder klassiche Methode aufrufen
    Hund.print_anzahl_hunde()

    rex = Hund("Kommissar Rex", 13)
    lassie = Hund("Lassie", 10)
    Hund.print_anzahl_hunde()


    rex.chip_nr = 1 # von außen (main, andere klassen) greifen wir nur über den namen direkt zu (damit über get/set properties)
    # rex.pulse = 10 # funktioniert nicht, da nur get property
    #rex._hund__chip_nr = 1 # vergessen und nicht machen


    rex.gib_laut("Achtung ein Wurstsemmel Dieb")
    c = Corgi("Cheddar", 13, "Känguru")
    c.gib_laut("Nix")

