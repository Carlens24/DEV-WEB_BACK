class ControleRemoto:
    def __init__(self, cor, altura, profundidade, largura):
        self.cor = cor
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura
        
    def volume(self, botao):
        if botao == "+":
            print("Aumentando o volume")
        elif botao == "-":
            print("Diminuindo o volume")  
    
remote_cont1 = ControleRemoto("preto", "20cm", "2cm", "2cm")
print(remote_cont1.cor)
remote_cont1.volume("+")

remote_cont2 = ControleRemoto("cinza", "10cm", "2cm", "2cm")
print(remote_cont2.cor)
remote_cont2.volume("-")