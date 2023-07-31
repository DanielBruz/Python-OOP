# abstrakce

# souvisi s enkapsulaci. Enkapsulace se dela, aby byla mozna abstrakce.
# Např. máme košík a můžeme do něj dávat a z něj vyndavat knihy. Co se skryva za temito operacemi/metodami nás
# nezajímá. Stačí že víme, co dělají.

class Kniha:
    def __init__(self, nazev):
        self.__nazev = nazev

    def get_nazev(self):
        return self.__nazev

    def set_nazev(self, x):
        self.__nazev = x


kniha = Kniha("Tri sestry")


class Kosik:
    def __init__(self):
        self.obsah = []

    def do_kosiku(self, x):
        print(x.get_nazev(), "byla vlozena do kosiku.")
        return self.obsah.append(x)

    def ven_z_kosiku(self, x):
        print(x.get_nazev(), "byla vyjmuta z kosiku.")
        return self.obsah.remove(x)


kosik = Kosik()
kosik.do_kosiku(kniha)
