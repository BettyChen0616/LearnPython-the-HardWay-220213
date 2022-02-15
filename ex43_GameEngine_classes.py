'''
1. write or draw about the problem.
2. extract key concepts from 1 and research them.
3. create a class hierarchy and object map for the concepts.
4. code the classes and a test to run them.
5. repeat and refine.
'''
class Scence(object):

    def enter(self):
        pass

class Engine(object):

    def __init__(self, scence_map):
        pass

    def play(self):
        pass

class Death(Scence):

    def enter(self):
        pass

class CentralCorridor(Scence):

    def enter(self):
        pass

class LaserWeaponArmory(Scence):

    def enter(self):
        pass

class TheBridge(Scence):

    def enter(self):
        pass

class EscapePod(Scence):

    def enter(self):
        pass

class Map(object):

    def __init__(self, start_scene):
        pass

    def next_scene(self, scence_name):
        pass

    def opening_scene(self):
        pass

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
