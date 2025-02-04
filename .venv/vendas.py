
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox
from PyQt5.QtCore import Qt

class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Finalizar Venda")
        self.setGeometry(500, 30, 648, 380)

        layout_principal = QVBoxLayout()
        layout_meio = QHBoxLayout()
        layout_esquerda = QVBoxLayout()
        layout_direita = QVBoxLayout()
        layout_inferior = QHBoxLayout()
        layout_botoes_centro = QVBoxLayout()
        layout_botoes_direita = QVBoxLayout()

        # Título
        titulo = QLabel("Finalizar Venda")
        titulo.setStyleSheet("font-size: 18px")
        layout_principal.addWidget(titulo)

        # Campos do lado esquerdo
        def criar_linha(texto, valor):
            linha = QHBoxLayout()
            linha.addWidget(QLabel(texto))
            campo = QLineEdit(valor)
            campo.setAlignment(Qt.AlignRight)
            linha.addWidget(campo)
            return linha

        for texto, valor in [
            ("Total da Venda:", "R$ 500,00"),
            ("Desconto:", "R$ 0,00"),
            ("Acréscimo:", "R$ 0,00"),
            ("Total Líquido:", "R$ 600,00"),
            ("Troco:", "R$ 0,00")
        ]:
            layout_esquerda.addLayout(criar_linha(texto, valor))

        # Campos do lado direito
        layout_direita.addLayout(criar_linha("Cliente:", "1 -CONSUMIDOR FINAL"))
        layout_direita.addLayout(criar_linha("Vendedor:", "500 - SYNDATA"))

        layout_pagamento = QHBoxLayout()
        layout_pagamento.addWidget(QLabel("Forma de Pagto:"))
        combo = QComboBox()
        combo.addItems(["1 -DINHEIRO", "2 -CARTÃO", "3 -DÉBITO"])
        layout_pagamento.addWidget(combo)
        campo_valor = QLineEdit("R$ 0,00")
        campo_valor.setAlignment(Qt.AlignRight)
        layout_pagamento.addWidget(campo_valor)
        layout_direita.addLayout(layout_pagamento)

        campo_grande = QLineEdit("1-DINHEIRO 100,00")
        campo_grande.setFixedSize(285, 100)
        campo_grande.setAlignment(Qt.AlignTop)
        layout_direita.addWidget(campo_grande)

        layout_meio.addLayout(layout_esquerda)
        layout_meio.addLayout(layout_direita)
        layout_principal.addLayout(layout_meio)

        # Texto inferior
        texto_inferior = QLabel("Selecione o Documento para emissão:")
        texto_inferior.setAlignment(Qt.AlignCenter)
        layout_principal.addWidget(texto_inferior)

        # Botões inferiores
        layout_inferior.addWidget(QPushButton("(Esc) Sair"))
        layout_botoes_centro.addWidget(QPushButton("(F6) Cupom Fiscal"))
        layout_botoes_centro.addWidget(QPushButton("(F8) NFC-e Online"))
        layout_botoes_direita.addWidget(QPushButton("(F7) Pedido de Venda"))
        layout_botoes_direita.addWidget(QPushButton("(F9) NFC-e Offline"))

        layout_inferior.addLayout(layout_botoes_centro)
        layout_inferior.addLayout(layout_botoes_direita)
        layout_principal.addLayout(layout_inferior)

        widget = QWidget()
        widget.setLayout(layout_principal)
        self.setCentralWidget(widget)

app = QApplication(sys.argv)
window = JanelaPrincipal()
window.show()
app.exec()
