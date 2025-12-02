# Student Management System

A comprehensive Student Management System built with Python using Object-Oriented Programming principles.

## Features

- **Student Management**: Add and view students
- **Subject Management**: Add subjects with credit hours
- **Enrollment System**: Enroll students in subjects
- **Grade Tracking**: Add grades and calculate averages
- **Attendance Tracking**: Mark attendance and calculate percentages
- **Reporting**: Generate detailed student reports
- **Data Persistence**: All data stored in text files

## Project Structure

```
student_management_system/
├── main.py                 # Entry point
├── models/
│   ├── student.py         # Student class
│   ├── subject.py         # Subject class
│   ├── record.py          # Record class (grades + attendance)
│   └── manager.py         # System manager class
├── data/                   # Auto-created on first run
│   ├── students.txt       # Auto-generated
│   ├── subjects.txt       # Auto-generated
│   └── records.txt        # Auto-generated
├── .gitignore             # Excludes data files
└── README.md
```

## How to Run

1. Ensure Python 3.x is installed
2. Navigate to the project directory
3. Run the system:

```bash
python main.py
```

**Note:** The `data/` folder will be automatically created when you first run the program.

## Classes

### Student
- Attributes: student_id, name, section, enrolled_subjects
- Methods: enroll_subject(), get_num_subjects()

### Subject
- Attributes: subject_code, subject_name, credit_hours

### Record
- Attributes: student_id, subject_code, grades[], attendance_present, total_classes
- Methods: add_grade(), get_average_grade(), mark_attendance(), get_attendance_percentage()

### SystemManager
- Manages all operations
- Handles file I/O
- Coordinates between all classes

## Data Storage

Data is stored in plain text files using pipe (|) delimiters:

**students.txt format:**
```
1001 | Alice Johnson | BSCS-3A
1002 | Ahmed Khan | BSSE-2B
```

**subjects.txt format:**
```
CS101 | Programming Fundamentals | 3
CS201 | Data Structures | 4
```

**enrollments.txt format:**
```
1001 | CS101,CS201
1002 | CS101
```

**records.txt format:**
```
1001 | CS101 | grades=[85,90,88] | attendance=12/14
1001 | CS201 | grades=[92,95] | attendance=13/15
```

The `data/` folder is excluded from git via `.gitignore` so it won't be submitted to the repository.

## Usage Example

1. Add students and subjects
2. Enroll students in subjects
3. Add grades and mark attendance
4. View individual or all student reports

## Author
Maryam Arshad (498506)