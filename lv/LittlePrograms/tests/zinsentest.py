import unittest
from littleprograms.zinsen import verzinsen


class MeinZinsenTest(unittest.TestCase):
    # setup phasen sind zum initialisieren da: objekte erzeugen, Verbindungen aufbauen, ...

    # einmal für alle tests in der klasse
    @classmethod
    def setUpClass(cls):
        # Dinge tun die viel Zeit brauchen, cls.hansi = CD(...)
        print("Wird einmal für die Klasse aufgerufen")

    def setUp(self):
        # Daten zurücksetzen vor jeder Methode (um Wechselwirkungen zwischen den Tests zu verhindern)
        print("Wird vor jedem Test einmal aufgerufen")
        self.betrag1 = 1000

    # Testmethoden werden am Namen erkannt (beginnend mit test)
    # Test sollte im Namen beschreiben worum es geht
    def test_verzinsen_ein_jahr(self):
        erg = verzinsen(self.betrag1, 1, 10)
        self.assertAlmostEqual(1100, erg)
        #self.assertEqual(True, False)  # add assertion here

    def test_verzinsen_mehrere_jahre(self):
        # execute phase (Führen das zu testende "Objekt" aus )
        erg = verzinsen(self.betrag1, 2, 10)
        # 1. jahr: 1100, 2.jahr: 1210
        # verify phase: ergebnis des testenden "objekts" mit korrektem ergebnis vergleichen
        self.assertAlmostEqual(1210, erg)

    # wird nach jedem test einmal ausgeführt
    def tearDown(self):
        # ressourcen freigeben, dateien schließen, ...
        print("tearDown")

    # wird einmal nach allen tests aufgerufen
    @classmethod
    def tearDownClass(cls):
        # ressourcen freigeben, db verbindung schließen, ...
        print("tearDownClass")

if __name__ == '__main__':
    unittest.main()
