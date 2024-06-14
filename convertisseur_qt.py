import sys
from concurrent.futures import ThreadPoolExecutor

import requests
from PyQt5.QtWidgets import (
    QApplication,
    QComboBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


def get_crypto_rates(name):
    import time

    time.sleep(10)
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": name, "vs_currencies": "eur"}
    response = requests.get(url, params=params)
    return response.json()[name]["eur"]


class Converter(QWidget):
    def __init__(self):
        super().__init__()

        self.executor = ThreadPoolExecutor()

        self.setWindowTitle("Crypto to EUR Converter")
        main_layout = QVBoxLayout()
        form_layout = QHBoxLayout()
        button_layout = QVBoxLayout()

        select_label = QLabel("Select cryptocurrency:")
        self.crypto_list = QComboBox()
        self.crypto_list.addItems(["bitcoin", "ethereum", "litecoin"])

        amount_label = QLabel("Enter amount:")
        self.amount_input = QLineEdit()

        self.result_label = QLabel("")

        form_layout.addWidget(select_label)
        form_layout.addWidget(self.crypto_list)
        form_layout.addWidget(amount_label)
        form_layout.addWidget(self.amount_input)
        form_layout.addWidget(self.result_label)

        button = QPushButton("Convert")
        button_layout.addWidget(button)
        button.clicked.connect(self.calculate_in_thread)

        main_layout.addLayout(form_layout)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)
        self.show()

    def calculate(self):
        coin_name = self.crypto_list.currentText()
        amount = float(self.amount_input.text())
        rate = get_crypto_rates(coin_name)
        result = amount * rate
        self.result_label.setText(f"{result}€")

    def calculate_in_thread(self):
        self.executor.submit(self.calculate)


app = QApplication(sys.argv)
ui = Converter()
sys.exit(app.exec_())
