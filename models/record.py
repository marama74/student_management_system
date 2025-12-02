"""
Record Class
Represents grades and attendance for a student in a specific subject
"""

class Record:
    def __init__(self, student_id, subject_code):
        self.student_id = student_id
        self.subject_code = subject_code
        self.grades = []
        self.attendance_present = 0
        self.total_classes = 0
    
    def add_grade(self, grade):
        """Add a grade entry"""
        if 0 <= grade <= 100:
            self.grades.append(grade)
            return True
        return False
    
    def get_average_grade(self):
        """Calculate average grade"""
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)
    
    def mark_attendance(self, present=True):
        """Mark attendance for a class"""
        self.total_classes += 1
        if present:
            self.attendance_present += 1
    
    def get_attendance_percentage(self):
        """Calculate attendance percentage"""
        if self.total_classes == 0:
            return 0.0
        return (self.attendance_present / self.total_classes) * 100
    
    def to_string(self):
        """Convert record data to string for file storage"""
        grades_str = ','.join(map(str, self.grades)) if self.grades else ''
        return f"{self.student_id} | {self.subject_code} | grades=[{grades_str}] | attendance={self.attendance_present}/{self.total_classes}"
    
    @staticmethod
    def from_string(data_string):
        """Create Record object from string"""
        # Parse format: student_id | subject_code | grades=[85,90] | attendance=12/14
        parts = [p.strip() for p in data_string.strip().split('|')]
        if len(parts) >= 4:
            record = Record(parts[0], parts[1])
            
            # Parse grades
            grades_part = parts[2].replace('grades=', '').replace('[', '').replace(']', '').strip()
            if grades_part:
                record.grades = [float(g.strip()) for g in grades_part.split(',')]
            
            # Parse attendance
            attendance_part = parts[3].replace('attendance=', '').strip()
            if '/' in attendance_part:
                present, total = attendance_part.split('/')
                record.attendance_present = int(present.strip())
                record.total_classes = int(total.strip())
            
            return record
        return None
    
    def __str__(self):
        return f"Record[Student: {self.student_id}, Subject: {self.subject_code}, Avg: {self.get_average_grade():.2f}, Attendance: {self.get_attendance_percentage():.2f}%]"