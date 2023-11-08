import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QFileDialog, QPushButton, QVBoxLayout, QWidget

from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class ImageOpener(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Image Opener')
        self.setGeometry(400, 400, 800, 800)
        self.setWindowTitle().setStyleSheet("background-color: #333; color: #fff; font-size: 12px; font-weight: bold;")

        self.open_button = QPushButton('Open Image', self)
        self.open_button.clicked.connect(self.open_image_dialog)

        self.exit_button = QPushButton('Exit', self)
        self.exit_button.clicked.connect(self.close)

        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(self.open_button)
        layout.addWidget(self.exit_button)
        layout.addWidget(self.label)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.status_label = QLabel('Akif', self)  
        self.statusBar().addWidget(self.status_label, 1)  
        self.status_label.setAlignment(Qt.AlignCenter)
        self.statusBar().setStyleSheet("background-color: #333; color: #fff; font-size: 12px; font-weight: bold;")

    def open_image_dialog(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Image Files (*.png *.jpg *.bmp, *.jpeg)")
        pixmap = QPixmap(file_path)
        pixmap = pixmap.scaled(800, 800, Qt.AspectRatioMode.KeepAspectRatio, Qt.SmoothTransformation)
        self.label.setPixmap(pixmap)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ImageOpener()
    window.show()
    sys.exit(app.exec_())
