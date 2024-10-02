from PySide6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QStackedLayout, QWidget, QHBoxLayout, QPushButton
from gui.popups.widgets.widgets import DatabaseDetailsForm, SelectTableForm, CreateProjectForm
from PySide6.QtCore import Qt

class SetUpWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Database Details")
        
        self.setFixedSize(400, 300)
        
        # Main layout for the central widget
        main_layout = QVBoxLayout()
        
        title_label = QLabel("Link Database")
        title_label.setStyleSheet("color: white; font-size: 18px; background-color: grey; margin: 0 auto; font-weight: 700")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        title_layout = QHBoxLayout()
        title_layout.addWidget(title_label)

        # Stacked layout for different views
        self.stacklayout = QStackedLayout()

        # Example pages in the stacked layout
        self.create_pages()

        # Button layout

        # Add widgets to the main layout
        main_layout.addLayout(title_layout)
        main_layout.addLayout(self.stacklayout)
        
        main_layout.setStretch(0, 1)
        main_layout.setStretch(1, 5)
        
        # Set the central widget
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)
    
    def create_pages(self):
        # Get first page
        self.details_form_widget = DatabaseDetailsForm(self)
        self.tables_form_widget = SelectTableForm(self)
        self.create_project_form = CreateProjectForm(self)
        
        # Add pages to the stacked layout
        self.stacklayout.addWidget(self.details_form_widget)
        self.stacklayout.addWidget(self.tables_form_widget)
        self.stacklayout.addWidget(self.create_project_form)
        
    def handle_db_details_submitted(self, table_names):
        # Here you can pass the details to the next form if needed
        self.tables_form_widget.set_table_names(table_names)
        
        # Move to the next widget in the stack
        self.stacklayout.setCurrentWidget(self.tables_form_widget)
    
    def handle_table_details_submitted(self, selected_table_names):
        # Create new tables with the selected tables
        print(f"Selected tables: {selected_table_names}")
        self.selected_table_names = selected_table_names
        
        self.stacklayout.setCurrentWidget(self.create_project_form)
        
    def start_application(self, project_name):
        
        self.project_name = project_name
    
        print("Starting application...")
        
        # 

def start_setup() -> QMainWindow:
    
    window = SetUpWindow()
    return window                  