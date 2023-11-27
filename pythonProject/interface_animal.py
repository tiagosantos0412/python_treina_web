#Trabalhando com interfaces
import abc
class InterfaceAnimal(abc.ABC):
    @abc.abstractmethod
    def emitir_som(self):
        pass
    @abc.abstractmethod
    def andar(self):
        pass
    @abc.abstractmethod
    def brincar(self):
        pass
