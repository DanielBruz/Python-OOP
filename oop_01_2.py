class Kniha:
    def zobraz_nazev(self):  # metoda tridy Kniha
        print("Nazev: ", self.nazev)


kniha1 = Kniha()
kniha2 = Kniha()

kniha1.nazev = "Vojna a mir"
kniha2.nazev = "O Honzovi a Marence"

kniha1.zobraz_nazev()   # () umoznuje vkladat do takovych metod parametry
kniha2.zobraz_nazev()

# I kdyby jsme meli stovky objektu tridy Kniha, vsechny mohou vyuzit metodu "zobraz_nazev", zmensi celkovy kod
