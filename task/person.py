class Person:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def print_person(self):
        return self.name + ' ' + self.age

    def increase_age(self, years):
        years = 10
        self.age = self.age + years
        return self.age


person = Person('rajon', 40)
print(person.increase_age(10))
