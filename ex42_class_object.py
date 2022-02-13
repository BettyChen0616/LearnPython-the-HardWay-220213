## Animal is-a object
class Animal(object):
    pass

#Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        #dog has-a name
        self.name = name

#cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        #Cat has-a name
        self.name = name

#Person is-a object
class Person(object):

    def __init__(self, name):
        #person has-a name
        self.name = name
        #person has-a pet of some kind
        self.pet = None

#Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):

        '''用子类对象调用父类已被覆盖的方法
        Employee has-a name and has-a pet of some kind'''
        super(Employee, self).__init__(name)
        #Employee has-a salary
        self.salary = salary

#fish is-a object
class Fish(object):
    pass

#Salmon is-a Fish
class Salmon(Fish):
    pass

#Halibut is-a Fish
class Halibut(Fish):
    pass

#rover is-a dog
rover = Dog("Rover")

#satan is-a Cat
satan = Cat("Satan")

#mary is-a Person
mary = Person("Mary")

#mary has-a pet called Satan
mary.pet = satan

#frank is-a Employee
frank = Employee("Frank", 120000)

#frank has-a pet called Rover
frank.pet = rover

#flipper is-a Fish
flipper = Fish()

#crouse is-a Salmon
crouse = Salmon()

#harry is-a Halibut
harry = Halibut()
