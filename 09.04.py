from PyQt5.QtWidgets import *

app = QApplication([])
window = QWidget()

mainline = QHBoxLayout()
window.setLayout(mainline)

line1 = QVBoxLayout()
line2 = QVBoxLayout()
mainline.addLayout(line1)
mainline.addLayout(line2)

b1 = QPushButton('Дальше')
tx1 = QLabel('Результат')
line1.addWidget(b1)
line2.addWidget(tx1)

tx1.hide()
#команда hide() - прячет объект
#команда show() - показывает
def next1():
    tx1.show()
    b1.hide()

b1.clicked.connect(next1)

window.show()
app.exec_()