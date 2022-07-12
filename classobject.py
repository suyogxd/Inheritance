# class Car:
#     def __init__(self,model,color):
#         self.m = model
#         self.c = color

# c = Car("2022" , "Black")
# print(c.m)
# print(c.c)
# class Book:
#     def __init__(self,page,read):
#         self.p = page
#         self.r = read
# a = Book("1027","27th line")
# print(a.p)
# print(a.r)
# class Page:
#     def __init__(self,page_number,content):
#         self.page_number = page_number
#         self.content = content

#     def read(self):
#         print(f"Reading{self.content} of page number {self.page_number}")

#     @staticmethod
#     def print_to_printer(content):
#         print(f"Printing.......")
#         print(content)
#     def __str__(self):
#         return self.content
#     def __repr__(self):
#         return self.content
#     def get_content(self,pagenumber):
#         for i in self.pages:
#             return i.content
#         return "page not found"


#     # p = Page(1, "This is a paragraph.")
#     # p.read()
#     # Page.print_to_printer("This is sentence.")
# class Book:
#     def __init__(self,title,pages):
#         self.title = title
#         self.pages = pages
    
#     def no_of_pages(self):
#         return len(self.pages)
    
#     def add_pages(self,page):
#         self.pages.append(page)
#     def __str__(self):
#         return self.title
    

# pages = []
# for i in range(1,6):
#     p = Page(i, f"This is  a paragraph {i}.")
#     pages.append(p)

# b = Book("Maths" , pages)
# print(f"Number of pages: {b.no_of_pages()}")
# print(b)
# print(p)
# print(b.pages)
try:
    n1 = int(input("Enter the number:"))
    n2 = int(input("Enter the number:"))
except ValueError:
    print("cannot convert to interger")
except NameError:
    print("variable not defined")
else:
    print(n1+n2)

