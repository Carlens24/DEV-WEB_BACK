class cliente:
    def __init__(self, nome, idade, email, plano):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.planos = ["basic", "Premium"]
        if plano in self.planos:
            self.plano = plano
        else:
            print("Plano invalido!!!!!!")  
            
            
    def mudar_plano(self, novo_plano):
        if novo_plano in self.planos:
            self.plano = novo_plano
        else:
            print("Plano invalido!!!!")  
            
            
    def filmes(self, filme, plano_filmes):
        if self.plano == plano_filmes:
            print(f"Acessar filme {filme}!!!") 
        elif self.plano == "Premium":
            print(f"Acessar filme {filme}!!!") 
        elif self.plano == "basic" and plano_filmes == "Premium":
            print("Atualize seu plano para ter acesso a este filmes!!!")
        else:
            print("Plano invalido!!!")
            
            
cliente = cliente("carlens", "15", "carlensoslin@gmail.com", "basic") 
print(cliente.plano)     
cliente.filmes("Harry potter", "Premium")

cliente.mudar_plano("Premium")
print(cliente.plano) 
cliente.filmes("Harry potter", "Premium")
