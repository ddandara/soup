from carrinho import *
from compra import *
class Sopa:

    def __init__(self, nn, preco, sabor, acompanhamento, qnt):
        self.nome = input("Qual sopa da casa você deseja? ")
        self.nn = nn
        self.preco = preco
        self.sabor = sabor
        self.acompanhamento = acompanhamento
        self.qnt = qnt


    def mostrar_preco(self):
        print(self.preco)

    def mostrar_sabor(self):
        print(self.sabor)

    def mostrar_acompanhamento(self):
        print(self.acompanhamento)

    def mostrar_qnt(self):
        print(self.qnt)

    def mostrar_nn(self):
        print(self.nn, "->Esse foi o prato escolhido")
        


    def mostrar_sopa(self):
        if(nome=="Matryoshka"):
          print(self.soup1)

        elif(nome=="Hellevator"):
          print(self.soup2)

        elif(nome=="Chronosaurus"):
          print(self.soup3)

        elif(nome=="WOW"):
          print(self.soup4)

        else: 
          print("Sopa não disponível")

class Legumes(Sopa):
    def __init__(self, nn, preco, sabor, acompanhamento, qnt, tpnoodle, tpverdura):
        Sopa.__init__(self, nn, preco, sabor, acompanhamento, qnt)
        self.tpnoodle = tpnoodle
        self.tpverdura = tpverdura

    def mostrar_tpnoodle(self):
        print(self.tpnoodle)

    def mostrar_tpverdura(self):
        print(self.tpverdura)

    def verificar_disponibilidade(self):
        print(self.nome, "Esse prato está disponível")


class Carne(Sopa):
    def __init__(self, nn, preco, sabor, acompanhamento, qnt, tparroz, tpcarne):
        Sopa.__init__(self, nn, preco, sabor, acompanhamento, qnt)
        self.tparroz = tparroz
        self.tpcarne = tpcarne

    def mostrar_tparroz(self):
        print(self.tparroz)

    def mostrar_tpcarne(self):
        print(self.tpcarne)

    def verificar_disponibilidade(self):
        print(self.nome, "Esse prato está disponível")


class Carnecomlegumes(Legumes, Carne):
    def __init__(self, nn, preco, sabor, acompanhamento, qnt, tpnoodle, tpverdura, tparroz, tpcarne, tptorrada):
        Legumes.__init__(self, nome, preco, sabor, acompanhamento, qnt, tpnoodle, tpverdura)
        Carne.__init__(self, nome, preco, sabor, acompanhamento, qnt, tparroz, tpcarne)
        self.tptorrada = tptorrada

    def mostrar_tptorrada(self):
        print(self.tptorrada)


soup2 = Carne("Hellevator", 15, "sabor: carne picante", "acompanhamento: Bruschetta", 1, "arroz cateto", "carne bovina")
soup2.mostrar_nn()
soup2.mostrar_sabor()
soup2.mostrar_qnt()
soup2.mostrar_preco()
soup2.mostrar_acompanhamento()
soup2.mostrar_tparroz()
soup2.mostrar_tpcarne()

