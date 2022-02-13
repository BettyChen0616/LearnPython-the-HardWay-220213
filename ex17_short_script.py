from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

print(f"Does the output file exist? {exists(to_file)}")#确认复制的目标文件存在
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

open(to_file, 'w').write(open(from_file).read())

print("Alright, all done.")
