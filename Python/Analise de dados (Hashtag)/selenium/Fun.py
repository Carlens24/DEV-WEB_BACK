import os
from tkinter.filedialog import askdirectory as ask

path = ask(title="Selecione a pasta desejada")
print(path)

arquivos = os.listdir(path)
print(arquivos)

locais = {
     "Pdf": [".pdf"],
     "Excel": [".xlsx"],
     "Python": [".py"],
     "Word": [".docx"],
     "Jupyter": [".ipynb"],
     "PNG": [".png"] 
}

for arquivo in arquivos:
     nome, extensao = os.path.splitext(f"{path}/{arquivo}")
     for pasta in locais:
          if extensao in locais[pasta]: 
               if not os.path.exists(f"{path}/{arquivo}"):
                    os.makedirs(f"{path}/{arquivo}")
               os.rename(f"{path}/{arquivo}", f"{path}/{pasta}/{arquivo}")  