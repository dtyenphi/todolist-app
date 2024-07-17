import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QComboBox, QSpinBox, QCheckBox, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QGroupBox

class DataEntryForm(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the window
        self.setWindowTitle("Data Entry Form")
        self.setGeometry(100, 100, 500, 400)

        # User Information Group Box
        self.user_info_group = QGroupBox("User Information")

        self.first_name_label = QLabel("First Name")
        self.first_name_input = QLineEdit()

        self.last_name_label = QLabel("Last Name")
        self.last_name_input = QLineEdit()

        self.title_label = QLabel("Title")
        self.title_input = QComboBox()
        self.title_input.addItems(["Mr.", "Ms.", "Mrs.", "Dr."])

        self.age_label = QLabel("Age")
        self.age_input = QSpinBox()
        self.age_input.setRange(0, 100)
        self.age_input.setValue(18)

        self.nationality_label = QLabel("Nationality")
        self.nationality_input = QLineEdit()

        user_info_layout = QGridLayout()
        user_info_layout.addWidget(self.first_name_label, 0, 0)
        user_info_layout.addWidget(self.first_name_input, 0, 1)
        user_info_layout.addWidget(self.last_name_label, 0, 2)
        user_info_layout.addWidget(self.last_name_input, 0, 3)
        user_info_layout.addWidget(self.title_label, 0, 4)
        user_info_layout.addWidget(self.title_input, 0, 5)
        user_info_layout.addWidget(self.age_label, 1, 0)
        user_info_layout.addWidget(self.age_input, 1, 1)
        user_info_layout.addWidget(self.nationality_label, 1, 2)
        user_info_layout.addWidget(self.nationality_input, 1, 3)

        self.user_info_group.setLayout(user_info_layout)

        # Registration Status Group Box
        self.registration_group = QGroupBox("Registration Status")

        self.currently_registered = QCheckBox("Currently Registered")

        self.completed_courses_label = QLabel("# Completed Courses")
        self.completed_courses_input = QSpinBox()
        self.completed_courses_input.setRange(0, 50)

        self.semesters_label = QLabel("# Semesters")
        self.semesters_input = QSpinBox()
        self.semesters_input.setRange(0, 10)

        registration_layout = QGridLayout()
        registration_layout.addWidget(self.currently_registered, 0, 0)
        registration_layout.addWidget(self.completed_courses_label, 0, 1)
        registration_layout.addWidget(self.completed_courses_input, 0, 2)
        registration_layout.addWidget(self.semesters_label, 0, 3)
        registration_layout.addWidget(self.semesters_input, 0, 4)

        self.registration_group.setLayout(registration_layout)

        # Terms and Conditions Group Box
        self.terms_group = QGroupBox("Terms & Conditions")
        self.terms_checkbox = QCheckBox("I accept the terms and conditions.")

        terms_layout = QVBoxLayout()
        terms_layout.addWidget(self.terms_checkbox)
        self.terms_group.setLayout(terms_layout)

        # Submit Button
        self.submit_button = QPushButton("Enter data")
        self.submit_button.clicked.connect(self.submit_data)

        # Main Layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.user_info_group)
        main_layout.addWidget(self.registration_group)
        main_layout.addWidget(self.terms_group)
        main_layout.addWidget(self.submit_button)

        self.setLayout(main_layout)

    def submit_data(self):
        print("First Name:", self.first_name_input.text())
        print("Last Name:", self.last_name_input.text())
        print("Title:", self.title_input.currentText())
        print("Age:", self.age_input.value())
        print("Nationality:", self.nationality_input.text())
        print("Currently Registered:", self.currently_registered.isChecked())
        print("Completed Courses:", self.completed_courses_input.value())
        print("Semesters:", self.semesters_input.value())
        print("Accepted Terms:", self.terms_checkbox.isChecked())

    if __name__ == "__main__":
        app = QApplication(sys.argv)
        window = DataEntryForm()
        window.show()
        sys.exit(app.exec_())