def print_two(*args): #输入数列赋与变量args，类似argv
    arg1, arg2 =args
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("I got nothin'.")


print_two("Simon","Kris")
print_two_again("Simon","Kris")
print_one("First!")
print_none()
