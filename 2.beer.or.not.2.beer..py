name=str(input("hello, what should i call you?\n"))
print(name+" is a nice name")
print("how old are you "+name+"?")
age=input("age:")
while type(age)!=int:
    print("I can only understand whole numbers "+name)
    age=eval(input("age:"))
if age>18:
    print("ah...you can legally drink in this world "+name+"!")
elif age<18 and age>16:
    print("if you ever want a beer just ask,\nit's not legal for someone of your age but for me\nage is just a number.")
else:
    print(str(18-age)+"years left and you can enjoy our tasty beer.")

