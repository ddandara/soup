from sopa import *
from perfil import *
class Compra:
    def __init__(self):
        self._perfil=None
        self._sopa=None

    def comprar(self):
        self._perfil=perfil
        self._sopa=sopa

    def ver_compra(self):
        print ("Você comprou uma sopa "+self._sopa.nome)
