import sys

from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtWidgets import  QApplication, QWidget, QLabel, QPushButton

from PyQt6.QtWidgets import  QApplication, QWidget, QLabel, QPushButton

def main():

  app = QApplication(sys.argv)
  window = QWidget()
  state_window = QWidget(window, Qt.WindowType.Window)
  blacklist_window = QWidget(window, Qt.WindowType.Window)

  timer = QLabel("00:00", window)

  main_text = QLabel("JustBeggining", window)

  start_timer = QPushButton("Start", window)

  add_to_bunlist_btn = QPushButton("Add new sites to blacklist.", window)

  see_state = QPushButton("Device activity statistics", window)

  see_state.move(15, 465)

  add_to_bunlist_btn.move(15, 500)

  start_timer.move(440, 270)

  timer.move(283,270)

  timer.resize(400, 100)

  main_text.resize(400,100)

  main_text.move(444, 200)

  main_text = QLabel("JustBeggining", window)
  startTimerBtn = QPushButton("Start", window)
  banlistBtn = QPushButton("Add new sites to blacklist.", window)
  stateBtn = QPushButton("Device activity statistics", window)

  stateBtn.move(15, 465)
  banlistBtn.move(15, 500)
  startTimerBtn.move(440, 270)
  timer.move(283,270)
  timer.resize(400, 100)
  main_text.resize(400,100)
  main_text.move(444, 200)

  timer.setAlignment(Qt.AlignmentFlag.AlignCenter)

  time_data = [0]

  def tick():

    time_data[0] += 1

    s = time_data[0]

    minutes = s //60

    seconds = s % 60

    timer.setText(f"{minutes:02}:{seconds:02}")

  clock = QTimer()

  clock.timeout.connect(tick)

  start_timer.clicked.connect(lambda: clock.start(1000))
  time_data = [0]
  def tick():
    time_data[0] += 1
    s = time_data[0]
    minutes = s //60
    seconds = s % 60
    timer.setText(f"{minutes:02}:{seconds:02}")
  clock = QTimer()
  clock.timeout.connect(tick)

  def startLogic():
    if not clock.isActive(): 
      clock.start(1000)
      startTimerBtn.setText("Running...")
    else:
      clock.stop()
      startTimerBtn.setText("Resume")

  startTimerBtn.clicked.connect(lambda: startLogic())

  window.setWindowTitle("Parent Control")

  window.resize(960,540)

  window.resize(960,540)
  window.show()

  state_window.setWindowTitle("Statistics")
  state_window.resize(480, 270)
  stateBtn.clicked.connect(lambda: state_window.show())
  parentName = QLabel("Parent: ", state_window)
  parentName.move(15, 15)
  childName = QLabel("Child: ", state_window)
  childName.move(15, 35)
  UsingTime = QLabel("Today you use: ", state_window)
  UsingTime.move(15, 55)


  blacklist_window.setWindowTitle("Blacklist")
  blacklist_window.resize(480, 270)
  banlistBtn.clicked.connect(lambda: blacklist_window.show())



  sys.exit(app.exec())

if __name__ == "__main__":

  # try: 

  # try: 
    main()

  # except Exception as e:

  #   print("Error detected")
  # except Exception as e:
  #   print("Error detected")