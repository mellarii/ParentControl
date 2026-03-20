import json
import os

from PyQt6.QtCore import Qt, QSettings
from PyQt6.QtWidgets import  (QWidget, QLabel, QLineEdit, QPushButton, QMessageBox)

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
    self.childName.setText(self.settings.value("parent_name", ""))

  def closeEvent(self, event):
    self.settings.setValue("parent_name", self.parentName.text())
    self.settings.setValue("child_name", self.childName.text())
    super().closeEvent(event)


class StateWindow(QWidget):
  def __init__(self, parent=None):
    super().__init__(parent, Qt.WindowType.Window)
    self.setWindowTitle("Statistics")
    self.resize(480, 270)
    
    self.UsingTime = QLabel("Today you use: ", self)
    self.UsingTime.move(15, 55)


class BlacklistWindow(QWidget):
  def __init__(self, parent=None):
    super().__init__(parent, Qt.WindowType.Window)
    self.setWindowTitle("Blacklist")
    self.resize(480, 270)

    self.blackFile_path = "blacklist.json"
    self.sites = self.load_data()

    self.input_field = QLineEdit(self)
    self.input_field.setPlaceholderText("Input site to add.")
    self.input_field.setGeometry(20, 20, 260, 30)

    self.add_btn = QPushButton("Add site",self)
    self.add_btn.move(20, 57)
    self.add_btn.clicked.connect(self.add_site)

    self.delete_btn = QPushButton("Delete site",self)
    self.delete_btn.move(105, 57)
    self.delete_btn.clicked.connect(self.delete_site)

  def load_data(self):
    if os.path.exists(self.blackFile_path):
      with open(self.blackFile_path, "r", encoding="utf-8") as f:
        return json.load(f)
    return []

  def save_data(self):
    with open(self.blackFile_path, "w", encoding="utf-8") as f:
      json.dump(self.sites, f, indent=4)

  def add_site(self):
    url = self.input_field.text().strip().lower()
    if url:
      if url not in self.sites:
        self.sites.append(url)
        self.save_data()
        self.input_field.clear()
      else:
        QMessageBox.warning(self, "Error", "This site was added earlier")

  def delete_site(self):
    url = self.input_field.text().strip().lower()
    if url in self.sites:
      self.sites.remove(url)
      self.save_data()
      self.input_field.clear()
    else:
      QMessageBox.warning(self, "Error", "This site dont be added yet")