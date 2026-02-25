# # # # # # from os import name


# # # # # # cars =['audi','bmw','subaru','toyota']

# # # # # # for car in cars:
# # # # # #     if car == 'bmw':
# # # # # #         print(car.upper())
# # # # # #     else:
# # # # # #         print(car.title())


# # # # # # name = 'mary'
# # # # # # password ='python123'



# # # # # # if name == 'mary':
# # # # # #     print("Hello, Mary, would you like to learn some Python today?")
# # # # # #     if password == 'python123':
# # # # # #         print("Access granted.")


# # # # # # age =19 

# # # # # # if age >=18:
# # # # # #     print("you are old enough to vote!")

# # # # # # else:
# # # # # #     print("sorry,you are too young to vote.")


# # # # # # age =12

# # # # # # if age <4:
# # # # # #     print("Your admission cost is $0.")
# # # # # # elif age <18:
# # # # # #     print("Your admission cost is $5.")
# # # # # # else:
# # # # # #     print("Your admission cost is $10.")

# # # # # from http.client import PRECONDITION_FAILED


# # # # # age =12

# # # # # if age <4:
# # # # #     price=0
# # # # # elif age <18:
# # # # #     price=5
# # # # # else:
# # # # #     price=10

# # # # # print(f"Your admission cost is ${price}.")


# # # # requested_toppongs=['mushrooms','extra cheese']

# # # # if 'mushrooms' in requested_toppongs:
# # # #     print("adding mushrooms.")
# # # # elif 'pepperoni' in requested_toppongs:
# # # #     print("adding pepperoni.")

# # # # elif 'extra cheese' in requested_toppongs:
# # # #     print("adding extra cheese.")

# # # # print("\nFinished making your pizza!")


# # # alien_color ='green'

# # # if alien_color == 'green':
# # #     print("you just earned 5 points!")
# # # else:
# # #     print("you just earned 10 points!")

# # age = int(input("Enter your age: "))

# # if age <2:
# #     print("you are a baby.")
# # elif age>=2 and age <4:
# #     print("you are a toddler.")
# # elif age >=4 and age <13:
# #     print("you are a kid.")
# # elif age>=13 and age <20:
# #     print("you are a teenager.")
# # elif age >=20 and age <65:
# #     print("you are an adult.")
# # else:
# #     print("you are an elder.")

# x=2

# print(type(x))

# # # if type conversion is happening internally then it is called implicit type conversion

# # #if we do type conversion by ourselves then it is called explicit type conversion

# # # int() -> converts string to integer
# # # float() -> converts integer to float
# # # str() -> converts integer/float to string
# # # bool() -> converts integer/float/string to boolean

from urllib import request


available_topplings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_topplings = ['mushrooms', 'french fries', 'extra cheese']

for requested_toppling in requested_topplings:
    if requested_toppling in available_topplings:
        # Use the singular variable here!
        print(f"Adding {requested_toppling}.")
    else:
        print(f"Sorry, we don't have {requested_toppling}.")