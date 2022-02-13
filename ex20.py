from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0) #回到开头

def print_a_line(line_count, f):
    print(line_count, f.readline())
#输入的行数，从第一行开始print，行数和print第几行没有联系！

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file) #找到文档开头

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)
#print一行， moving the read head to right after the \n that ends that line
#print一行到/n截止，且在末尾自动添加一个 end = " " ，因此print的两行之间空一行？

current_line = current_line + 1
print_a_line(current_line, current_file)

# current_line = current_line + 1
current_line += 1
print_a_line(current_line, current_file)

'''
python3.8 ex20.py ex16_origin.txt
First let's print the whole file:

What can I hold you with?
   I offer you lean streets, desperate sunsets, the
      moon of the jagged suburbs.
   I offer you the bitterness of a man who has looked
      long and long at the lonely moon.
   I offer you my ancestors, my dead men, the ghosts
      that living men have honoured in bronze:
      my father's father killed in the frontier of
      Buenos Aires, two bullets through his lungs,
      bearded and dead, wrapped by his soldiers in
      the hide of a cow; my mother's grandfather
      --just twentyfour-- heading a charge of
      three hundred men in Peru, now ghosts on
      vanished horses.
   I offer you whatever insight my books may hold,
      whatever manliness or humour my life.
   I offer you the loyalty of a man who has never
      been loyal.
   I offer you that kernel of myself that I have saved,
      somehow --the central heart that deals not
      in words, traffics not with dreams, and is
      untouched by time, by joy, by adversities.
   I offer you the memory of a yellow rose seen at
      sunset, years before you were born.
   I offer you explanations of yourself, theories about
      yourself, authentic and surprising news of
      yourself.
   I can give you my loneliness, my darkness, the
      hunger of my heart; I am trying to bribe you
      with uncertainty, with danger, with defeat.


                     - Jorge Luis Borges (1934)

Now let's rewind, kind of like a tape.
Let's print three lines:
1 What can I hold you with?

2    I offer you lean streets, desperate sunsets, the

3       moon of the jagged suburbs.


'''
