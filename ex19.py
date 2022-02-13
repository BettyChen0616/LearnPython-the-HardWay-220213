def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, wariables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

print("We can ask inputs from users:")
amount_of_cheese_1 = int(input("How much cheeses do we have?")) #将input的string类型转换为整数
amount_of_crackers_1 = int(input("How many crackers do we have?"))
cheese_and_crackers(amount_of_cheese_1,amount_of_crackers_1)
