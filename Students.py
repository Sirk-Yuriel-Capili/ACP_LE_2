class Student:
    studentrecords = []   

    def __init__(self, id_name, email, grades, courses):
        self.id_name = id_name
        self.email = email
        self.grades = grades
        self.courses = courses
        

    @classmethod  
    def add_student(cls, id_name , email, grades, courses):
        new_student = student(id_name, email, grades, courses)
        cls.student.append(new_student) 
        return "Student added successfully"

    @classmethod
    def update_student(cls, id_name, email=None, grades=None, courses=None):
        for student in cls.student:
            if student.id_name == id_name :
                if email is not None:
                    student.email = email
                if grades is not None:
                    student.grades = grades
                if courses is not None:
                    student.courses = courses
                return "Student information updated successfully"
        return "Student not found"
    
    @classmethod
    def delete_student(cls, id_name):
        for student in cls.student:
            if student.id_name == id_name:
                cls.student.remove(student)
                return "Student deleted successfully"
        return "Student not found"
    
    @classmethod
    def display_studentrecords(cls):
        if not cls.studentrecords:
            return "Student Record is empty."
        result = "\nSTUDENT RECORDS:\n"
        for p in cls.studentrecords:
            result += f"ID: {p.id_name}, Email: {p.email}, Grades: {p.grades}, "
            result += f"Courses: {p.courses}\n"
        return result
