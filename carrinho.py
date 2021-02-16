
class Carrinho:
    def __init__(self):
        self.sopas = []

    def Inserir_Sopa(self, Sopa):
        self.sopas.append(Sopa)

    def lista_Sopas(self):
        for Sopa in self.sopas:
            print(Sopa.nome, Sopa.preco)




    def soma_total(self):
      total = 0
      for Sopa in self.sopas:
        total += Sopa.preco
      return