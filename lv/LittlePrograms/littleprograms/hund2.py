class Hund:
    species = "Canis lupus familiaris" # Klassenattribut (oder auch stat. Attribut genannt)
    zaehler = 0 # zählen wie viele Hundeinstanzen es gibt

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

if __name__ == '__main__':

    # statische oder klassiche Methode aufrufen
    Hund.print_anzahl_hunde()

    rex = Hund("Kommissar Rex", 13)
    lassie = Hund("Lassie", 10)
    Hund.print_anzahl_hunde()



