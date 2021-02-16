

class Delivery:

    def __init__(self, contato, unidades, servicos, catalogo, regiao, sopas):
        self.contato = contato
        self.unidades = unidades
        self.servicos = servicos
        self.catalogo = catalogo
        self.regiao = regiao
        self.sopas = sopas

    def mostrar_contato(self):
      print(self.contato)
    def mostrar_unidades(self):
      print(self.unidades)
    def mostrar_servicos(self):
      print(self.servicos)
    def mostrar_catalogo(self):
      print(self.catalogo)
    def mostrar_regiao(self):
      print(self.regiao)
    def mostrar_sopas(self):
      print(self.sopas)


deli = Delivery ('GODS MENU SOPARIA - Contato:40028922', 'Unidades: Av Calama e Zona Sul', 'Entrega em domicílio e take out', 'Sopas Variadas', 'Entrega em todas as zonas', 'Sopas: Matryoshka, Hellevator, Chronosaurus e WOW-------------------------------------------------------------')
deli.mostrar_contato()
deli.mostrar_unidades()
deli.mostrar_servicos()
deli.mostrar_regiao()
deli.mostrar_sopas()