import sqlite3
from PyQt5 import QtWidgets

databaseconnection = sqlite3.connect("users.db")

def qtPopup(title, text, icon, confirm=False):
    popup = QtWidgets.QMessageBox()
    dictionary_icons = {"Warning":popup.Warning,"Information":popup.Information, "Critical":popup.Critical, "Question":popup.Question}
    popup.setIcon(dictionary_icons[icon])
    popup.setWindowTitle(title)
    popup.setText(text)
    if confirm:
        botao_clicado = []
        popup.setStandardButtons(QtWidgets.QMessageBox.Cancel | QtWidgets.QMessageBox.Ok)
        def popup_clicked(i):
            botao_clicado.append(i.text())
        popup.buttonClicked.connect(popup_clicked)
        popup.exec()
        return botao_clicado[0]
    popup.exec()

def dbQuery(sql):
    cursor = databaseconnection.cursor() # Cursor
    cursor.execute(sql) # Executa o código SQL
    databaseconnection.commit() # Realiza alterações
    resultado = cursor.fetchall() # Busca tudo
    if resultado == []: # Verifica se está vazio
        return None # Retorna None se estiver vazio
    else: # Se não estiver vazio
        return resultado # Retorna o resultado
