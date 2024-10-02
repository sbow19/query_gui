from PySide6.QtWidgets import QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QWidget, QPushButton, QMessageBox, QScrollArea, QCheckBox
from utils.db_methods.source_db_methods import test_db_connection
from PySide6.QtCore import Qt

class DatabaseDetailsForm(QWidget):
    
    def __init__(self, MainWidget):
        super().__init__()
        
        # Main layout
        details_form_layout = QVBoxLayout()
        
        self.main_widget = MainWidget
        
        #Input fields
        self.host_layout = QHBoxLayout()
        self.host_input = QLineEdit()
        self.host_layout.addWidget(QLabel("Host:"))
        self.host_layout.addWidget(self.host_input)
        self.host_layout.setStretch(0, 1)
        self.host_layout.setStretch(1, 5)
        
        self.port_layout = QHBoxLayout()
        self.port_input = QLineEdit()
        self.port_layout.addWidget(QLabel("Port:"))
        self.port_layout.addWidget(self.port_input)
        self.port_layout.setStretch(0, 1)
        self.port_layout.setStretch(1, 5)
        
        self.username_layout = QHBoxLayout()
        self.username_layout.setStretch(1, 5)
        self.username_input = QLineEdit()
        self.username_layout.addWidget(QLabel("Username:"))
        self.username_layout.addWidget(self.username_input)
        self.username_layout.setStretch(0, 1)
        self.username_layout.setStretch(1, 5)
        
        self.password_layout = QHBoxLayout()
        self.password_layout.setStretch(1, 5)
        self.password_input= QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_layout.addWidget(QLabel("Password:"))
        self.password_layout.addWidget(self.password_input)
        self.password_layout.setStretch(0, 1)
        self.password_layout.setStretch(1, 5)
        
        self.database_layout = QHBoxLayout()
        self.database_layout.setStretch(1, 5)
        self.database_input= QLineEdit()
        self.database_layout.addWidget(QLabel("Database:"))
        self.database_layout.addWidget(self.database_input)
        self.database_layout.setStretch(0, 1)
        self.database_layout.setStretch(1, 5)

        # Create a submit button
        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.submit_details)

        # Add widgets to the layout
        details_form_layout.addLayout(self.host_layout)
        details_form_layout.addLayout(self.port_layout)
        details_form_layout.addLayout(self.username_layout)
        details_form_layout.addLayout(self.password_layout)
        details_form_layout.addLayout(self.database_layout)
        details_form_layout.addWidget(self.submit_button)
        
        # Spacing out items in form
        details_form_layout.setStretch(0, 1)
        details_form_layout.setStretch(1, 1)
        details_form_layout.setStretch(2, 1)
        details_form_layout.setStretch(3, 1)
        details_form_layout.setStretch(4, 1)
        details_form_layout.setStretch(5, 3)
        
        details_form_layout.setSpacing(10)
        
        self.setLayout(details_form_layout)
    
    def submit_details(self):
        # Get input values
        host = self.host_input.text()
        port = self.port_input.text()
        username = self.username_input.text()
        password = self.password_input.text()
        database = self.database_input.text()
        
        # Validate input values
        if not host or not port or not username or not password or not database:
            QMessageBox.warning(self, "Warning", "All fields are required")
            return
        
        # Validate port number
        try:
            port = int(port)
        except ValueError:
            QMessageBox.warning(self, "Warning", "Port must be a number")
            return
        
        # Validate port range
        if port < 1 or port > 65535:
            QMessageBox.warning(self, "Warning", "Port must be between 1 and 65535")
            return
        
        # Validate database name
        if not database.isidentifier():
            QMessageBox.warning(self, "Warning", "Database name must be a valid identifier")
            return
        
        # Test MySql connection
        try:
            table_names = test_db_connection(username, password, host, port, database)

            # Save table name details to parent widget
            self.main_widget.handle_db_details_submitted(table_names)
        except Exception as e:
            QMessageBox.warning(self, "Warning", "Failed to connect to database, try again")
            
    

class SelectTableForm(QWidget):
    def __init__(self, MainWidget):
        super().__init__()
        
        self.main_widget = MainWidget
        self.checkboxes = []
        
        # Main layout
        self.layout = QVBoxLayout()
        
        # Create a scroll area
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)

        # Create a widget to hold the table names
        self.table_names_widget = QWidget()
        self.table_names_layout = QVBoxLayout(self.table_names_widget)

        # Set the widget for the scroll area
        self.scroll_area.setWidget(self.table_names_widget)

        # Add the scroll area to the main layout
        self.layout.addWidget(QLabel("Select Tables You Need:"))
        self.layout.addWidget(self.scroll_area)
        
        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.submit_selection)
        self.layout.addWidget(self.submit_button)

        self.setLayout(self.layout)
    
    def set_table_names(self, table_names):
        # Clear previous checkboxes
        for i in reversed(range(self.table_names_layout.count())):
            widget = self.table_names_layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

        # Add checkboxes for each table name
        for table_name in table_names:
            checkbox = QCheckBox(table_name)
            self.table_names_layout.addWidget(checkbox)
            self.checkboxes.append(checkbox)
    
    def submit_selection(self):# Collect checked table names
        selected_tables = [checkbox.text() for checkbox in self.checkboxes if checkbox.isChecked()]
        self.main_widget.handle_table_details_submitted(selected_tables)


class CreateProjectForm(QWidget):
    def __init__(self, MainWidget):
        super().__init__()
        
        self.main_widget = MainWidget
        
        # Main layout
        self.layout = QVBoxLayout()
        
        # Title
        title_widget = QLabel("Create New Project")
        title_widget.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        title_layout = QHBoxLayout()
        title_widget.setLayout(title_layout)
        
        #   Project name input
        project_name_widget = QWidget()
        project_name_internal = QHBoxLayout()
        self.project_input = QLineEdit()
        project_name_internal.addWidget(QLabel("Project Name"))
        project_name_internal.addWidget(self.project_input)
        project_name_internal.setStretch(0, 1)
        project_name_internal.setStretch(1, 5)
        project_name_widget.setLayout(project_name_internal)
        
        # Start button
        start_button = QPushButton("Start")
        start_button.clicked.connect(self.handle_start_application)
        button_layout = QHBoxLayout()
        button_layout.addWidget(start_button)
        
        self.layout.addWidget(title_widget)
        self.layout.addWidget(project_name_widget)
        self.layout.addLayout(button_layout)
        
        self.layout.setStretch(0, 1)
        self.layout.setStretch(1, 5)
        self.layout.setStretch(2, 1)
        
        self.setLayout(self.layout)
        
    def handle_start_application(self):
        self.main_widget.start_application(self.project_input.text())
        
        