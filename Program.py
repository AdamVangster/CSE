class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self):
        print("%s goes to work" % self.name)

    def birthday(self):
        print("It's you birthday, you just turned %s today" % self.age)


class Employee(Person):
    def __init__(self, name, age, skills):
        super(Employee, self).__init__(name, age)
        self.skills = skills

    def work(self):
        print("You employee, %s, is working really hard." % self.name)

    def age(self):
        print("You employee just turn %s today." % self.age)


class Programmer(Employee):
    def __init__(self, name, age, skills):
        super(Programmer, self).__init__(name, age, skills)

    def work(self):
        print("%s work as a programmer in your company." % self.name)

    def age(self):
        print("%s, your employee just turned %s today." % self.name % self.age)

    def skills(self):
        print("%s have skills to %s a game in one day" % self.name % self.skills)


CEO = Person('Jake', 40)
CEO.work()
CEO.birthday()
