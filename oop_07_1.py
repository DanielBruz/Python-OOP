"""
Polymorfizmus, Duck typing, Abstraktné classy

Polymorfizmus znamená viacero foriem. Metódy s rovnakým menom aplikované na rozdielne objekty môžu mať
rôznu implementáciu. Tu sa dostávame k duck typingu. V rámci Pythonu nás skôr zaujímajú vlastnosti a metódy objektu,
než ich typ. Python zároveň umožňuje vytvárať šablóny pre implementáciu dcérskych metód pomocou abstraktných class.

"""
import abc

# Polymorfizmus:
# Znamená více forem. Funkce se stejným názvem můžou dělat rozdílné věci. Jeden z principů OOP.
# zkusíme to na metodě __add__.

"Jeden ".__add__("Dva")  # spojí řetězce

(1).__add__(2)  # když to aplikujeme na integer, sčítá. Metoda __add__ má polymorfickou aplikaci.


class Polozka():  # toto je mateřská třída
    def __init__(self, nazev, autor, cena):
        self.nazev = nazev
        self.autor = autor
        self.cena = cena

    def zobraz_cenu(self):
        print("Cena je: ", self.cena)


class Kniha(Polozka):
    pass


class KnihaZadarmo(Polozka):  # mění implementaci metody "zobraz_cenu".
    def zobraz_cenu(self):
        print("Tato kniha je zdarma.")


kniha = Kniha("O Honzíkovi a Mařence", "Bratři Grimmové", 10)
knihazadarmo = KnihaZadarmo("O Honzíkovi a Mařence", "Bratři Grimmové", 0)

kniha.zobraz_cenu()  # cena = 10
knihazadarmo.zobraz_cenu()  # kniha je zdarma. Změnili jsme v této třídě metodu "zobraz_cenu".
# Polymorfizmus v praxi, metody se jmenují stejně, ale dělají různé věci.


################################## Duck Typing ####################################################
# "Duck Typing". Když něco vypadá jako kachna, kejhá jako kachna, chodí jako kachna, bude to kachna.
# Když to má název, autora a cenu, bude to položka. Princip: Objekt je méně důležitý než metody, které implementuji.
# Při implementaci nás zajímají atributy a metody více než samotný objekt.

################################## Abstraktní třídy ###############################################
# Aby jsme měli jednotnou strukturu našich tříd, můžeme definovat abstraktní třídy.
# Slouží jako šablony pro ostatní třídy. Sami se nepoužívají.
# Definují metody, které musí jejich dceřinné třídy implementovat.
# Jinak nebudou moci být dceřinnými třídami. Abstraktní třídy definují rozhraní, které musí být implementováno
# v odvozených třídách. Odvozená třída, která dědí z abstraktní třídy, musí implementovat všechny abstraktní metody
# a vlastnosti. Jinak dojde k chybě a program nebude fungovat. Takto zaručíme, že všechny dceřinné třídy budou
# mít jednotné rozhranní.

from abc import ABC, abstractmethod


# od Python verze 3.3


class AbcPolozka(ABC):
    @abstractmethod
    # od Python 3.3 se nepoužívá @abstractclassmethod.
    def zadej_cenu(self, cena):
        return

    @abstractmethod
    def zobraz_cenu(self):
        return


# konkrétní implementace abstraktní třídy:

class Kniha1(AbcPolozka):
    def zadej_cenu(self, cena):
        self.cena = cena

    def zobraz_cenu(self):
        print("Cena je : ", self.cena)


class Kniha2(AbcPolozka):
    def zadej(self, cena):  # chybný název metody
        self.cena = cena

    def zobraz_cenu(self):
        print("Cena je : ", self.cena)


kniha1 = Kniha1()
kniha2 = Kniha2()   # vyhodí chybu, protože je definována špatná metoda "zadej". TypeError: Can't instantiate
# abstract class Kniha2 with abstract method zadej_cenu.


