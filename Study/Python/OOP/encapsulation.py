"""
Escapsulation is the act of preventing direct access to certain methods and attributes of a class. It is helpful for making your code more secure and prevent some unwanted behavior as well. 

In Python, it is as mere convention, as the language does not provide us with a feature to making these attributes and methods 'private'. So, you just name the variable or the method with a leading underscore, such as _name and _age

"""


class Student:
    def __init__(self, name, age) -> None:
        self._name = name
        self._age = age

    def info(self):
        print(f"\nThe student's is {self._age} years old and is called {self._name}")


if __name__ == "__main__":
    student = Student(name="Sandro", age=28)
    student.info()

    print(f"\n\n {student._name}")
