from PySide6.QtCore import Qt, QPoint
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QDialog
from PySide6.QtGui import QPixmap, QPainter, QPen, QColor
from UiPhotoEditor import Ui_MainWindow
from UiOpenURLDialog import Ui_Dialog
from PIL import Image, ImageFilter
import sys
import os
import tempfile
import requests
import shutil


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
        self.back_file_path = None  # Temporary image for zooming or dragging other images
        self.dialog = None  # Dialog window
        self.overlay_image = None  # Overlay image
        self.overlay_position = QPoint(0, 0)  # Overlay image position
        self.scale_factor = 1.0  # For scaling some images
        self.undo_stack = []  # Stack for undo operations

        # For mouse events
        self.is_dragging = False
        self.drag_start_position = None

        # For painting
        self.is_painting = False
        self.last_point = None
        self.color = QColor(0, 0, 0)  # Default color black

        # Connecting button signals with slots
        self.ui.undoButton.clicked.connect(self.undo_changes)  # Undo changes button
        self.ui.brushButton.clicked.connect(self.start_painting)  # Brush button
        self.ui.openFileButton.clicked.connect(self.open_file)  # Open file button
        self.ui.pasteImageButton.clicked.connect(self.choose_image_to_paste)  # Paste image button
        self.ui.openURLButton.clicked.connect(self.open_via_url)  # Open via URL button
        self.ui.saveFileButton.clicked.connect(self.save_file)  # Save file button
        self.ui.applyFilterButton.clicked.connect(self.apply_filter)  # Apply filter button
        self.ui.reflectVertButton.clicked.connect(self.reflect_vertically)  # Reflect vertically button
        self.ui.reflectHorizonButton.clicked.connect(self.reflect_horizontally)  # Reflect horizontally button
        self.ui.rotateButton.clicked.connect(self.rotate_90)  # Rotate button

    def mousePressEvent(self, event):  # Mouse press slot
        """Mouse pressing processor"""
        if event.button() == Qt.MouseButton.LeftButton:
            self.is_dragging = True
            if self.overlay_image:
                self.drag_start_position = event.position()
            elif self.is_painting:
                self.last_point = event.position().toPoint()

    def mouseMoveEvent(self, event):  # Mouse move slot
        """Mouse moving processor"""
        if self.is_dragging:
            if self.overlay_image:
                delta = event.position() - self.drag_start_position
                self.overlay_position += delta.toPoint()
                self.drag_start_position = event.position()
                self.paste_image()
            elif self.is_painting:
                pixmap = self.ui.imageWidget.pixmap()
                if pixmap:
                    painter = QPainter(pixmap)
                    pen = QPen(self.color, 3, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap, Qt.PenJoinStyle.RoundJoin)
                    painter.setPen(pen)
                    painter.drawLine(self.last_point, event.position().toPoint())
                    self.last_point = event.position().toPoint()
                    painter.end()
                    self.ui.imageWidget.setPixmap(pixmap)

    def mouseReleaseEvent(self, event):  # Mouse release slot
        """Mouse releasing processor"""
        if event.button() == Qt.MouseButton.LeftButton:
            self.is_dragging = False
            if self.is_painting:
                self.is_painting = False
                pixmap = self.ui.imageWidget.pixmap()
                if pixmap:
                    pixmap.save(self.temp_file_path)
                self.save_state()
                self.show_changes()

    def wheelEvent(self, event):  # Mouse wheel slot
        """Mouse wheel processor"""
        if self.overlay_image:
            angle = event.angleDelta().y()
            if angle > 0:
                self.scale_factor *= 1.1
            else:
                self.scale_factor /= 1.1
            new_width = int(self.overlay_image.width * self.scale_factor)
            new_height = int(self.overlay_image.height * self.scale_factor)
            self.overlay_image = self.overlay_image.resize((new_width, new_height))
            self.scale_factor = 1.0
            self.paste_image()

    def keyPressEvent(self, event):  # Keyboard slot
        """Key pressing processor"""
        if event.key() == Qt.Key.Key_Enter or event.key() == Qt.Key.Key_Return:
            self.overlay_image = None
            self.overlay_position = QPoint(0, 0)

    def show_changes(self) -> None:  # Show changes after image edit
        """Shows the changes of image after any edit options"""
        pixmap = QPixmap(self.temp_file_path)
        self.ui.imageWidget.setPixmap(pixmap.scaled(self.ui.imageWidget.size(),
                                                    Qt.AspectRatioMode.KeepAspectRatio,
                                                    Qt.TransformationMode.SmoothTransformation))

    def save_state(self) -> None:  # Save current state for undo
        """Saves the current state of the image for undo functionality"""
        if self.temp_file_path:
            state_path = tempfile.mktemp(suffix=os.path.splitext(self.temp_file_path)[1])
            shutil.copy2(self.temp_file_path, state_path)
            self.undo_stack.append(state_path)
            if len(self.undo_stack) > 10:  # Limit the stack size to 10
                os.remove(self.undo_stack.pop(0))

    def undo_changes(self) -> None:  # Undo changes slot
        """Cancels the changes by one step"""
        if self.undo_stack:
            last_state = self.undo_stack.pop()
            shutil.copy2(last_state, self.temp_file_path)
            os.remove(last_state)
            self.show_changes()

    def start_painting(self) -> None:  # Start to paint on image with chosen color
        """Paint start function"""
        color_name = self.ui.colorBox.currentText()
        self.color = QColor(color_name)
        self.is_painting = True

    def open_file(self) -> None:  # Open file slot
        """Opening the file and saving its name in class field named 'image_path'"""
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Image File", "",
                                                   "Images (*.png *.jpg *.bmp)",
                                                   options=options)
        if file_name:
            self.image_path = file_name
            temp_file = tempfile.NamedTemporaryFile(prefix="photo_editor_temp_",
                                                    suffix=os.path.splitext(self.image_path)[1],
                                                    delete=False)
            back_file = tempfile.NamedTemporaryFile(prefix="photo_editor_back_",
                                                    suffix=os.path.splitext(self.image_path)[1],
                                                    delete=False)
            self.back_file_path = back_file.name
            self.temp_file_path = temp_file.name
            Image.open(self.image_path).save(self.temp_file_path)
            Image.open(self.image_path).save(self.back_file_path)
            self.save_state()
            self.show_changes()

    def choose_image_to_paste(self) -> None:  # Place Image slot
        """Choosing an image to paste"""
        if self.temp_file_path:
            options = QFileDialog.Options()
            file_name, _ = QFileDialog.getOpenFileName(self, "Open Image File", "",
                                                       "Images (*.png *.jpg *.bmp)",
                                                       options=options)
            if file_name:
                self.overlay_image = Image.open(file_name)
                self.overlay_position = QPoint(0, 0)
                self.paste_image()

    def paste_image(self) -> None:
        """Pasting new image on current image"""
        if self.overlay_image:
            image = Image.open(self.back_file_path)
            overlay_geometry = (self.overlay_position.x(), self.overlay_position.y())
            overlay_image_resized = self.overlay_image.resize(
                (min(image.width - overlay_geometry[0], self.overlay_image.width),
                 min(image.height - overlay_geometry[1], self.overlay_image.height)),
                Image.Resampling.LANCZOS)
            image.paste(overlay_image_resized, overlay_geometry, overlay_image_resized.convert('RGBA'))
            image.save(self.temp_file_path)
            self.save_state()
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
            try:
                response = requests.get(self.url, stream=True)
                response.raise_for_status()
                response.raw.decode_content = True
                temp_file = tempfile.NamedTemporaryFile(suffix=os.path.splitext(self.url)[1], delete=False)
                self.temp_file_path = temp_file.name
                Image.open(response.raw).save(self.temp_file_path)
                self.save_state()
                self.show_changes()
                self.dialog.hide()
            except requests.exceptions.RequestException as e:
                self.ui_dialog.URLError.setText(str(e))
            except IOError:
                self.ui_dialog.URLError.setText("Unable to open Image")

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
            self.save_state()
            filter_name = self.ui.filterBox.currentText()
            filters = {
                "Blur": ImageFilter.BLUR,
                "BoxBlur": ImageFilter.BoxBlur(50),
                "Contour": ImageFilter.CONTOUR,
                "Detail": ImageFilter.DETAIL,
                "EdgeEnhance": ImageFilter.EDGE_ENHANCE,
                "EdgeEnhanceMore": ImageFilter.EDGE_ENHANCE_MORE,
                "Emboss": ImageFilter.EMBOSS,
                "FindEdges": ImageFilter.FIND_EDGES,
                "GaussianBlur": ImageFilter.GaussianBlur,
                "Kernel": ImageFilter.Kernel((3, 3), (2, 2, 2, 2, 2, 2, 2, 2, 2)),
                "Sharpen": ImageFilter.SHARPEN,
                "Smooth": ImageFilter.SMOOTH,
                "SmoothMore": ImageFilter.SMOOTH_MORE,
            }
            image = image.filter(filters.get(filter_name, ImageFilter.SMOOTH))
            image.save(self.temp_file_path)
            self.show_changes()

    def reflect_vertically(self) -> None:  # Reflect vertically slot
        """Reflecting current image vertically"""
        if self.temp_file_path:
            image = Image.open(self.temp_file_path)
            self.save_state()
            image = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
            image.save(self.temp_file_path)
            self.show_changes()

    def reflect_horizontally(self) -> None:  # Reflect horizontally slot
        """Reflecting current image horizontally"""
        if self.temp_file_path:
            image = Image.open(self.temp_file_path)
            self.save_state()
            image = image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
            image.save(self.temp_file_path)
            self.show_changes()

    def rotate_90(self) -> None:  # Rotate slot
        """Rotating current image by 90 degrees"""
        if self.temp_file_path:
            image = Image.open(self.temp_file_path)
            self.save_state()
            image = image.transpose(Image.Transpose.ROTATE_270)
            image.save(self.temp_file_path)
            self.show_changes()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = PhotoEditor()
    window.show()

    sys.exit(app.exec())
