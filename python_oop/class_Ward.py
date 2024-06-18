class Person:
    def __init__(self, name, yob):
        self.name = name
        self.yob = yob

    def describe(self):
        # This method is intentionally left empty as no initialization is required for this class.
        pass


class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self.grade = grade

    def describe(self):
        print(
            f"Student - Name: {self.name} - YoB: {self.yob} - Grade: {self.grade}")


class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self.subject = subject

    def describe(self):
        print(
            f"Teacher - Name: {self.name} - YoB: {self.yob} - Subject: {self.subject}")


class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self.specialist = specialist

    def describe(self):
        print(
            f"Doctor - Name: {self.name} - YoB: {self.yob} - Specialist: {self.specialist}")


class Ward:
    def __init__(self, name):
        self.name = name
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def describe(self):
        print(f"Ward Name: {self.name}")
        for person in self.people:
            person.describe()

    def count_doctor(self):
        return sum(1 for person in self.people if isinstance(person, Doctor))

    def sort_age(self):
        self.people.sort(key=lambda person: person.yob)

    def compute_average(self):
        teachers = [
            person for person in self.people if isinstance(person, Teacher)]
        if teachers:
            return sum(teacher.yob for teacher in teachers) / len(teachers)
        return 0


ward = Ward("Ward1")
ward.add_person(Student("studentA", 2010, "7"))
ward.add_person(Teacher("teacherA", 1969, "Math"))
ward.add_person(Teacher("teacherB", 1995, "History"))
ward.add_person(Doctor("doctorA", 1945, "Endocrinologists"))
ward.add_person(Doctor("doctorB", 1975, "Cardiologists"))

ward.describe()
print(f"Number of doctors: {ward.count_doctor()}")
ward.sort_age()
print("After sorting by age:")
ward.describe()
print(f"Average year of birth (teachers): {ward.compute_average()}")
