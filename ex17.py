from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# in_file = open(from_file)
# indata = in_file.read()
indata = open(from_file).read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")#确认复制的目标文件存在
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close() #保存关闭文件
# in_file.close()

'''
(base) % echo "This is a test flie." > test.txt #创建一个测试txt，写入内容
(base) % cat test.txt  #读取测试文档的内容
This is a test flie.

(base) % python3.8 ex17.py test.txt new_file.txt
Copying from test.txt to new_file.txt
The input file is 21 bytes long
Does the output file exist? False #复制的目标文件new_file.txt尚未创建
Ready, hit RETURN to continue, CTRL-C to abort.

Alright, all done.
'''
