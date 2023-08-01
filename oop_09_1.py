"""
Výjimky a spolehlivé metody:

Občas sa stane, že vaše objekty ostanú zaskočené. Nesprávne zadané hodnoty, neočakávané výsledky výpočtov alebo
nami vytvorené podmienky môžu spôsobiť pád programu. Aby sme tomu zabránili, môžeme použiť výnimky pre komunikáciu
medzi objektmi o takýchto problémoch.
"""

# Výjimky (chyby, které se objeví průběhem spuštěného programu.) Třeba dělení nulou:
# ZeroDivisionError: division by zero

x = 1 / 0

for n in range(-5, 5):  # program poběží a při n=0 se zastaví s chybou.
    print(1 / n)

# ošetřím výjimku, program na ní upozorní, ale nezastaví se a běží dál:

for n in range(-5, 5):
    try:
        print(1 / n)
    except ZeroDivisionError:
        print("Pozor, dělení nulou!")


# můžeme sami spustit výjimku:

class Kosik(list):
    def append(self, polozka):
        if not isinstance(polozka, Polozka):
            raise TypeError("Jen položky mohou být přidávané do košíku.")
        super().append(polozka)


kosik = Kosik()


class Polozka():
    pass


polozka = Polozka()

kosik.append(polozka)
kosik.append(0)  # TypeError: Jen položky mohou být přidávané do košíku.


# mužeme si vytvořit vlastní výjimky. Jde o třídu odvozenou od základní třídy výjimek Exception:

class ChybaCeny(Exception):
    pass


class ChybaZaporneCeny(ChybaCeny):
    def __init__(self, value):
        self.value = value
        print("Cena : ", self.value, " je záporná!")


class Kniha():
    def nastav_cenu(self, cena):
        if cena < 0:
            raise ChybaZaporneCeny(cena)
        else:
            self.cena = cena  # když je cena OK, nastaví se cena.


kniha = Kniha()
kniha.nastav_cenu(100)

kniha.nastav_cenu(-100)

