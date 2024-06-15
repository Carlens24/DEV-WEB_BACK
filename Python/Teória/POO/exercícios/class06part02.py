from class06 import Escritor
from class06 import Caneta
from class06 import MaquinaEscrever


escritor = Escritor("Oslin")
caneta = Caneta("Bic")
maquina = MaquinaEscrever()

escritor.ferramenta = maquina
escritor.ferramenta.escrever()

del escritor
print(caneta.marca)
maquina.escrever()