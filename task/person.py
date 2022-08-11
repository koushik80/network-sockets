class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def _person(self):
        print(f'{self.name} {self.age}')

    def increase_age(self, years):
        self.age += years


person = Person('rajon', 40)
print(person)

# if __name__ == '__main__':
#person = Person('rajon', 40)
# print(person)
