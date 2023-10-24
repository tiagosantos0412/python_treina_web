from pessoa import Pessoa
from insterface_passagem import Interface_Passagem

class Cliente(Interface_Passagem):
    def __init__(self, pessoa, viacao, cidade_origem, cidade_destino, data_ida, data_volta):
        self.__pessoa = pessoa
        self.__viacao = viacao
        self.__cidade_origem = cidade_origem
        self.__cidade_destino = cidade_destino
        self.__data_ida = data_ida
        self.__data_volta = data_volta
        self.__cont_compra = 0
        self.__cont_cancel = 0

    def __str__(self):
        return (f"Viação..................: {self.viacao} \n"
                f"Passageiro..............: {self.pessoa.nome} \n"  # Acessando o nome da pessoa
                f"Idade do Passageiro.....: {self.pessoa.idade} \n"  # Acessando a idade da pessoa
                f"RG do Passageiro........: {self.pessoa.rg} \n"  # Acessando o RG da pessoa
                f"CPF do Passageiro.......: {self.pessoa.cpf} \n"  # Acessando o CPF da pessoa
                f"Cidade de Origem........: {self.cidade_origem} \n"
                f"Cidade de Destino.......: {self.cidade_destino} \n"
                f"Data de Ida.............: {self.data_ida} \n"
                f"Data de Volta...........: {self.data_volta}")

    @property
    def viacao(self):
        return self.__viacao

    @viacao.setter
    def viacao(self, viacao):
        self.__viacao = viacao

    @property
    def cidade_origem(self):
        return self.__cidade_origem

    @cidade_origem.setter
    def cidade_origem(self, cidade_origem):
        self.__cidade_origem = cidade_origem

    @property
    def cidade_destino(self):
        return self.__cidade_destino

    @cidade_destino.setter
    def cidade_destino(self, cidade_destino):
        self.__cidade_destino = cidade_destino

    @property
    def data_ida(self):
        return self.__data_ida

    @data_ida.setter
    def data_ida(self, data_ida):
        self.__data_ida = data_ida

    @property
    def data_volta(self):
        return self.__data_volta

    @data_volta.setter
    def data_volta(self, data_volta):
        self.__data_volta = data_volta

    @property
    def cont_compra(self):
        return self.__cont_compra

    @cont_compra.setter
    def cont_compra(self, cont_compra):
        self.__cont_compra = cont_compra

    @property
    def cont_cancel(self):
        return self.__cont_cancel

    @cont_cancel.setter
    def cont_cancel(self, cont_cancel):
        self.__cont_cancel = cont_cancel

    @property
    def pessoa(self):
        return self.__pessoa

    def confirmar_compra(self):
        self.cont_compra += 1

    def cancelar_compra(self):
        self.cont_cancel -= 1
