import abc
class Interface_Passagem(abc.ABC):
    @abc.abstractmethod
    def confirmar_compra(self):
        pass

    @abc.abstractmethod
    def cancelar_compra(self):
        pass

