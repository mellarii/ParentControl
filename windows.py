from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import  (QWidget, QLabel)

class StateWindow(QWidget):
  def __init__(self, parent=None):
    super().__init__(parent, Qt.WindowType.Window)
    self.setWindowTitle("Statistics")
    self.resize(480, 270)
    self.parentName = QLabel("Parent: ", self)
    self.parentName.move(15, 15)
    self.childName = QLabel("Child: ", self)
    self.childName.move(15, 35)
    self.UsingTime = QLabel("Today you use: ", self)
    self.UsingTime.move(15, 55)

class BlacklistWindow(QWidget):
  def __init__(self, parent=None):
    super().__init__(parent, Qt.WindowType.Window)
    self.setWindowTitle("Blacklist")
    self.resize(480, 270)