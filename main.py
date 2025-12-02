"""
Student Management System - Main Entry Point
Run this file to start the application
"""
from models.manager import SystemManager

def display_menu():
    print("\n" + "="*50)
    print("   STUDENT MANAGEMENT SYSTEM")
    print("="*50)
    print("1. Add Student")
    print("2. Add Subject")
    print("3. Enroll Student")
    print("4. Add Grade")
    print("5. Mark Attendance")
    print("6. View Student Report")
    print("7. View All Students")
    print("8. Exit")
    print("="*50)

def main():
    manager = SystemManager()
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-8): ").strip()
        
        try:
            if choice == '1':
                student_id = input("Enter Student ID: ").strip()
                name = input("Enter Name: ").strip()
                section = input("Enter Section/Batch: ").strip()
                manager.add_student(student_id, name, section)
                
            elif choice == '2':
                subject_code = input("Enter Subject Code: ").strip()
                subject_name = input("Enter Subject Name: ").strip()
                credit_hours = int(input("Enter Credit Hours: ").strip())
                manager.add_subject(subject_code, subject_name, credit_hours)
                
            elif choice == '3':
                student_id = input("Enter Student ID: ").strip()
                subject_code = input("Enter Subject Code: ").strip()
                manager.enroll_student(student_id, subject_code)
                
            elif choice == '4':
                student_id = input("Enter Student ID: ").strip()
                subject_code = input("Enter Subject Code: ").strip()
                grade = float(input("Enter Grade: ").strip())
                manager.add_grade(student_id, subject_code, grade)
                
            elif choice == '5':
                student_id = input("Enter Student ID: ").strip()
                subject_code = input("Enter Subject Code: ").strip()
                status = input("Present or Absent (P/A): ").strip().upper()
                manager.mark_attendance(student_id, subject_code, status == 'P')
                
            elif choice == '6':
                student_id = input("Enter Student ID: ").strip()
                manager.view_student_report(student_id)
                
            elif choice == '7':
                manager.view_all_students()
                
            elif choice == '8':
                print("\nSaving data and exiting...")
                manager.save_all_data()
                print("Thank you for using Student Management System!")
                break
                
            else:
                print("\nInvalid choice! Please enter a number between 1 and 8.")
                
        except ValueError as e:
            print(f"\nError: Invalid input format - {e}")
        except Exception as e:
            print(f"\nError: {e}")

if __name__ == "__main__":
    main()