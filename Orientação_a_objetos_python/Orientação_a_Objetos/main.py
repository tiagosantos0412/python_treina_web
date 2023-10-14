from cachorro import Cachorro
from gato import Gato
from dono import Dono

cachorro = Cachorro("Cachorro", "Bela",  5, "Caramelo", "Salsichinha", dono=Dono('Vivi'))
print(cachorro.especie)
print(cachorro.nome)
print(cachorro.idade)
print(cachorro.cor)
print(cachorro.raca)
print(cachorro.emitir_som())
print(cachorro.andar())
print(cachorro.brincar())
print(cachorro.dono.nome)

gato = Gato("Gato", "Puff", 12, "Cinza", "Vira-lata", dono=Dono('Gigi'))
print(gato.especie)
print(gato.nome)
print(gato.idade)
print(gato.cor)
print(gato.raca)
print(gato.emitir_som())
print(gato.andar())
print(gato.brincar())
print(gato.dono.nome)
