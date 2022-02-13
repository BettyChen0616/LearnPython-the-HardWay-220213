def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')#根据空格来分割句子
    return words

def sort_words(words):
    return sorted(words)

def print_first_word(words):
    word = words.pop(0)
    print(word)

def print_last_word(words):
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

'''
(base) % python3.8
Python 3.8.5 (default, Sep  4 2020, 02:22:02)
[Clang 10.0.0 ] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import ex25
>>> sentence = "All good things come to those who wait."
>>> words = ex25.break_words(sentence)
>>> words
['All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait.']
>>> sorted_words = ex25.sort_words(words)
>>> sorted_words
['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
>>> ex25.print_first_word(words)
All
>>> ex25.print_last_word(words)
wait.

>>> sorted_words
['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']

>>> sorted_words = ex25.sort_sentence(sentence)
>>> sorted_words
['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
>>> ex25.print_first_and_last(sentence)
All
wait.
>>> ex25.print_first_and_last_sorted(sentence)
All
who
>>> help(ex25)

Help on module ex25:

NAME
    ex25

FUNCTIONS
    break_words(stuff)
        This function will break up words for us.

    print_first_and_last(sentence)

    print_first_and_last_sorted(sentence)

    print_first_word(words)

    print_last_word(words)

    sort_sentence(sentence)

    sort_words(words)

FILE
    /Users/jiayuchen/github/LPython_HardW/ex25.py

q 退出

>>> help(ex25.break_words)

Help on function break_words in module ex25:

break_words(stuff)
    This function will break up words for us.
(END)


'''
