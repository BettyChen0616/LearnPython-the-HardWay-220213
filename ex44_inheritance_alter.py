class Parent(object):

    def altered(self):
        print("PARENT altered()")

class Child(Parent):

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        # get the Parent class
        super(Child, self).altered()
        print("CHILD, AFTER PRINT altered()")

dad = Parent()
son = Child()

dad.altered()
son.altered()

"""
(base) % python ex44_inheritance_alter.py
PARENT altered()
CHILD, BEFORE PARENT altered()
PARENT altered()
CHILD, AFTER PRINT altered()
"""
