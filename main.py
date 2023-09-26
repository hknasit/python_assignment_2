class Vehicle:
    def __init__(self, name_of_vehicle, max_speed, average_speed):
        self.name_of_vehicle = name_of_vehicle
        self.max_speed = max_speed
        self.average_speed = average_speed

class Car(Vehicle):
    def seating_capacity(self, capacity):
        return f"{self.name_of_vehicle} has a seating capacity of {capacity} passengers."

my_car = Car("Sedan", 180, 50)
print(f"{my_car.name_of_vehicle} has a maximum speed of {my_car.max_speed} km/h and an average speed of {my_car.average_speed} km/h.")
print(my_car.seating_capacity(5))

class College:
    def address(self):
        return f"Mississauga, Ontario, Canada"

college = College()


class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def say_hello(self):
        print(f"Hello, my name is {self.name}!")

    def is_adult(self):
        return self.age >= 18

harsh = Person("Harsh", 25, "Male")
print(harsh.say_hello())
print(harsh.is_adult())

class Student(Person):
    def __init__(self, name, age, gender, student_id, course):
        super().__init__(name, age, gender)
        self.student_id = student_id
        self.course = course

    def get_student_info(self):
        return f"Student ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Course: {self.course}"

student1 = Student("Harsh", 25, "Male", "c04125", "Computer Science")
student1.say_hello()
print(f"{student1.name} is an adult: {student1.is_adult()}")  # Output: John is an adult: True
print(student1.get_student_info())

class Teacher(Person):
    def __init__(self, name, age, gender, teacher_id, subject):
        super().__init__(name, age, gender)
        self.teacher_id = teacher_id
        self.subject = subject

    def say_hello(self):
            print(f"Hello, I'm a teacher named {self.name}!")


teacher1 = Teacher("Mr. Namra", 50, "Male", "T9876", "Mathematics")
teacher1.say_hello()
print(f"{teacher1.name} is an adult: {teacher1.is_adult()}")

