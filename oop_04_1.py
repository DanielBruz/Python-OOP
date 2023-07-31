"""
Enkapsulace, abstrakce a kompozíce v Pythonu:
Enkapsulace nebo uzavrenost je jedním ze základních atributu objektového programovani.
Enkapsulace je vykonávaná, aby byla možná abstrakce.
Obe jsou ve videu vysvetlene, společne s príklady toho, jak fungují v Pythonu.
Nové objekty můžeme vytvářet tak, že spojíme dohromady více objektů. Toto je princíp kompozíce.
"""


#  pojdme si nejdrive definovat rozhrani objektu: metoda, kterou ostatni objekty pouzivaji pro praci s jinými objekty.
#  Jsou to metody a atribury, ktere nam umoznuji manipulovat s objekty a nasledne od nich ziskat urcitou odezvu.
#  Objekty by mely byt uzavrene a pracovat s nimi lze pouze pomoci rozhrani.

#  enkapsulace:
#  vlozit nejake informace do uzavrene logicke struktury, abychom zabranili nahodne nebo zamerne zmene takove informace.
#  Pro takove zmeny je vyhrazene rozhrani objektu. Trida poskytuje prave takove uzavreni objektu. Metody a promenne
#  jsou v ni enkapsulovany.

class Kniha:
    def __init__(self, nazev):
        self.__nazev = nazev

    def get_nazev(self):  # rozhrani, ktere nam dovoli ziskat nazev
        return self.__nazev

    def set_nazev(self, x):  # rozhrani, ktere nam dovoli nastavit nazev
        self.__nazev = x


kniha = Kniha("Tri sestry")

print(kniha.nazev)  # atribut "nazev" je verejny, dostupny i mimo tridu

# atributy mohou byt i chranene. Chranene ev. privatni atributy se oznacuji "_", treba tak, ze vsude v tride nahradime
# "self.nazev" atrtibutem "self._nazev". # Python nema vestavenou kontrolu chranenych atributu,
# pouze se oznacuji podtrzitkem. Tedy vypise mi hodnotu i tak.

print(kniha._nazev) # dopadne to stejne jako print(kniha.nazev)

# Hodnotu muzeme sice prirazit i takto, jako obvykle:

kniha._nazev = "Honzik a Marenka"

# ale programator by mel ke chranenemu atributu pristupovat vyhradne pomoci definovane metody, tedy set_nazev.

kniha = Kniha.set_nazev("Honzik a Marenka")

# chci-li udelat tento chraneny atribut skutecne nedostupny mimo tridu, dam mu na zacatku 2 podtrzitka:

self.__nazev
