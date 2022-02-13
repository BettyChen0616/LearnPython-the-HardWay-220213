'''
class, object/instance, inheritance <=> composition,
attribute, is-a <=> has-a
'''

import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%)":
        "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)":
        "class %%% has-a __init__ that takes self and *** params.",
    "class %%%(object):\n\tdef ***(self, @@@)":
        "class %%% has-a function *** that takes self and @@@ params.",
    "*** = %%%()":
        "Set *** to an instance of class %%%.",
    "***.***(@@@)":
        "From *** get the *** function, call it with params self, @@@.",
    "***.*** = '***'":
        "From *** get the *** attribute and set it to '***'."
}

#do they want to dill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASES_FIRST = True
else:
    PHRASES_FIRST = False

#load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding="utf-8"))

def convert(snippet, phrase):
    #从words中随机抽取n个word,生成list，大写
    class_names = [w.capitalize() for w in
                   random.sample(WORDS, snippet.count("%%%"))]
    #从words中随机抽取m个word，生成list
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        #生成一个1到3的随机整数
        param_count = random.randint(1,3)
        #从words中抽取随机数个word,用‘，’连接，写入param_names数列
        param_names.append(', '.join(
            random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        result = sentence[:]

        #fake class class_names
        for word in class_names:
            #一次替换一个
            result = result.replace("%%%", word, 1)

        #fake other class_names
        for word in other_names:
            result = result.replace("***", word, 1)

        #fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results


#keep going until they hit CTRL-D
try:
    while True:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASES_FIRST:
                question, answer = answer, question

            print(question)

            input("> ")
            print(f"ANSWER: {answer}\n\n")
except EOFError:
    print("\nBye")


'''
(base) % python ex41_Object.py
driving = Bit()
> set driving to an instance of class Bit.
ANSWER: Set driving to an instance of class Bit.


class Coil(Can)
> make a class named Coil that is a Can
ANSWER: Make a class named Coil that is-a Can.


coil.cub(competition)
> from coil get the cub function that takes self and competition params
ANSWER: From coil get the cub function, call it with params self, competition.


class Dad(object):
	def balloon(self, current)
> class Dad has-a balloon function take self and current params
ANSWER: class Dad has-a function balloon that takes self and current params.


class Army(object):
	def __init__(self, bulb)
> class Army has-a funtion __init__ that takes self and bule params
ANSWER: class Army has-a __init__ that takes self and bulb params.


bubble.creature = 'base'
> from bulle get the creature attribute and set it to 'base'
ANSWER: From bubble get the creature attribute and set it to 'base'.


class Disgust(object):
	def __init__(self, argument)
> ^D
Bye
(base) %

'''
