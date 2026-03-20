from PyQt6.QtCore import Qt, QSettings
from PyQt6.QtWidgets import  (QWidget, QLabel, QLineEdit)

class StateWindow(QWidget):
  def __init__(self, parent=None):
    super().__init__(parent, Qt.WindowType.Window)
    self.setWindowTitle("Statistics")
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
    
    self.UsingTime = QLabel("Today you use: ", self)
    self.UsingTime.move(15, 55)

    self.parentName.setText(self.settings.value("parent_name", ""))
    self.childName.setText(self.settings.value("parent_name", ""))


  def closeEvent(self, event):
    self.settings.setValue("parent_name", self.parentName.text())
    self.settings.setValue("child_name", self.childName.text())
    super().closeEvent(event)

class BlacklistWindow(QWidget):
  def __init__(self, parent=None):
    super().__init__(parent, Qt.WindowType.Window)
    self.setWindowTitle("Blacklist")
    self.resize(480, 270)

    # self.input_field = QLineEdit()
    # self.input_field.setPlaceholderText(". . .")
    # self.safe_btn = QPushButton("Save")
    # self.safe_btn.clicked.connect(self.save_data)