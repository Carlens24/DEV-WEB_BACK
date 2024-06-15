class Musico:
    def tocar(self):
        pass

class Guitarrista(Musico):
    def tocar(self):
        return "Tocando a minha guitarra!"

class Baterista(Musico):
    def tocar(self):
        return "Tocando a minha bateria!"

class Pianista(Musico):
    def tocar(self):
        return "Tocando meu piano!"
   
class Violinista(Musico):
     def tocar(self):
          return "Tocando Meu violino!"   

# Agora, vamos criar alguns músicos e pedir para eles tocarem
guitarrista = Guitarrista()
baterista = Baterista()
pianista = Pianista()
violinista = Violinista()

musicos = [guitarrista, baterista, pianista, violinista]

for musico in musicos:
    print(musico.tocar())
