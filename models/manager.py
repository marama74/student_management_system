"""
System Manager Class
Handles all operations and data management
"""
import os
from models.student import Student
from models.subject import Subject
from models.record import Record

class SystemManager:
    def __init__(self):
        self.students = {}
        self.subjects = {}
        self.records = {}
        self.enrollments = {}  # Track which students are enrolled in which subjects
        self.data_dir = 'data'
        self._ensure_data_directory()
        self.load_all_data()
    
    def _ensure_data_directory(self):
        """Create data directory if it doesn't exist"""
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
    
    def _get_record_key(self, student_id, subject_code):
        """Generate unique key for record"""
        return f"{student_id}_{subject_code}"
    
    def add_student(self, student_id, name, section):
        """Add a new student"""
        if student_id in self.students:
            print(f"\nError: Student with ID {student_id} already exists!")
            return False
        
        student = Student(student_id, name, section)
        self.students[student_id] = student
        self.save_students()
        print(f"\nStudent {name} added successfully!")
        return True
    
    def add_subject(self, subject_code, subject_name, credit_hours):
        """Add a new subject"""
        if subject_code in self.subjects:
            print(f"\nError: Subject with code {subject_code} already exists!")
            return False
        
        subject = Subject(subject_code, subject_name, credit_hours)
        self.subjects[subject_code] = subject
        self.save_subjects()
        print(f"\nSubject {subject_name} added successfully!")
        return True
    
    def enroll_student(self, student_id, subject_code):
        """Enroll a student in a subject"""
        if student_id not in self.students:
            print(f"\nError: Student with ID {student_id} not found!")
            return False
        
        if subject_code not in self.subjects:
            print(f"\nError: Subject with code {subject_code} not found!")
            return False
        
        student = self.students[student_id]
        record_key = self._get_record_key(student_id, subject_code)
        
        if record_key in self.records:
            print(f"\nError: Student already enrolled in this subject!")
            return False
        
        student.enroll_subject(subject_code)
        self.records[record_key] = Record(student_id, subject_code)
        
        # Track enrollment
        if student_id not in self.enrollments:
            self.enrollments[student_id] = []
        self.enrollments[student_id].append(subject_code)
        
        self.save_enrollments()
        self.save_records()
        print(f"\nStudent {student.name} enrolled in {self.subjects[subject_code].subject_name}!")
        return True
    
    def add_grade(self, student_id, subject_code, grade):
        """Add a grade for a student in a subject"""
        record_key = self._get_record_key(student_id, subject_code)
        
        if record_key not in self.records:
            print(f"\nError: Enrollment record not found!")
            return False
        
        if self.records[record_key].add_grade(grade):
            self.save_records()
            print(f"\nGrade {grade} added successfully!")
            return True
        else:
            print(f"\nError: Invalid grade! Must be between 0 and 100.")
            return False
    
    def mark_attendance(self, student_id, subject_code, present=True):
        """Mark attendance for a student"""
        record_key = self._get_record_key(student_id, subject_code)
        
        if record_key not in self.records:
            print(f"\nError: Enrollment record not found!")
            return False
        
        self.records[record_key].mark_attendance(present)
        self.save_records()
        status = "Present" if present else "Absent"
        print(f"\nAttendance marked as {status}!")
        return True
    
    def view_student_report(self, student_id):
        """Generate and display student report"""
        if student_id not in self.students:
            print(f"\nError: Student with ID {student_id} not found!")
            return
        
        student = self.students[student_id]
        print("\n" + "="*60)
        print(f"   STUDENT REPORT")
        print("="*60)
        print(f"Student ID: {student.student_id}")
        print(f"Name: {student.name}")
        print(f"Section: {student.section}")
        print(f"Total Subjects Enrolled: {student.get_num_subjects()}")
        print("="*60)
        
        if not student.enrolled_subjects:
            print("\nNo subjects enrolled yet.")
            return
        
        print("\nSUBJECT DETAILS:")
        print("-"*60)
        
        for subject_code in student.enrolled_subjects:
            record_key = self._get_record_key(student_id, subject_code)
            subject = self.subjects.get(subject_code)
            record = self.records.get(record_key)
            
            if subject and record:
                print(f"\nSubject: {subject.subject_name} ({subject_code})")
                print(f"Credit Hours: {subject.credit_hours}")
                
                if record.grades:
                    print(f"Grades: {', '.join(map(str, record.grades))}")
                    print(f"Average Grade: {record.get_average_grade():.2f}")
                else:
                    print("Grades: No grades recorded")
                
                print(f"Attendance: {record.attendance_present}/{record.total_classes} classes")
                print(f"Attendance Percentage: {record.get_attendance_percentage():.2f}%")
                print("-"*60)
    
    def view_all_students(self):
        """Display all students"""
        if not self.students:
            print("\nNo students in the system yet.")
            return
        
        print("\n" + "="*60)
        print("   ALL STUDENTS")
        print("="*60)
        
        for student in self.students.values():
            print(f"\nID: {student.student_id}")
            print(f"Name: {student.name}")
            print(f"Section: {student.section}")
            print(f"Subjects Enrolled: {student.get_num_subjects()}")
            print("-"*60)
    
    def save_students(self):
        """Save students to file"""
        file_path = os.path.join(self.data_dir, 'students.txt')
        try:
            with open(file_path, 'w') as f:
                for student in self.students.values():
                    f.write(student.to_string() + '\n')
        except Exception as e:
            print(f"Error saving students: {e}")
    
    def save_subjects(self):
        """Save subjects to file"""
        file_path = os.path.join(self.data_dir, 'subjects.txt')
        try:
            with open(file_path, 'w') as f:
                for subject in self.subjects.values():
                    f.write(subject.to_string() + '\n')
        except Exception as e:
            print(f"Error saving subjects: {e}")
    
    def save_records(self):
        """Save records to file"""
        file_path = os.path.join(self.data_dir, 'records.txt')
        try:
            with open(file_path, 'w') as f:
                for record in self.records.values():
                    f.write(record.to_string() + '\n')
        except Exception as e:
            print(f"Error saving records: {e}")
    
    def save_enrollments(self):
        """Save enrollments to file"""
        file_path = os.path.join(self.data_dir, 'enrollments.txt')
        try:
            with open(file_path, 'w') as f:
                for student_id, subject_codes in self.enrollments.items():
                    subjects_str = ','.join(subject_codes)
                    f.write(f"{student_id} | {subjects_str}\n")
        except Exception as e:
            print(f"Error saving enrollments: {e}")
    
    def save_all_data(self):
        """Save all data to files"""
        self.save_students()
        self.save_subjects()
        self.save_enrollments()
        self.save_records()
    
    def load_all_data(self):
        """Load all data from files"""
        self.load_students()
        self.load_subjects()
        self.load_enrollments()
        self.load_records()
    
    def load_enrollments(self):
        """Load enrollments from file"""
        file_path = os.path.join(self.data_dir, 'enrollments.txt')
        if not os.path.exists(file_path):
            return
        
        try:
            with open(file_path, 'r') as f:
                for line in f:
                    if line.strip():
                        parts = [p.strip() for p in line.strip().split('|')]
                        if len(parts) >= 2:
                            student_id = parts[0]
                            subject_codes = [s.strip() for s in parts[1].split(',')]
                            self.enrollments[student_id] = subject_codes
                            
                            # Update student's enrolled_subjects
                            if student_id in self.students:
                                self.students[student_id].enrolled_subjects = subject_codes
        except Exception as e:
            print(f"Error loading enrollments: {e}")
    
    def load_students(self):
        """Load students from file"""
        file_path = os.path.join(self.data_dir, 'students.txt')
        if not os.path.exists(file_path):
            return
        
        try:
            with open(file_path, 'r') as f:
                for line in f:
                    student = Student.from_string(line)
                    if student:
                        self.students[student.student_id] = student
        except Exception as e:
            print(f"Error loading students: {e}")
    
    def load_subjects(self):
        """Load subjects from file"""
        file_path = os.path.join(self.data_dir, 'subjects.txt')
        if not os.path.exists(file_path):
            return
        
        try:
            with open(file_path, 'r') as f:
                for line in f:
                    subject = Subject.from_string(line)
                    if subject:
                        self.subjects[subject.subject_code] = subject
        except Exception as e:
            print(f"Error loading subjects: {e}")
    
    def load_records(self):
        """Load records from file"""
        file_path = os.path.join(self.data_dir, 'records.txt')
        if not os.path.exists(file_path):
            return
        
        try:
            with open(file_path, 'r') as f:
                for line in f:
                    record = Record.from_string(line)
                    if record:
                        record_key = self._get_record_key(record.student_id, record.subject_code)
                        self.records[record_key] = record
        except Exception as e:
            print(f"Error loading records: {e}")