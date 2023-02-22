import sys

from PyQt5.QtWidgets import QApplication
from ui import View
from ctrl import Control

def main():
    calc = QApplication(sys.argv)
    app = QApplication(sys.argv)
    view = View()
    Control(view = view)
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()