class Person:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def print_person(self):
        print(self.name, self.age)

    def increase_age(self, years):
        self.age += int(years)
        return self.age


person = Person('rajon', 40)
print(person.increase_age(10))
