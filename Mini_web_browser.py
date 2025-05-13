import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView


class MiniBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mini Web Browser")
        self.setGeometry(100, 100, 1000, 700)

        self.browser = QWebEngineView()
        self.browser.setUrl("https://www.google.com")

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.load_url)

        go_button = QPushButton("Go")
        go_button.clicked.connect(self.load_url)

        layout = QVBoxLayout()
        layout.addWidget(self.url_bar)
        layout.addWidget(go_button)
        layout.addWidget(self.browser)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def load_url(self):
        url = self.url_bar.text()
        if not url.startswith("http"):
            url = "http://" + url
        self.browser.setUrl(url)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MiniBrowser()
    window.show()
    sys.exit(app.exec_())
