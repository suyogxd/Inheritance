# # lambda function
# total = lambda a, b:a*b
# print (total(10,10))

# map and filter
#map
# a = [1 , 2, 3 , 4, 5]
# # def increment_by_one(n):
# #     return n+1
# # output = map (increment_by_one , a)
# output = map (lambda n:n+1, a)
# print(list(output))
# print(output)
# print(a)
# names = ["ram", "shyam", "sita", "hari"]
# print (list(map(lambda s:s.capitalize(),names)))
#filter
# a = [1,2,3,4,5]
# cout = list(filter(lambda n: n%2 != 0 , a))
# out = list(filter(lambda n: n%2 == 0 , a))
# print(out)
# print(cout)
# email = [
#     "1@gmail.com",
#     "2@yahoo.com",
#     "3@gmail.com",
#     "4@outlook.com",
#     "5@gmail.com"
# ]
# out = list(filter(lambda n:n.endswith("@gmail.com"), email))
# print(out)
#isinsatnce function
a = [1,2,3,"python","apple",5,6,7]
out = list(filter(lambda n: isinstance(n,int),a))
cout = sum(filter(lambda n: isinstance(n,int),a))
print(out)
print(cout)
