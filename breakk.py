# for i in range(10):
#     n = int(input("enter num:"))
#     if n == 9:
#         break
#     print(n)
# else:
#     print("loop completed")
# for i in range(10):
#     n = int(input("enter num:"))
#     if n ==9:
#         continue
#     print(n)
# else:
#     print("loop completed")

# username = "r@gmail.com"
# password = "123@abcd"
# n = input("enter username: ")
# m = input("password: ")
# while n == username and m == password:
#      n = input("enter username: ")
#      m = input("password: ")
# if n == username and m == password:
#         print("login successful !!!")
# else:
#         print("incoorect username or password !!!")

a = [(1,2,3),(5,6,7),(8,9,0)]
sum = 0 
for i in a:
    sum += int ("".join([str(j) for j in i]))
print(sum)


