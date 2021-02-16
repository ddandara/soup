from compra import *
class Perfil:
    def __init__(self):
        self.name=input("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++  Primeiramente, qual o seu nome? ")
        self.login=input("Crie um nome de login: ")
        self.telefone=input("Nos informe seu número de telefone atual: ")
        self.endereco=input("Insira o logradouro nº da casa e bairro: ")
        self.data_nasc=input("Insira sua data de nascimento: ")
        self.cpf=input("Estamos quase finalizando, insira seu cpf: ")
        self.email=input("Digite um endereço de email válido: ")
        self.senha=input("Crie uma senha de no mínimo 8 caracteres, com ao menos uma letra e um número: ")

    def consultperfil(self):
        return self.name

    def consultaNome(self):
        return self.name 
    
