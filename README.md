# Student Management System

A comprehensive Student Management System built with Python using Object-Oriented Programming principles. This system provides a complete solution for managing student records, subject enrollments, grades, and attendance tracking through an intuitive command-line interface.

##  Features

### Core Functionalities
- **Student Management**: Add new students with unique IDs, names, and section information. View all registered students with their enrollment details.
- **Subject Management**: Create and manage subjects with course codes, names, and credit hours.
- **Enrollment System**: Seamlessly enroll students in multiple subjects with automatic record creation and validation.
- **Grade Tracking**: Add multiple grade entries per subject, automatically calculate grade averages, and maintain complete grade history.
- **Attendance Tracking**: Mark daily attendance (present/absent), track total classes held, and calculate attendance percentages in real-time.
- **Comprehensive Reporting**: Generate detailed student reports showing all enrolled subjects, grade summaries, and attendance statistics.
- **Data Persistence**: All data automatically saved to human-readable text files with proper formatting.

### Technical Features
- **Object-Oriented Design**: Clean separation of concerns using multiple classes (Student, Subject, Record, SystemManager)
- **File-Based Storage**: No database required—uses simple, readable text files
- **Error Handling**: Comprehensive validation and error messages for user inputs
- **Auto-Creation**: Data directory and files are created automatically on first run
- **Data Integrity**: Prevents duplicate entries and maintains referential integrity

##  Project Structure

```
student_management_system/
├── main.py                 # Main entry point - runs the interactive menu
├── models/                 # Contains all class definitions
│   ├── student.py         # Student class: manages student data
│   ├── subject.py         # Subject class: handles course information
│   ├── record.py          # Record class: tracks grades & attendance
│   └── manager.py         # SystemManager: coordinates all operations
├── data/                   # Auto-created directory for data storage
│   ├── students.txt       # Stores student information
│   ├── subjects.txt       # Stores subject/course details
│   ├── enrollments.txt    # Tracks student-subject enrollments
│   └── records.txt        # Stores grades and attendance data
└── README.md              # Project documentation (this file)
```

##  How to Run

### Prerequisites
- Python 3.6 or higher installed on your system
- Basic understanding of command-line interface

### Installation & Execution

1. **Download/Clone the project:**
   ```bash
   git clone https://github.com/marama74 /student_management_system.git
   cd student_management_system
   ```

2. **Run the application:**
   ```bash
   python main.py
   ```

3. **First Run:**
   - The program automatically creates the `data/` folder
   - All necessary text files are generated on first save operation
   - No manual setup required!

### Menu Options

When you run the program, you'll see an interactive menu:

```
==================================================
   STUDENT MANAGEMENT SYSTEM
==================================================
1. Add Student
2. Add Subject
3. Enroll Student
4. Add Grade
5. Mark Attendance
6. View Student Report
7. View All Students
8. Exit
==================================================
```

## System Architecture

### Class Descriptions

#### **1. Student Class** (`models/student.py`)
Represents an individual student in the system.

**Attributes:**
- `student_id` (str): Unique identifier for each student
- `name` (str): Full name of the student
- `section` (str): Class section or batch (e.g., "BSCS-3A")
- `enrolled_subjects` (list): List of subject codes the student is enrolled in

**Key Methods:**
- `enroll_subject(subject_code)`: Adds a subject to student's enrollment list
- `get_num_subjects()`: Returns the count of enrolled subjects
- `to_string()`: Converts student data to file-storage format
- `from_string(data_string)`: Creates Student object from stored data

#### **2. Subject Class** (`models/subject.py`)
Represents a course or subject offered by the institution.

**Attributes:**
- `subject_code` (str): Unique code (e.g., "CS101")
- `subject_name` (str): Full subject name
- `credit_hours` (int): Number of credit hours for the course

**Key Methods:**
- `to_string()`: Formats subject data for file storage
- `from_string(data_string)`: Reconstructs Subject object from file

#### **3. Record Class** (`models/record.py`)
Manages grades and attendance for a specific student-subject pair.

**Attributes:**
- `student_id` (str): References the student
- `subject_code` (str): References the subject
- `grades` (list): All grade entries for this subject
- `attendance_present` (int): Number of classes attended
- `total_classes` (int): Total number of classes held

**Key Methods:**
- `add_grade(grade)`: Adds a new grade (validates 0-100 range)
- `get_average_grade()`: Calculates and returns grade average
- `mark_attendance(present)`: Records attendance for a class
- `get_attendance_percentage()`: Calculates attendance percentage
- `to_string()`: Formats record data for storage
- `from_string(data_string)`: Reconstructs Record from stored data

