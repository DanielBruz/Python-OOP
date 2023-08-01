"""
Vícenásobná dědičnost:

Dědíme s více tříd najednou.
Python prochází strukturu dědění a hledá třídy a metody, ktere chceme používat.
Múže se stát, že tyto atributy a metody budou ve vice tridach definovany stejně. Co na to Python?
"""


class A():
    def print_metoda(self):
        print("Print A")


class B(A):  # dceřinná trida A-čka
    pass

class C():  # nedědí
    def print_metoda(self):
        print("Print C")

# uděláme vícenásobné dědění:

class D(B, C):
    pass

d = D()

d.print_metoda()    # použila se metoda z třídy A (vytisklo se "Print A")
# Python prohledává class D(B, C) tak, že se podívá do D, tam metodu nenajde,
# tak pokračuje do B, kde metoda také není, ale B dědí z A, tak jde do A a v A jí najde a použije.
# Pokud by nebyla metod ani v A, přešel by do C, kde by jí našel a provedl.
# Toto se jmenuje "Method Resolution Order".

# když si nejsme jistí, tak zavoláme metodu mro():

D.mro()
