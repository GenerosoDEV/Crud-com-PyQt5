from PyQt5 import uic, QtWidgets
from qtui import ui_listausuarios, ui_login, ui_main, ui_registro 
import utils

with open('session.txt', 'w') as f:
    f.write("")

utils.dbQuery("""CREATE TABLE IF NOT EXISTS users (
    uid            INTEGER PRIMARY KEY AUTOINCREMENT,
    privLevel      INT     DEFAULT (1),
    usuario        TEXT,
    senha          TEXT,
    nome           TEXT,
    datanascimento DATE,
    cpf            TEXT,
    email          TEXT,
    numerocelular  BIGINT 
);
""")

import sys
app = QtWidgets.QApplication(sys.argv)

ui_login.showWindow()

sys.exit(app.exec_())
