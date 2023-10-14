#Trabalhando com Herança
from animal import Animal
from interface_animal import InterfaceAnimal
#Trabalhando com composição
from dono import Dono
class Gato(Animal, InterfaceAnimal):
    def __init__(self, especie, nome, idade, cor, raca, dono=Dono()):
        super().__init__(especie, nome, idade, cor, raca)
        self.__dono = dono

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
        return "O gato está brincando"