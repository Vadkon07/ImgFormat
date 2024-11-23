import os
import sys
import time
import ffmpeg

from PyQt6.QtGui import QAction, QIcon, QPixmap
from PyQt6.QtWidgets import (
    QApplication,
    QFileDialog,
    QMainWindow,
    QToolBar,
    QLabel,
    QVBoxLayout,
    QWidget,
    QMenuBar,
    QStatusBar,
    QPushButton,
    QCompleter,
    QLineEdit,
    QMessageBox
)
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ImgFormat")
        self.setGeometry(100, 100, 600, 400)

        # Set up central widget and layout
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Create and add QLabel
        self.label = QLabel('Please, choose a file to convert')
        self.layout.addWidget(self.label, alignment=Qt.AlignmentFlag.AlignCenter)

        # Create Menu Bar
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('File')

        # Add actions to the File menu
        open_action = QAction('Open', self)
        open_action.triggered.connect(self.get_image_path)
        file_menu.addAction(open_action)

        exit_action = QAction('Exit', self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # Create Status Bar
        self.statusBar().showMessage('Ready')

    def get_image_path(self):
        self.path, _ = QFileDialog.getOpenFileName(self, "Choose file to convert", "", "All Files (*);;Image Files (*.png *.jpg *.jpeg *.bmp)")
        if self.path:
            self.statusBar().showMessage(f'Selected file: {self.path}')
            print(self.path)
            self.label.hide()
            self.show_image(self.path)

    def show_image(self, path):
        image_label = QLabel(self.central_widget)
        pixmap = QPixmap(path)

        scaled_pixmap = pixmap.scaled(360, 480, Qt.AspectRatioMode.KeepAspectRatio)
        image_label.setPixmap(scaled_pixmap)

        # Clear the layout and add the image label in a centered position
        for i in reversed(range(self.layout.count())):
            widget_to_remove = self.layout.itemAt(i).widget()
            self.layout.removeWidget(widget_to_remove)
            widget_to_remove.setParent(None)

        self.layout.addWidget(image_label, alignment=Qt.AlignmentFlag.AlignCenter)

        self.input = QLineEdit()
        self.input.setPlaceholderText("Enter format...")

        suggestions = ["png", "jpg", "webp", "heif", "svg", "tiff", "raw"]
        completer = QCompleter(suggestions)
        self.input.setCompleter(completer)

        self.input.setFixedWidth(100)
        self.layout.addWidget(self.input, alignment=Qt.AlignmentFlag.AlignCenter)

        # Add Start button
        button = QPushButton("Start", self)
        button.clicked.connect(self.convert_image)
        self.layout.addWidget(button, alignment=Qt.AlignmentFlag.AlignCenter)

        # Adjust window size if needed
        if scaled_pixmap.width() > self.width() or scaled_pixmap.height() > self.height():
            self.resize(scaled_pixmap.width() + 20, scaled_pixmap.height() + 60)

    def convert_image(self):
        chosen_format = self.input.text()
        QMessageBox.information(self, "Conversion Started", f"Conversion to {chosen_format} started...")

        output_path = os.path.splitext(self.path)[0] + f'.{chosen_format}'

        try:
            (
                ffmpeg.input(self.path)
                .output(output_path)
                .run()
            )
            QMessageBox.information(self, "Conversion Completed", f"Conversion to {chosen_format} completed: {output_path}")
        except Exception as e:
            QMessageBox.critical(self, "Conversion Error", f"An error occurred: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("ImgFormat")

    window = MainWindow()
    window.show()
    sys.exit(app.exec())

