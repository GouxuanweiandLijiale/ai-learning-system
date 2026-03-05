name = input("what is your name?:")
print("hello " , name)
time = int(input("How much time do you spend on coding,today: "))
if time >= 120:
    print("super good!")
elif time <120 and time >=90:
    print("good job!")
elif time <90 and time >=60:
    print("finish goal!")
elif time <60 and time >=30:
    print("keep going!")
else:
    print("try harder!")
plan = input("Do you finish your plan today? (yes/no): ")
if time >= 60 and plan == "yes":
    print("today you reach your goal, keep it up!")
else:
    print("try harder tomorrow!")
age = int(input("what is your age?: "))
if age < 18:
    print("you are an teenager!")
elif age >= 18 and age < 60:
    print("you are an adult!")
else:
    print("you are a senior!")
if time < 30 or time >180 :
    print("you should schedule your time better!")