class Student:
    def __init__(self, student_id, name, gender, major, gpa):
        self._id = student_id
        self._name = name
        self._gender = gender
        self._major = major
        self._gpa = gpa
        self._academic_performance = ""