class Student:
    def __init__(self, student_id, student_name, email, grades=None, courses=None):
        self.id_name = (student_id, student_name)
        self.email = email
        self.grades = grades if grades is not None else {}
        self.courses = set(courses) if courses is not None else set()

    def __str__(self):
        course_list = ', '.join(self.courses) if self.courses else 'None'
        return f"ID: {self.id_name[0]}, Name: {self.id_name[1]}, Email: {self.email}, Grades: {self.grades}, Courses: {course_list}"


class StudentRecords:
    def __init__(self):
        self.students = []

    def add_student(self, student_id, student_name, email, grades=None, courses=None):
        new_student = Student(student_id, student_name, email, grades, courses)
        self.students.append(new_student)
        return "Student added successfully"

    def update_student(self, student_id, email=None, grades=None, courses=None):
        for student in self.students:
            if student.id_name[0] == student_id:
                if email:
                    student.email = email
                if grades:
                    student.grades = grades
                if courses:
                    student.courses = set(courses)
                return "Student information updated successfully"
        return "Student not found"

    def delete_student(self, student_id):
        for student in self.students:
            if student.id_name[0] == student_id:
                self.students.remove(student)
                return "Student deleted successfully"
        return "Student not found"

    def enroll_course(self, student_id, course):
        for student in self.students:
            if student.id_name[0] == student_id:
                student.courses.add(course)
                return f"Enrolled in course: {course}"
        return "Student not found"

    def search_student(self, student_id):
        for student in self.students:
            if student.id_name[0] == student_id:
                return str(student)
        return "Student not found"

    def display_students(self):
        if len(self.students) == 0:
            return "Student Record is empty."

        output = ""
        for student in self.students:
            output += str(student) + "\n"
        return output.strip()


# Sampleeee
records = StudentRecords()
print(records.add_student(1, "Sirk", "sirk@gmail.com", {"math": 90}, {"CS101"}))
print(records.add_student(2, "Yuriel", "yuriel@gmail.com"))
print("\nAll Students:")
print(records.display_students())
print(records.update_student(2, grades={"programming": 88}))
print(records.enroll_course(1, "CS102"))
print("\nSearch Result:")
print(records.search_student(1))
print(records.delete_student(2))
print("\nStudents After Deletion:")
print(records.display_students())
