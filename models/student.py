"""
Student Class
Represents a student in the system
"""

class Student:
    def __init__(self, student_id, name, section):
        self.student_id = student_id
        self.name = name
        self.section = section
        self.enrolled_subjects = []
    
    def enroll_subject(self, subject_code):
        """Enroll student in a subject"""
        if subject_code not in self.enrolled_subjects:
            self.enrolled_subjects.append(subject_code)
            return True
        return False
    
    def get_num_subjects(self):
        """Get number of enrolled subjects"""
        return len(self.enrolled_subjects)
    
    def to_string(self):
        """Convert student data to string for file storage"""
        return f"{self.student_id} | {self.name} | {self.section}"
    
    @staticmethod
    def from_string(data_string):
        """Create Student object from string"""
        parts = [p.strip() for p in data_string.strip().split('|')]
        if len(parts) >= 3:
            return Student(parts[0], parts[1], parts[2])
        return None
    
    def __str__(self):
        return f"Student[ID: {self.student_id}, Name: {self.name}, Section: {self.section}]"