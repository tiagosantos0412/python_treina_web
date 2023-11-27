import abc
class Animal(abc.ABC):
    def __init__(self, nome, idade, cor, raca, felicidade=0):
        self.__nome = nome
        self.__idade = idade
        self.__cor = cor
        self.__raca = raca
        self.__felicidade = felicidade

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

    @property
    def felicidade(self):
        return self.__felicidade

    @felicidade.setter
    def felicidade(self, felicidade):
        self.__felicidade = felicidade

