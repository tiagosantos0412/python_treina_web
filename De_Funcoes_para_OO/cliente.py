from pessoa import Pessoa
from insterface_passagem import Interface_Passagem
class Cliente(Pessoa, Interface_Passagem):
    def __init__(self, nome, idade, rg, cpf, cep, rua, bairro, cidade, estado, viacao, cidade_origem,
                 cidade_destino, data_ida, data_volta, cont_compra, cont_cancel):
        super().__init__(nome, idade, rg, cpf, cep, rua, bairro, cidade, estado)
        self.__viacao = viacao
        self.__cidade_origem = cidade_origem
        self.__cidade_destino = cidade_destino
        self.___data_ida = data_ida
        self.__data_volta = data_volta
        self.__cont_compra = cont_compra
        self.__cont_cancel = cont_cancel

        # Metodo que determina como um objeto será impresso
        def __str__(self):
            return (f"Viação..................: {self.viacao} \n"
                    f"Passageiro..............: {self.nome} \n"
                    f"Idade do Passageiro.....: {self.idade} \n"
                    f"RG do Passageiro........: {self.rg} \n"
                    f"CPF do Passageiro.......: {self.cpf} \n"
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
        return self.___data_ida

    @data_ida.setter
    def data_ida(self, data_ida):
        self.___data_ida = data_ida

    @property
    def data_volta(self):
        return self.___data_volta

    @data_volta.setter
    def data_ida(self, data_volta):
        self.___data_volta = data_volta

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

    def confirmar_compra(self):
        self.cont_compra += 1

    def cancelar_compra(self):
        self.cont_cancel -= 1
