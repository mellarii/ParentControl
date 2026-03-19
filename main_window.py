import sys

from PyQt6.QtCore import (Qt, QTimer)
from PyQt6.QtWidgets import  (QApplication, QWidget, QLabel, QPushButton, QLineEdit)

from windows import StateWindow, BlacklistWindow

class mainWindow(QWidget):
  def __init__(self):
    super().__init__()
    self.time_seconds = 0

    self.state_win = StateWindow(self)
    self.blacklist_win = BlacklistWindow(self)

    self.init_ui()
    self.init_timer()

  def init_ui(self): 
    self.setWindowTitle("Parent Control")  
    self.resize(960,540)

    self.main_text = QLabel("JustBeggining", self)
    self.main_text.resize(400,100)
    self.main_text.move(444, 200)

    self.timer = QLabel("00:00", self) 
    self.timer.move(283,270)
    self.timer.resize(400, 100)
    self.timer.setAlignment(Qt.AlignmentFlag.AlignCenter)

    self.start_btn = QPushButton("Start", self)
    self.start_btn.move(440, 270)
    self.bunlist_btn = QPushButton("Add new sites to blacklist.", self)
    self.bunlist_btn.move(15, 500)
    self.state_btn = QPushButton("Device activity statistics", self)
    self.state_btn.move(15, 465)

    self.start_btn.clicked.connect(self.startLogic)
    self.state_btn.clicked.connect(self.state_win.show)
    self.bunlist_btn.clicked.connect(self.blacklist_win.show)

  def init_timer(self):
    self.clock = QTimer()
    self.clock.timeout.connect(self.tick)
        
  def tick(self):
    self.time_seconds += 1
    minutes = self.time_seconds //60
    seconds = self.time_seconds % 60
    self.timer.setText(f"{minutes:02}:{seconds:02}")
    

  def startLogic(self):
    if self.clock.isActive(): 
      self.clock.stop()
      self.start_btn.setText("Resume")
    else:
      self.clock.start(1000)
      self.start_btn.setText("Running...")