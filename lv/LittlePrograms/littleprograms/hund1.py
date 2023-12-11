class Hund:
    species = "Canis lupus familiaris" # Klassenattribut (oder auch stat. Attribut genannt)
    # init Methode wird aufgerufen wenn neues objekt erzeugt wird
    def __init__(self, n:str, a:int):
        self.name = n #Parameter n wird auf Instanzattribut gespeichert (jedes Objekt/Instanz hat eigene Var.)
        self.age = a
        # hier koennte beliebiger andere ganz ganz ganz komplzierter code stehen
        # (methodenaurufe, Datenbankabfrage, ...)
    def gib_laut(self, text: str):
        print(f'{self.name} bellt und sagt {text}')

    def __str__(self):
        return f"Hund {self.name} ist schon {self.age} Jahre alt"
    def __repr__(self):
        return f"Hund(name={self.name}, age={self.age})"

if __name__ == '__main__':
    rex = Hund("Kommissar Rex", 13)
    lassie = Hund("Lassie", 10)

    rex.gib_laut("Wurtsemmel bitte")
    Hund.gib_laut(rex, "Noch mal Wurstsemmel bitte")
    # Zugriff auf Klassenattribute
    print(Hund.species)
    print(Hund.__dict__)

    # Zugriff auf Instanzattribute
    print(rex.age)
    print(lassie.name)

    # wir können auch auf Klassenattribute über Instanz zugreifen
    # (ACHTUNG nur lesend)
    #print(rex.species)





    # immer wenn wir mit . auf etwas zugreifen
    # python schaut im __dict__ der Instanz nach ob es das Ding nach dem . gibt
    # falls es nichts findet schaut es im __dict__ der Klasse nach
    print(lassie.gib_laut("ich rette Menschen"))
    print(lassie.__dict__)

    # pfui nicht machen - fügt ein neues Instanzattribut zur Instanz lassie hinzu
    #lassie.species = "Hansi"
    #print(lassie.__dict__)

    # Was lernen wir drauf? Auf Klassenattribute am Besten immer über Klassenname (hier Hund) zugreifen
    Hund.species = "Canis lupus katzikus"

    # Hunde ausgeben
    print(rex)

    hunde_hotel = [rex, lassie]
    print(hunde_hotel)

