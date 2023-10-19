#Trabalhando com Herança
from animal import Animal
from interface_animal import InterfaceAnimal
#Trabalhando com composição
from dono import Dono
class Gato(Animal, InterfaceAnimal):
    def __init__(self, nome, idade, cor, raca, qtd_bolinhas, dono=Dono()):
        super().__init__(nome, idade, cor, raca)
        self.__dono = dono
        self.__qtd_bolinhas = qtd_bolinhas

    # Metodo que determina como um objeto será impresso
    def __str__(self):
        return (f"Nome do gato....: {self.nome} \n"
                f"Idade do gato...: {self.idade} \n"
                f"Cor do gato.....: {self.cor} \n"
                f"Raça do gato....: {self.raca} \n"
                f"QTD bolinhas....: {self.qtd_bolinhas}")

    @property
    def qtd_bolinhas(self):
        return self.__qtd_bolinhas

    @qtd_bolinhas.setter
    def qtd_bolinhas(self, qtd_bolinhas):
        self.__qtd_bolinhas = qtd_bolinhas

    @property
    def dono(self):
        return self.__dono

    @dono.setter
    def dono(self, dono):
        self.__dono = dono


    def emitir_som(self):
        return "Miaaau!"

    def andar(self):
        return "O gato está andando"
    def brincar(self):
        self.felicidade += 1
        return "O gato está brincando"