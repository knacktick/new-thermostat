from PyQt6 import QtWidgets
from PyQt6.QtCore import pyqtSlot, QTimer
from qasync import asyncSlot
from functools import wraps
import asyncio

class InfoBox(QtWidgets.QMessageBox):
    def __init__(self):
        super().__init__()
        self.setIcon(QtWidgets.QMessageBox.Icon.Information)

    @pyqtSlot(str, str)
    def display_info_box(self, title, text):
        self.setWindowTitle(title)
        self.setText(text)
        self.show()


class WarningBox(QtWidgets.QMessageBox):
    def __init__(self):
        super().__init__()
        self.setIcon(QtWidgets.QMessageBox.Icon.Warning)

    @pyqtSlot(str, str)
    def display_warning_box(self, title, text, detail_text):
        self.setWindowTitle(title)
        self.setText(text)
        self.setDetailedText(detail_text)
        self.show()