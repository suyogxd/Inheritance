# def product_one(num1, num2):
#     print (num1 * num2)

# ans = product_one(10,12)
# print(f"Answer: {ans}")

# def product_two(num1, num2):
#     return(num1*num2)
# ans = product_two(10,12)
# print(f"Answer: {ans}")

# def example (*args):
#     print(a)
# example(1,2,3,4,5,6)

# def example_two(**kwargs):
#     print(a)

# example_two(name="jethiya" , address= "gokuldham")

# def example_three (*args , **kwargs):
#     print(args)
#     print(kwargs)

# example_three(1,2,3,4,5, name= "chempuk", address= "bhachau")

# def profile(name, contact, address):
#     print(f"Name : {name}")
#     print(f"Contact : {contact}")
#     print(f"Address : {address}")

# pro = {"name": "daya", "contact": "98580", "address" : "amdabad"}
# profile(**pro)

# def welcome(name):
#     print(f"Welcome {name}")

# def greeting(func):
#     func("Jethalal")
# greeting(welcome)

# def square_root_of_sum(func, num1, num2):
#     return func(num1 , num2)**0.5
# def add (num1 , num2):
#     return num1 + num2
# print (square_root_of_sum(add,30,6))

# def outer_func():
#     def first_child():
#         print("I am first child")
#     def second_child():
#         print("I am second child")
#     first_child()
#     second_child()

# outer_func()

# def calculator(operator):
#     def add(a,b):
#         return a+b
#     def product(a,b):
#         return a*b
#     if operator == "+":
#         return add
#     elif operator == "*":
#         return product

# totalsum = calculator("+")
# multiply = calculator("*")
# print(totalsum(2,3))
# print(multiply(2,3))

# def calculator(operator, a, b):
#     def add():
#         return a+b
#     def product():
#         return a*b
#     if operator == "+":
#         return a+b
#     elif operator =="*":
#         return a*b
# a = calculator("+",10,15)
# print(a)
# b = calculator("*",10,15)
# print(b)    