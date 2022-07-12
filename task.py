heroes = ['spiderman', 'thor', 'hulk', 'ironman', 'captain america']


# 1. Print the length of list.
# 2. Add 'black panther' at the end of this list
# 3. You realize that you need to add 'black panther' after 'hulk', so remove it from th elist first and then add it after 'hulk'.
# 4. Now you dont like thor and hulk beccause they get angry easily    
#         So you want to remove thor and hulk from list and replace them with doctor strange(because he is cool).Do that with one lin eof code.
# 5. Sort the heroes list in alphabetical order.

print(len(heroes))
heroes.append('black panther')
print(heroes)
heroes.remove('black panther')
heroes.insert(3,'black panther')
print(heroes)
print(heroes[1:3])
heroes[1:3] = ["wakanda"]
print(heroes)
heroes.sort()
print(heroes)
