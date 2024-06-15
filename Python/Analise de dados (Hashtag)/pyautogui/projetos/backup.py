# Importando a biblioteca
import pyautogui as py
# Dando alerta ao usuario
py.alert("Não mecha mais em nada do computador, para não interferir no resultado do codigo")
# Tempo de execução
py.PAUSE = 0.5
# Apertando o botão do windows
py.press("win")
# Pesquisando pelo navegador
py.write("google")
# Dando enter
py.press("enter")