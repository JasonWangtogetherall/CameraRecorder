from PySide2.QtCore import Signal, Qt
from PySide2.QtWidgets import QDialog


class DialogBase(QDialog):

    closed = Signal()

    def __init__(self, parent):
        super().__init__(parent)
        self.app = parent

    def closeEvent(self, event):
        getattr(self.closed, "emit")()
