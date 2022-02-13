from sys import argv
script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C)") #ctrl-c 按键中断脚本的运行
print("If you do want that, hit RETURN.")

input("?") #换行键直接运行下一行代码

print("Opening the file...")
target = open(filename, 'w') #读取文件本身，并允许改写内容.
# 'w' for writing (truncating the file if it already exists)

print("Truncating the file. Goodbye!") #在'w'模式下，文件内容默认自动删除，不需要truncate函数
target.truncate() #删除文件内容

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ") #第一行
line2 = input("line 2: ") #第二行
line3 = input("line 3: ") #第三行

print("I'm going to write these to the file.")

# target.write(line1) #文件写入第一行
# target.write("/n") #第一行末尾写入换行
# target.write(line2)
# target.write("/n")
# target.write(line3)
# target.write("/n")

target.write(f'''
{line1}/n{line2}/n{line3}/n
''')

print("And finally, we close it.")
target.close() #保存，关闭文件

'''
readline() #读取txt第一行
read() #读取文件内容
seek(0) #找到文件内容开头位置
write('stuff') #文件写入stuff
close() #保存关闭
-----------------------------------------
(base) % python3.8 ex16.py ex16_test.txt
We're going to erase ex16_test.txt.
If you don't want that, hit CTRL-C (^C)
If you do want that, hit RETURN.
?
Opening the file...
Truncating the file. Goodbye!
Now I'm going to ask you for three lines.
line 1: 我用什么才能留住你
line 2: 我给你瘦落的街道、绝望的落日、荒郊的月亮
line 3: 我给你一个久久地望着孤月的人的悲哀
I'm going to write these to the file.
And finally, we close it.
(base) %
'''
