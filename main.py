# Entry point to the application
from gui.main_window import MainWindow # Import main window
from PySide6.QtWidgets import QApplication
import sys


def main():
    app = QApplication(sys.argv)# Show main window in the GUI
    window = MainWindow()
    window.show()
    app.exec()                      
    

if __name__ == '__main__':
    
    try:
        main()
    except Exception as e:
        print(e)