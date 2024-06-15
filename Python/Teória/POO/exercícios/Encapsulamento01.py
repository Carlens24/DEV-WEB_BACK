# Publico
class Aluno:
    def __init__(self, nome, nota01, nota02, nota03):
        self.nome = nome
        self.nota01 = nota01
        self.nota02 = nota02
        self.nota03 = nota03

aluno = Aluno("Carlens", "90", "80", "10")
print(aluno.nome)

# Protected
class Aluno:
    def __init__(self, nome, nota01, nota02, nota03):
        self._nome = nome
        self._nota01 = nota01
        self._nota02 = nota02
        self._nota03 = nota03

aluno = Aluno("Carlens", "90", "80", "10")
print(aluno._nome)

# Private
class Aluno:
    def __init__(self, nome, nota01, nota02, nota03):
        self.__nome = nome
        self.__nota01 = nota01
        self.__nota02 = nota02
        self.__nota03 = nota03

aluno = Aluno("Carlens", "90", "80", "10")
print(aluno.__nome)

