from PyQt6.QtCore import Qt, QSettings
from PyQt6.QtWidgets import  QWidget, QLabel, QLineEdit

class SettingsWindow(QWidget):
  def __init__(self, parent=None):
    super().__init__(parent, Qt.WindowType.Window)
    self.setWindowTitle("Settings")
    self.resize(480, 270)
    self.settings = QSettings("Mellarii", "ParentControl")
    
    self.parentLabel = QLabel("Parent: ", self)
    self.parentLabel.move(15, 15)
    self.parentName = QLineEdit(self)
    self.parentName.setPlaceholderText(" Name ")
    self.parentName.move(57, 10)

    self.childLabel = QLabel("Child: ", self)
    self.childLabel.move(15, 35)
    self.childName = QLineEdit(self)
    self.childName.setPlaceholderText(" Name ")
    self.childName.move(57, 30)

    self.parentName.setText(self.settings.value("parent_name", ""))
    self.childName.setText(self.settings.value("child_name", ""))

  def closeEvent(self, event):
    self.settings.setValue("parent_name", self.parentName.text())
    self.settings.setValue("child_name", self.childName.text())
    super().closeEvent(event)