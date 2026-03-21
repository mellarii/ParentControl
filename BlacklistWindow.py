import json
import os
import ctypes

from PyQt6.QtCore import Qt, QSettings
from PyQt6.QtWidgets import  QWidget, QLabel, QLineEdit, QPushButton, QMessageBox

class BlacklistWindow(QWidget):
  def __init__(self, parent=None):
    super().__init__(parent, Qt.WindowType.Window)
    self.setWindowTitle("Blacklist")
    self.resize(480, 270)

    self.blackFile_path = "blacklist.json"
    self.sites = self.load_data()


    self.host_path = r"C:\Windows\System32\drivers\etc\hosts"
    self.redirect = "127.0.0.1"

    self.input_field = QLineEdit(self)
    self.input_field.setPlaceholderText("Input site to add.")
    self.input_field.setGeometry(20, 20, 260, 30)

    self.add_btn = QPushButton("Add site",self)
    self.add_btn.move(20, 57)
    self.add_btn.clicked.connect(self.add_site)

    self.delete_btn = QPushButton("Delete site",self)
    self.delete_btn.move(105, 57)
    self.delete_btn.clicked.connect(self.delete_site)

    self.clear_btn = QPushButton("Clear url's", self)
    self.clear_btn.move(190, 57)
    self.clear_btn.clicked.connect(self.clear_all)

  def is_admin(self):
    try:
      return ctypes.windll.shell32.IsUserAnAdmin()
    except:
      return false

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

  def clear_all(self):
    self.sites = []
    with open(self.blackFile_path, "w", encoding="utf-8") as f:
      json.dump([], f)

  def block_sites(self):
    if not self.is_admin():
      QMessageBox.warning(self, "Warning", "You cant do that")
      return
    try:
      with open(self.host_path, 'r+') as f:
        content = f.read()
        for site in self.sites:
          entry = f"{self.redirect} {site}\n"
          if site not in content:
            f.write(entry)
      os.system("ipconfig /flushdns")
    except:
      QMessageBox.critical(self, "Error", f"Cant eded hosts: {e}")

  def unblock_sites(self):
    with open(self.host_path, 'r') as f:
      lines = f.readlines()
    with open(self.host_path, 'w') as f:
      for line in lines:
        if not any(site in line for site in self.sites):
          f.write(line) 
    os.system("ipconfig /flushdns")