#### **4. SystemManager Class** (`models/manager.py`)
The central controller that manages all system operations.

**Attributes:**
- `students` (dict): All Student objects indexed by ID
- `subjects` (dict): All Subject objects indexed by code
- `records` (dict): All Record objects indexed by student_subject key
- `enrollments` (dict): Tracks which subjects each student is enrolled in

**Key Methods:**
- `add_student()`: Creates and stores a new student
- `add_subject()`: Creates and stores a new subject
- `enroll_student()`: Links student to subject and creates record
- `add_grade()`: Adds grade entry to student's subject record
- `mark_attendance()`: Records attendance for student in subject
- `view_student_report()`: Generates comprehensive report for one student
- `view_all_students()`: Lists all students in the system
- `save_all_data()`: Saves all data to text files
- `load_all_data()`: Loads existing data on program start

## 💾 Data Storage Format

All data is stored in **human-readable plain text files** using pipe (`|`) delimiters with spaces for clarity.

### **students.txt**
Stores basic student information.
```
1001 | Alice Johnson | BSCS-3A
1002 | Ahmed Khan | BSSE-2B
1003 | Sara Ali | BSCS-3B
```
**Format:** `student_id | name | section`

### **subjects.txt**
Contains all available subjects/courses.
```
CS101 | Programming Fundamentals | 3
CS201 | Data Structures | 4
MATH101 | Calculus I | 3
```
**Format:** `subject_code | subject_name | credit_hours`

### **enrollments.txt**
Tracks which students are enrolled in which subjects.
```
1001 | CS101,CS201,MATH101
1002 | CS101,MATH101
1003 | CS201
```
**Format:** `student_id | subject_code1,subject_code2,...`

### **records.txt**
Stores grades and attendance for each student-subject enrollment.
```
1001 | CS101 | grades=[85,90,88] | attendance=12/14
1001 | CS201 | grades=[92,95] | attendance=13/15
1002 | CS101 | grades=[78,82,85,88] | attendance=14/14
```
**Format:** `student_id | subject_code | grades=[g1,g2,...] | attendance=present/total`

### Why Text Files?
- **Human Readable**: Can be opened and edited with any text editor
- **No Dependencies**: No database installation required
- **Easy Backup**: Simple file copy for backups
- **Portable**: Works on any operating system
- **Educational**: Easy to understand data structure
- **Version Control Friendly**: Text files work well with Git

## 📝 Usage Examples

### Example Workflow

1. **Add Students:**
   ```
   Enter choice: 1
   Enter Student ID: 1001
   Enter Name: Alice Johnson
   Enter Section/Batch: BSCS-3A
   ✓ Student Alice Johnson added successfully!
   ```

2. **Add Subjects:**
   ```
   Enter choice: 2
   Enter Subject Code: CS101
   Enter Subject Name: Programming Fundamentals
   Enter Credit Hours: 3
   ✓ Subject Programming Fundamentals added successfully!
   ```

3. **Enroll Student:**
   ```
   Enter choice: 3
   Enter Student ID: 1001
   Enter Subject Code: CS101
   ✓ Student Alice Johnson enrolled in Programming Fundamentals!
   ```

4. **Add Grades:**
   ```
   Enter choice: 4
   Enter Student ID: 1001
   Enter Subject Code: CS101
   Enter Grade: 85
   ✓ Grade 85 added successfully!
   ```

5. **Mark Attendance:**
   ```
   Enter choice: 5
   Enter Student ID: 1001
   Enter Subject Code: CS101
   Present or Absent (P/A): P
   ✓ Attendance marked as Present!
   ```

6. **View Report:**
   ```
   Enter choice: 6
   Enter Student ID: 1001
   
   ============================================================
      STUDENT REPORT
   ============================================================
   Student ID: 1001
   Name: Alice Johnson
   Section: BSCS-3A
   Total Subjects Enrolled: 2
   ============================================================
   
   SUBJECT DETAILS:
   ------------------------------------------------------------
   
   Subject: Programming Fundamentals (CS101)
   Credit Hours: 3
   Grades: 85, 90, 88
   Average Grade: 87.67
   Attendance: 12/14 classes
   Attendance Percentage: 85.71%
   ------------------------------------------------------------
   

##  OOP Concepts Demonstrated

This project implements key Object-Oriented Programming principles:

1. **Encapsulation**: Each class manages its own data and provides methods to interact with it
2. **Abstraction**: Complex operations hidden behind simple method calls
3. **Modularity**: Separate files for each class promote code organization
4. **Single Responsibility**: Each class has one clear purpose
5. **DRY Principle**: Code reusability through methods and classes


##  Author

**Maryam Arshad**  
Roll Number: 498506  


