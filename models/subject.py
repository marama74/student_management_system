"""
Subject Class in this module
Represents a subject/course in the system
"""

class Subject:
    def __init__(self, subject_code, subject_name, credit_hours):
        self.subject_code = subject_code
        self.subject_name = subject_name
        self.credit_hours = credit_hours
    
    def to_string(self):
        """Convert subject data to string for file storage"""
        return f"{self.subject_code} | {self.subject_name} | {self.credit_hours}"
    
    @staticmethod
    def from_string(data_string):
        """Create Subject object from string"""
        parts = [p.strip() for p in data_string.strip().split('|')]
        if len(parts) >= 3:
            return Subject(parts[0], parts[1], int(parts[2]))
        return None
    
    def __str__(self):
        return f"Subject[Code: {self.subject_code}, Name: {self.subject_name}, Credits: {self.credit_hours}]"