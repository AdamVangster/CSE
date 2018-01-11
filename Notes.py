# print("Hello World!")
#
# # Adam Vang
#
# a = 4
# b = 3
#
# print(3 - 5)
# prs = 8
# print(3 * 5)
# print(6 / 2)
# print(3 ** 2)
#
# print
# print("Try to figure out how this work")
# print(15 % 5)
# # The "%" sign is a modulus. It finds the remainder
#
# car_mpg = 5000.9
# car_name = "The Wiebe Mobile"
# car_type = "BMW"
# car_cylinder = 8
# car_mpg = 5000.9
#
# print("I have a car called %s. It's pretty nice." % car_name)
# print("I have a car called %s. It's a %s" % (car_name, car_type)) # Watch the order
#
# Here is where we get a little fancy
# print("What is your name?")
# name = input(" ")
# print("Hello %s." % name)
#
# age = 15
# print("How old are you?")
# age = input(" ")
# print ("%s! That's really old. You belong in a retirement home." % 15)
#
# print("My favorite character in League of Legend is Rakan")
#
# # Function
# # Indent is 4 spaces
#
#
# def print_hw():
#     print("Hello World.")
#     print("Enjoy the day")
#
# print_hw()
#
# def say_hi(name):
#     print("Hello %s" % name)
#     print("Coding is great!")
#
#
# def print_age(name, age):
#     print("%s is %d years old" % (name, age))
#     age += 1  # age = age + 1
#     print ("Next year, %s will be %d year old" % (name, age))
#
#
# print_age("John", 15)
#
#
# def algebra_hw(x):
#     return x**3 + 4*x**2 + 7 * x - 4
#
#
# print(algebra_hw(3))
# print(algebra_hw(4))
# print(algebra_hw(5))
# print(algebra_hw(6))
# print(algebra_hw(7))
#
#
# # if statements
#
#
# def grade_calc(percentage):
#     if percentage >= 90:
#         return "A"
#     elif percentage >= 80:  # else if
#         return "B"
#     elif percentage >= 70:
#         return "C"
#     elif percentage >= 60:
#         return "D"
#     elif percentage >= 50:
#         return "F"
#
# print(grade_calc(59))
# def happy_bday(name):
#     print("Happy Birthday to you")
#     print("Happy Birthday to you" + ',')
#     print("Happy Birthday dear " + name + ',')
#     print("Happy Birthday to you" + ',')
#
# happy_bday("Adam")
#
# # Loops
#
# for num in range(10):
#     print(num + 1)
# def happy_bday(name):
#     print("Happy Birthday to you" + ',')
#
# # While Loops (Beware!!!)
#
# a = 1
# while a < 10: # This is the condition,
#                 # it must be true to execute
#     print(a)
#     a += 1  # This iterates so that we can break the loop
#
# # Random Numbers
# import random # This should be on line 1
# print(random.randint(0, 1000))
#
#
# Recasting
c = '1'
print(c == 1)  # We have a string and an int
print(int(c) == 1)
print(c == str(1))


# Comparisons

print( 1 == 1)  # Use a double equal sign
print(1 != 2)  # 1 is not equal to 2
print( not False)


#