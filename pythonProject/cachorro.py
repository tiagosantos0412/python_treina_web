from animal import Animal
from interface_animal import InterfaceAnimal
from dono import Dono
class Cachorro(Animal, InterfaceAnimal):
    def __init__(self, nome, idade, cor, raca, qtd_brinquedos, dono=Dono()):
        super().__init__(nome, idade, cor, raca)
        self.__qtd_brinquedos = qtd_brinquedos
        self.__dono = dono

    #Metodo que determina como um objeto será impresso
    def __str__(self):
        return (f"Nome do cachorro....: {self.nome} \n"
                f"Idade do cachorro...: {self.idade} \n"
                f"Cor do cachorro.....: {self.cor} \n"
                f"Raça do cachorro....: {self.raca} \n"
                f"QTD brinquedos......: {self.qtd_brinquedos}")

    @property
    def dono(self):
        return self.__dono

    @dono.setter
    def dono(self, dono):
        self.__dono = dono

    @property
    def qtd_brinquedos(self):
        return self.__qtd_brinquedos

    @qtd_brinquedos.setter
    def qtd_brinquedos(self, qtd_brinquedos):
        self.__qtd_brinquedos = qtd_brinquedos

    def emitir_som(self):
        return "Au au!"
    def andar(self):
        return (f'{self.nome} está andando')
    def brincar(self):
        self.felicidade += 2
        return (f'{self.nome} está brincando')