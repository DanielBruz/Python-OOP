class Kniha:  # Trida Kniha
    pass  # nedelá nic


k = Kniha()  # vytvorim instanci tridy Kniha
print(k)  # podivam se, ze k je instance objektu Kniha nekde v pameti

kniha1 = Kniha()  # dalsi insrtance tridy Kniha
kniha2 = Kniha()  # dalsi instance

kniha1.nazev = "Vojna a mir"  # mame vytvoreny atribut. Konotace je nazev_objektu.nazev_atributu
print(kniha1.nazev)

kniha2.nazev = "O Honzovi a Marence"  # atribut  objektu je nazev promenne a my do ni muzeme vkladat hodnoty
print(kniha2.nazev)
