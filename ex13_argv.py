from sys import argv #argument variable 引数  import modules模块 / libraries库
script, first, second, third = argv #unpack argv;在cammand line 中输入，默认形式为文本
forth = input("forth?") # 在脚本运行过程中输入

print("The script is called:", script)
print("Your first variabe is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
print("Your third variable is:", forth)
