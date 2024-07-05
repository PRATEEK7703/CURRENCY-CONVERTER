from PyQt6.QtWidgets import QApplication,QWidget,QVBoxLayout,QLabel,QPushButton,QLineEdit,QComboBox,QHBoxLayout
from PyQt6.QtCore import Qt
from bs4 import BeautifulSoup
import requests

def get_currency(in_currency,out_currency):
  url=f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1'
  content=requests.get(url).text
  soup=BeautifulSoup(content,'html.parser')
  rate=soup.find("span",class_="ccOutputRslt").get_text()
  rate=float(rate[:-4])
  return rate


def show_currency():
    input_text=float(text.text())
    in_cur=in_combo.currentText()
    target_cur=target_combo.currentText()
    rate=get_currency(in_cur,target_cur)
    output=input_text*rate
    output_label.setText(str(input_text)+" "+in_cur+"="+str(output)+" "+target_cur)


app=QApplication([])
window=QWidget()
window.setWindowTitle('Currency Converter')

layout=QVBoxLayout()

layout1=QHBoxLayout()
layout.addLayout(layout1)

output_label=QLabel('')
layout.addWidget(output_label)

layout2=QVBoxLayout()
layout1.addLayout(layout2)

layout3=QVBoxLayout()
layout1.addLayout(layout3)

in_combo=QComboBox()
currencies = ['USD', 'EUR', 'INR', 'NPR', 'GBP', 'JPY', 'CAD', 'AUD', 'CHF', 'CNY']
in_combo.addItems(currencies)
layout2.addWidget(in_combo)

target_combo=QComboBox()
target_combo.addItems(currencies)
layout2.addWidget(target_combo)


text=QLineEdit()
layout3.addWidget(text)

btn=QPushButton('Convert')
layout3.addWidget(btn,alignment=Qt.AlignmentFlag.AlignBottom)
btn.clicked.connect(show_currency)



window.setLayout(layout)
window.show()
app.exec()