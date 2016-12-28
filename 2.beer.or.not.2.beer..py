import time
import random
bottle_count=0
def guess():
    print("guess from 1 to 12:")
    bottle_count = random.randint(1,12)
    found=False
    while not found:
        user=eval(input("your guess:"))
        
        if user==bottle_count:
            print("congradulations!")
            found=True
        elif user>bottle_count:
            print("I'm not an alcoholic,\nless")
        else:
            print("you think I'm a P*ssy?\nmore")

name=str(input("hello, what should i call you?\n"))
print(name+" is a nice name")
time.sleep(1)
print("how old are you "+name+"?")
age=eval(input("age:"))
##I want this part to check if the entered age is an int and only than proceed
##while type(age)!=int:
##    print("I can only understand whole numbers "+name)
##    age=eval(input("age:"))
if age>18:
    print("ah...you can legally drink in this world "+name+"!")
    time.sleep(1)
    print("now tell me how many bottles can you drink in an hour?")
    bottle_count=eval(input("from 1 to 12:"))
    while bottle_count>12:
                      print("it must be between 1 and 12")
                      bottle_count=eval(input("from 1 to 12:"))
    
                      
                      

    if bottle_count<=12 and bottle_count>0:
                          
                          print(str(bottle_count)+" bottles is impressive for a "+str(age)+" year old")
                          time.sleep(1)
                          print("however")
                          time.sleep(1)
                          print("...")
                          time.sleep(1)
                          print("never mind, I forgot what I wanted to say.")
                          time.sleep(1)
                          print("can you guess how much I can drink in an hour?")
                          time.sleep(1)
                          guess()

                      
                      
elif age<18 and age>16:
    print("if you ever want a beer just ask,\nit's not legal for someone of your age but for me\nage is just a number.")
else:
    print(str(18-age)+"years left and you can enjoy our tasty beer.")

