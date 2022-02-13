from sys import argv

script, filename = argv #命令行输入文件名

txt = open(filename) # what you get back from open is a file, 读取文件本身

print(f"Here's your file {filename}:")
print(txt.read()) # 读取文件内容

print("Type the filename again:")
file_again = input("> ") #脚本运行过程输入文件名

txt_again = open(file_again)#读取文件本身

print(txt_again.read())#读取文件内容

file_again.close() # 关闭文件

"""
(base) % python3.8 ex15.py ex15_sample.txt
Here's your file ex15_sample.txt:
This is stuff I typed into a file.
It is really cool stuff.
Lots and lots of fun to have in here.

Type the filename again:
> ex15_sample.txt
This is stuff I typed into a file.
It is really cool stuff.
Lots and lots of fun to have in here.

在该目录下运行python
(base) % python

>>> txt=open('ex15_sample.txt')
>>> txt.read()
'This is stuff I typed into a file.\nIt is really cool stuff.\nLots and lots of fun to have in here.\n'
>>> quit()
(base) %
"""
