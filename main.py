from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QDialog
from PySide6.QtGui import QPixmap
from UiPhotoEditor import Ui_MainWindow
from UiOpenURLDialog import Ui_Dialog
from PIL import Image, ImageFilter
import sys
import os
import tempfile
import requests


class PhotoEditor(QMainWindow):
    """Class representing a PhotoEditor window. Inherits from QMainWindow class"""
    def __init__(self):  # Constructor
        """Photo Editor constructor"""
        super(PhotoEditor, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui_dialog = None
        self.ui.setupUi(self)  # Applying UI from PhotoEditor.ui compiled as UiPhotoEditor.py

        # Fields
        self.image_path = None  # Path to current image file
        self.url = None  # URL to current image file
        self.temp_file_path = None  # Path to temporary image file
        self.dialog = None  # Dialog window

        # Connecting button signals with slots
        self.ui.openFileButton.clicked.connect(self.open_file)  # Open file button
        self.ui.openURLButton.clicked.connect(self.open_via_url)  # Open via URL button
        self.ui.saveFileButton.clicked.connect(self.save_file)  # Save file button
        self.ui.applyFilterButton.clicked.connect(self.apply_filter)  # Apply filter button
        self.ui.reflectVertButton.clicked.connect(self.reflect_vertically)  # Reflect vertically button
        self.ui.reflectHorizonButton.clicked.connect(self.reflect_horizontally)  # Reflect horizontally button
        self.ui.rotateButton.clicked.connect(self.rotate_90)  # Rotate button

    def open_file(self) -> None:  # Open file slot
        """Opening the file and saving its name in class field named 'image_path'"""
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Image File", "",
                                                   "Images (*.png *.jpg *.bmp)",
                                                   options=options)
        if file_name:
            self.image_path = file_name
            temp_file = tempfile.NamedTemporaryFile(suffix=os.path.splitext(self.image_path)[1], delete=False)
            self.temp_file_path = temp_file.name
            Image.open(self.image_path).save(self.temp_file_path)
            self.show_changes()

    def open_via_url(self) -> None:  # Open via url slot
        """Opening the dialog window for URL edit"""
        self.dialog = QDialog()
        self.ui_dialog = Ui_Dialog()
        self.ui_dialog.setupUi(self.dialog)  # Applying UI from OpenURLDialog.ui compiled as UiOpenURLDialog.py
        self.dialog.show()

        self.ui_dialog.URLButton.clicked.connect(self.open_url)  # Open URL button

        if self.ui_dialog.URLError.text():
            self.ui_dialog.URLError.setText("")  # Clearing error field

    def open_url(self) -> None:
        """Opening the image via url and saving it in temporary file"""
        self.url = self.ui_dialog.URLEdit.text()

        if self.url:
            response = None
            try:
                response = requests.get(self.url, stream=True).raw
            except requests.exceptions.RequestException as e:
                self.ui_dialog.URLEdit.setText(e)
            if response:
                try:
                    temp_file = tempfile.NamedTemporaryFile(suffix=os.path.splitext(self.url)[1], delete=False)
                    self.temp_file_path = temp_file.name
                    print(self.temp_file_path)
                    Image.open(response).save(self.temp_file_path)
                    self.show_changes()
                    self.dialog.hide()
                except IOError:
                    self.ui_dialog.URLEdit.setText("Unable to open Image")

    def show_changes(self) -> None:
        """Shows the changes of image after any edit options"""
        pixmap = QPixmap(self.temp_file_path)
        self.ui.imageWidget.setPixmap(pixmap.scaled(self.ui.imageWidget.size(),
                                                    Qt.AspectRatioMode.KeepAspectRatio,
                                                    Qt.TransformationMode.SmoothTransformation))

    def save_file(self) -> None:  # Save file slot
        """Saving the file in current directory"""
        if self.temp_file_path:
            options = QFileDialog.Options()
            save_path, _ = QFileDialog.getSaveFileName(self, "Save Image File", "",
                                                       "Images (*.png *.jpg *.bmp)",
                                                       options=options)
            if save_path:
                image = Image.open(self.temp_file_path)
                extension = os.path.splitext(save_path)[1].lower()
                if extension in ['.jpg', '.jpeg']:
                    image.save(save_path, format='JPEG')
                elif extension == '.png':
                    image.save(save_path, format='PNG')
                elif extension == '.bmp':
                    image.save(save_path, format='BMP')
                else:
                    image.save(save_path, format='PNG')

    def apply_filter(self) -> None:  # Apply filter slot
        """Applying chosen filter to a current image"""
        if self.temp_file_path:
            image = Image.open(self.temp_file_path)
            if self.ui.comboBox.currentText() == "Blur":
                image = image.filter(ImageFilter.BLUR)
            elif self.ui.comboBox.currentText() == "BoxBlur":
                image = image.filter(ImageFilter.BoxBlur(radius=50))
            elif self.ui.comboBox.currentText() == "Contour":
                image = image.filter(ImageFilter.CONTOUR)
            elif self.ui.comboBox.currentText() == "Detail":
                image = image.filter(ImageFilter.DETAIL)
            elif self.ui.comboBox.currentText() == "EdgeEnhance":
                image = image.filter(ImageFilter.EDGE_ENHANCE)
            elif self.ui.comboBox.currentText() == "EdgeEnhanceMore":
                image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
            elif self.ui.comboBox.currentText() == "Emboss":
                image = image.filter(ImageFilter.EMBOSS)
            elif self.ui.comboBox.currentText() == "FindEdges":
                image = image.filter(ImageFilter.FIND_EDGES)
            elif self.ui.comboBox.currentText() == "GaussianBlur":
                image = image.filter(ImageFilter.GaussianBlur)
            elif self.ui.comboBox.currentText() == "Kernel":
                image = image.filter(ImageFilter.Kernel((3, 3), (2, 2, 2, 2, 2, 2, 2, 2, 2)))
            elif self.ui.comboBox.currentText() == "Sharpen":
                image = image.filter(ImageFilter.SHARPEN)
            elif self.ui.comboBox.currentText() == "Smooth":
                image = image.filter(ImageFilter.SMOOTH)
            elif self.ui.comboBox.currentText() == "SmoothMore":
                image = image.filter(ImageFilter.SMOOTH_MORE)
            image.save(self.temp_file_path)
            self.show_changes()

    def reflect_vertically(self) -> None:  # Reflect vertically slot
        """Reflecting current image vertically"""
        if self.temp_file_path:
            image = Image.open(self.temp_file_path)
            image = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
            image.save(self.temp_file_path)
            self.show_changes()

    def reflect_horizontally(self) -> None:  # Reflect horizontally slot
        """Reflecting current image horizontally"""
        if self.temp_file_path:
            image = Image.open(self.temp_file_path)
            image = image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
            image.save(self.temp_file_path)
            self.show_changes()

    def rotate_90(self) -> None:  # Rotate slot
        """Rotating current image by 90 degrees"""
        if self.temp_file_path:
            image = Image.open(self.temp_file_path)
            image = image.transpose(Image.Transpose.ROTATE_270)
            image.save(self.temp_file_path)
            self.show_changes()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = PhotoEditor()
    window.show()

    sys.exit(app.exec())
