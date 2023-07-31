# Kompozice

# spojeni vice objektu dohromady tak, aby vznikl jeden objekt.
# V minulé úloze jsme si vyzvorili atribut obsah = [], ktery je samostatnym objektem - seznamem.
# A pouzili jsme dalsi objekt "kniha", ktery jsme vlozili pomoci x.
# V ramci objektu Kosik jsme spojili objekt Obsah a objekt Kniha = kompozice 2 objektu.
# Kompozice je uzitecna hlavne kdyz se objekt stava soucasti jineho objektu. Vysavac se sklada z motoru,
# filtru, hadice atp. A na zaklade kompozice tyto objekty tvori vysavac.

# Pouzijeme objekt Vlastnik v objektu Kosik, abychom vedeli, komu kosik patri.

class Kniha:
    def __init__(self, nazev):
        self.__nazev = nazev

    def get_nazev(self):
        return self.__nazev

    def set_nazev(self, x):
        self.__nazev = x


class Vlastnik():
    def __init__(self, jmeno):
        self.jmeno = jmeno


class Kosik():
    def __init__(self, vlastnik):
        self.obsah = []
        self.vlastnik = vlastnik
        print("Tento kosik vlastni: ", self.vlastnik.jmeno)

    def do_kosiku(self, x):
        print(x.get_nazev(), "byla vlozena do kosiku.")
        return self.obsah.append(x)

    def ven_z_kosiku(self, x):
        print(x.get_nazev(), "byla vyjmuta z kosiku.")
        return self.obsah.remove(x)


kniha = Kniha("Tri sestry")
vlastnik = Vlastnik("Jozef")
kosik = Kosik(vlastnik)
