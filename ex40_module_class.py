'''
When you instantiate a class what you get is called an object
'''

class Song(object):

    def __init__(self, lyrics): #__init__前后有两条“_”
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_baby = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

happy_baby.sing_me_a_song()
bulls_on_parade.sing_me_a_song()

'''
(base) % python ex40_module_class.py
Traceback (most recent call last):
  File "ex40_module_class.py", line 14, in <module>
    happy_baby = Song(["Happy birthday to you",
TypeError: Song() takes no arguments
init前后需要两条 “_”
-----------
(base) % python ex40_module_class.py
Happy birthday to you
I don't want to get sued
So I'll stop right there
They rally around the familyWith pockets full of shells
(base) % python ex40_module_class.py
Happy birthday to you
I don't want to get sued
So I'll stop right there
They rally around the family
With pockets full of shells
'''
