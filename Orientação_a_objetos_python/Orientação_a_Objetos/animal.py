# class Animal:
#     def __init__(self, especie, nome, idade, cor, raca):
#         self.especie = especie
#         self.nome = nome
#         self.idade = idade
#         self.cor = cor
#         self.raca = raca

#O @property é equivalente ao getter de outras linguagens
#O @atributo.setter é equivalente ao setter de outras linguagens

#Trabalhando com atributos privados e protegidos
#Utlilizando a Classe Animal como classe abstrata

import abc
class Animal(abc.ABC):
    def __init__(self, especie, nome, idade, cor, raca):
        self.__especie = especie
        self.__nome = nome
        self.__idade = idade
        self.__cor = cor
        self.__raca = raca

    @property
    def especie(self):
        return self.__especie

    @especie.setter
    def especie(self, especie):
        self.__especie = especie

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def idade(self):
        return self.__idade
    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    @property
    def cor(self):
        return self.__cor

    @cor.setter
    def cor(self, cor):
        self.__cor = cor

    @property
    def raca(self):
        return self.__raca

    @raca.setter
    def raca(self, raca):
        self.__raca = raca

    @abc.abstractmethod
    def emitir_som(self):
        pass