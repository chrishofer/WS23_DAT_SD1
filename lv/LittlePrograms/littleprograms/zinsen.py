# default werte für parameter
def verzinsen(betrag: float, jahre: int =1, zinsen_in_prozent: float =10) -> float:
    return betrag * (1 + zinsen_in_prozent / 100)**jahre


if __name__ == '__main__':
    print("Unser code")
    print(verzinsen(100))
    print(verzinsen(100, 10, 10))
    print(verzinsen(100, jahre=5))
    # print(verzinsen( jahre=5, 100)) # nicht erlaubt