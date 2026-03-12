import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import  QApplication, QWidget, QLabel


def main():
  app = QApplication(sys.argv)

  window = QWidget()
  text = QLabel("JustBeggining", window)
  text.resize(400,400)
  text.move(170, -20)

  timer = QLabel("00:00", window)
  timer.setAlignment(Qt.AlignmentFlag.AlignCenter)
  timer.resize(400, 400)

  window.setWindowTitle("Parent Control")
  window.resize(400,400)
  window.show()

  sys.exit(app.exec())

if __name__ == "__main__":
  try: 
    main()
  except Exception as e:
    print("Error detected")