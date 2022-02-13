types_of_people = 10
x = f"There are {types_of_people} types of people." #f-string

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}." # 表示两个变量的f-string

print(x)
print(y)

print(f"I said: {x}") #f-string中套f-string
print(f"I also said: '{y}'") # f-string中的''仍旧可以表示

hilarious =False
Joke_evaluation = "Isn't that joke so funny?! {}" #预留显示变量的位置{}

print(Joke_evaluation.format(hilarious)) #使用format函数填上预留位置{};逻辑值直接显示为False

w = "This is the left side of ..."
e = "a string with a right side."

print(w + e)
