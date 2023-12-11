# default werte für parameter
def verzinsen(betrag: float, jahre: int =1, zinsen_in_prozent: float =10) -> float:
    """Einfache Zinseszins Berechnung

    Diese Funktion verzinst den `betrag` für `jahre` Jahre mit `zinsen_in_prozent` Prozent. Die Prozent werden als
    Werte zwischen 0 und 100 interpretiert.

    Parameters
    ----------
    betrag: float
        Der zu verzinsende Betrag.
    jahre: int
        Anzahl der Zinsjahre
    zinsen_in_prozent:
        Prozentsatz im Bereich zwischen 0 und 100

    Returns
    -------
    float
        Verzinsten Betrag
    """
    return betrag * (1 + zinsen_in_prozent / 100)**jahre


if __name__ == '__main__':
    print("Unser code")
    print(verzinsen(100))
    print(verzinsen(100, 10, 10))
    print(verzinsen(100, jahre=5))

    
    # print(verzinsen( jahre=5, 100)) # nicht erlaubt