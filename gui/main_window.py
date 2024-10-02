from PySide6.QtWidgets import QMainWindow
from gui.popups.setup import start_setup
from utils.db_methods.dbs_methods import SavedDatabasesMethods
from PySide6.QtCore import QTimer
from utils.db_setup.create_databases import init_db


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Welcome window")
        
        # Initialise Local App db connection
        init_db()
        
        # Prompt user for db information
        if not SavedDatabasesMethods.does_database_exist():
            self.startup_window = start_setup()
        
    def showEvent(self, event):
        super().showEvent(event)
        if self.startup_window:
            QTimer.singleShot(1000, self.hide)
            QTimer.singleShot(2000, self.startup_window.show)
         
        