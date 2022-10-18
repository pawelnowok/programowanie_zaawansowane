class Student:
    def __init__(self, name: int, marks: list):
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        avg = sum(self.marks)/len(self.marks)
        return avg > 50

student1 = Student("Pyjter", [35, 40, 69, 70, 58, 21, 45, 87, 100, 11])
print(student1.is_passed())

student2 = Student("Mareczek", [12, 11, 67, 34, 88, 17, 36, 79, 5, 23])
print(student2.is_passed())
