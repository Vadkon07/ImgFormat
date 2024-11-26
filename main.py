import os
import sys
import time
import ffmpeg
import qdarkstyle

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

app_version = '0.2.0'

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(f"ImgFormat {app_version}")
        self.setGeometry(100, 100, 400, 350)

        # Set up central widget and layout
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.widgetF = QLabel("Please, choose a file to convert in 'File' menu")
        widget_font = self.widgetF.font()
        widget_font.setPointSize(16)
        widget_font.setBold(True)
        self.widgetF.setFont(widget_font)
        self.widgetF.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        self.layout.addWidget(self.widgetF)

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

        #self.check_updates()

        # Create Status Bar
        self.statusBar().showMessage('Ready')

    def get_image_path(self):
        self.path, _ = QFileDialog.getOpenFileName(self, "Choose file to convert", "", "All Files (*);;Image Files (*.png *.jpg *.jpeg *.bmp)")
        if self.path:
            self.statusBar().showMessage(f'Selected file: {self.path}')
            print(self.path)
            self.widgetF.hide()
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

        # Input form and suggestions for her. Note that often special formats (raw, heif, etc.) don't work with some formats

        self.input = QLineEdit()
        self.input.setPlaceholderText("Enter format...")

        suggestions = ["png", "jpg", "webp", "heif", "svg", "tiff", "raw"]
        completer = QCompleter(suggestions)
        self.input.setCompleter(completer)

        self.input.setFixedWidth(150)
        self.layout.addWidget(self.input, alignment=Qt.AlignmentFlag.AlignCenter)

        # Add Start button
        button = QPushButton("Start", self)
        button.setFixedWidth(50)
        button.clicked.connect(self.convert_image)
        self.layout.addWidget(button, alignment=Qt.AlignmentFlag.AlignCenter)

        # Adjust window size if needed
        if scaled_pixmap.width() > self.width() or scaled_pixmap.height() > self.height():
            self.resize(scaled_pixmap.width() + 20, scaled_pixmap.height() + 60)

    def check_updates(self):
        try:
            url_fetch = 'https://raw.githubusercontent.com/Vadkon07/Splash/refs/heads/master/ver.html'
            current_version = app_version

            lines_with_word = self.fetch_lines_with_word(url_fetch, current_version)
            new_version = self.fetch_new_version(url_fetch)

            if not lines_with_word:
                self.new_update_notif(new_version)

        except Exception as e:
            dev_mode = 1
            QMessageBox.warning(self, "Error", f"Please, check your internet connection:\n\n\n {e}.")
            if dev_mode == 0: # Close app if dev mode is disabled
                exit()
            else: # Don't close app if dev mode is enabled
                print("DEV mode, skip error")

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

    custom_stylesheet_black = """
    QWidget {
        background-color: #1a1a1a;
        color: white;
    }
    QMenuBar {
        background-color: #1a1a1a;
        color: white;
    }
    QMenuBar::item {
        background-color: #1a1a1a;
    }
    QMenuBar::item:selected {
        background: #697565;
        color: white;
    }
    QPushButton {
        background-color: #97fff5;
        color: black;
    }
    QPushButton:hover {
        background-color: #00d4ff;
        color: black;
    }
    QMenu {
        background-color: #3C3D37;
        color: white;
    }
    QMenu::item {
        background-color: #3C3D37;
        color: white;
    }
    QProgressBar {
        border: 2px solid grey;
        text-align: center;
    }
    QProgressBar::chunk {
        background-color: #97fff5;
    }
   """

    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt6() + custom_stylesheet_black)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())

