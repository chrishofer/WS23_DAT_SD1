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

if __name__ == '__main__':
    rex = Hund("Kommissar Rex", 13)



    lassie = Hund("Lassie", 10)

    rex.gib_laut("Wurtsemmel bitte")
    # Zugriff auf Klassenattribute
    print(Hund.species)

    # Zugriff auf Instanzattribute
    print(rex.age)
    print(lassie.name)