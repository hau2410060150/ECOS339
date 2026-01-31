from Student import Student


class StudentManager:
    student_list = []

    def generate_id(self):
        max_id = 1
        if self.get_student_count() > 0:
            max_id = self.student_list[0]._id
            for sv in self.student_list:
                if max_id < sv._id:
                    max_id = sv._id
            max_id += 1
        return max_id

    def get_student_count(self):
        return len(self.student_list)

    def input_student(self):
        sv_id = self.generate_id()
        name = input("Enter student name: ")
        gender = input("Enter student gender: ")
        major = input("Enter student major: ")
        gpa = float(input("Enter student GPA: "))

        sv = Student(sv_id, name, gender, major, gpa)
        self.classify_academic_performance(sv)
        self.student_list.append(sv)

    def update_student(self, student_id):
        sv: Student = self.find_by_id(student_id)
        if sv is not None:
            name = input("Enter student name: ")
            gender = input("Enter student gender: ")
            major = input("Enter student major: ")
            gpa = float(input("Enter student GPA: "))

            sv._name = name
            sv._gender = gender
            sv._major = major
            sv._gpa = gpa

            self.classify_academic_performance(sv)
        else:
            print("Student with ID = {} does not exist.".format(student_id))

    def sort_by_id(self):
        self.student_list.sort(key=lambda x: x._id, reverse=False)

    def sort_by_name(self):
        self.student_list.sort(key=lambda x: x._name, reverse=False)

    def sort_by_gpa(self):
        self.student_list.sort(key=lambda x: x._gpa, reverse=False)

    def find_by_id(self, student_id):
        result = None
        if self.get_student_count() > 0:
            for sv in self.student_list:
                if sv._id == student_id:
                    result = sv
        return result

    def find_by_name(self, keyword):
        result_list = []
        if self.get_student_count() > 0:
            for sv in self.student_list:
                if keyword.upper() in sv._name.upper():
                    result_list.append(sv)
        return result_list

    def delete_by_id(self, student_id):
        is_deleted = False
        sv = self.find_by_id(student_id)
        if sv is not None:
            self.student_list.remove(sv)
            is_deleted = True
        return is_deleted

    def classify_academic_performance(self, sv: Student):
        if sv._gpa >= 8:
            sv._academic_performance = "Excellent"
        elif sv._gpa >= 6.5:
            sv._academic_performance = "Good"
        elif sv._gpa >= 5:
            sv._academic_performance = "Average"
        else:
            sv._academic_performance = "Poor"

    def show_students(self, student_list):
        print("{:<8} {:<18} {:<8} {:<10} {:<8} {:<10}"
              .format("ID", "Name", "Gender", "Major", "GPA", "Performance"))

        if len(student_list) > 0:
            for sv in student_list:
                print("{:<8} {:<18} {:<8} {:<10} {:<8} {:<10}"
                      .format(sv._id, sv._name, sv._gender,
                              sv._major, sv._gpa, sv._academic_performance))
        print("\n")

    def get_student_list(self):
        return self.student_list