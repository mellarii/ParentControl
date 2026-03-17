import sys

from PyQt6.QtCore import Qt, QTimer

from PyQt6.QtWidgets import  QApplication, QWidget, QLabel, QPushButton

def main():

  app = QApplication(sys.argv)

  window = QWidget()

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

  window.setWindowTitle("Parent Control")

  window.resize(960,540)

  window.show()

  sys.exit(app.exec())

if __name__ == "__main__":

  # try: 

    main()

  # except Exception as e:

  #   print("Error detected")