"""
most of the uses of inheritance can be simplified or replaced with
composition, and multiple inheritance should be avoided at all costs.
"""

class Parent(object):

    def implicit(self):
        print("PARENT implicit()")

#Actions on child imply an action on the parent.
class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

"""
(base) % python ex44_inheritance.py
PARENT implicit()
PARENT implicit()
"""
