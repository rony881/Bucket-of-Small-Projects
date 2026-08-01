import sys
from PyQt6.QtWidgets import QApplication ,QLineEdit,QMainWindow,QToolBar
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QProgressBar

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.default_url = "https://www.google.com/"
        self.setWindowTitle("My Browser")
        self.resize(1200, 800)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(self.default_url))
        self.setCentralWidget(self.browser)

        # Dark mode
        self.browser.page().runJavaScript("""
        document.body.style.backgroundColor = '#111';
        document.body.style.color = 'white';
        """)
        # Toolbar
        toolbar = QToolBar()
        self.addToolBar(toolbar)

        home_btn = QAction("Home", self)
        home_btn.triggered.connect(lambda x: self.browser.setUrl(QUrl(self.default_url)))

        back_btn = QAction("←", self)
        back_btn.triggered.connect(self.browser.back)

        forward_btn = QAction("→", self)
        forward_btn.triggered.connect(self.browser.forward)

        reload_btn = QAction("⟳", self)
        reload_btn.triggered.connect(self.browser.reload)

        toolbar.addAction(home_btn)
        toolbar.addAction(back_btn)
        toolbar.addAction(forward_btn)
        toolbar.addAction(reload_btn)
        
        # Address Bar
        self.address_bar = QLineEdit()
        self.address_bar.returnPressed.connect(self.load_url)

        toolbar.addWidget(self.address_bar)


        # Update Url
        self.browser.urlChanged.connect(self.update_url)
        self.browser.titleChanged.connect(self.setWindowTitle)

        # Progress bar
        self.progress = QProgressBar()
        self.progress.setMaximumHeight(2)
        self.progress.setTextVisible(False)
        toolbar.addWidget(self.progress)
        self.browser.loadProgress.connect(self.progress.setValue)

    def load_url(self):
        url = self.address_bar.text()

        if "." not in url:
            url = "https://www.google.com/search?q=" + url

        if not url.startswith("http"):
            url = "http://" + url
        self.browser.setUrl(QUrl(url))
    def update_url(self, q):
        self.address_bar.setText(q.toString())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Browser()
    window.show()
    sys.exit(app.exec())
