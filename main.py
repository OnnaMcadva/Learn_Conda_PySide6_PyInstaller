import sys
from model_train_new import YOLOTrainWindow
from PySide6.QtWidgets import QApplication

def main():
    app = QApplication(sys.argv)
    window = YOLOTrainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
