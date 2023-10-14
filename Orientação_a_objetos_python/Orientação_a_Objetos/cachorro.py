#Trabalhando com construtores
# class Cachorro:
#     def __init__(self, nome, idade, cor, raca):
#         self.nome = nome
#         self.idade = idade
#         self.cor = cor
#         self.raca = raca
#
#     def latir(self):
#         return "au au"

#Trabalhando com Herança
from animal import Animal
from interface_animal import InterfaceAnimal
#Trabalhando com composição
from dono import Dono
class Cachorro(Animal, InterfaceAnimal):
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
        return "Au au!"
    def andar(self):
        return (f'{self.nome} está andando')
    def brincar(self):
        return (f'{self.nome} está brincando')