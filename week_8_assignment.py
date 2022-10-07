# set1={4,'v',6.9,4.0,'e'}
# print (set1)


# list1=[”]*3
# print(len(list1))

list1=[1,-2,3]
list2=[1,6,2]

print([[i+j for i in list2] for j in list1])

# list1=[1,-3,0.9,5.6]
# list2 = [int(i) for i in list1]
# print(list2)

# day_1 = [i for i in 'ABCDEFG' if i not in 'aeiou']
# print(day_1)

# li = [6, 24, 25, 16]

# print(li[-1:-4:-1])

# print('Hello World'[::-1])

# def func(c):
#     if(c in 'aeiou'):
#         return c
#     return 'end'
# print(func('i'))

# print(filter(lambda x,y: x if x<y else y,[-3,2,9,0]))

# def fun(lst):
#     def func(n):
#         s=0
#         for i in range(0,n+1):
#             s=s+lst[i]
#         return s
#     for i in range(len(lst)):
#         print(func(i),end='')
# print(fun([1,3,5]))


# def fun(x,y=0,z):
#     print(x-y+z)
# print(fun(1,23))

# range(1,4,0)
# range(2.0,5,2)
# range(3.0,6.0)


# class Person:

 

#     def __init__(self, name, age):

#         self.name = name

#         self.age = age

 
#     def birthday(self):

#         self.age += 1

 

# p1 = Person('Smith', 24)

# p2 = Person('Chris', 30)

# for _ in range(10):

#     p2.birthday()

# num = p1.age + p2.age

# print(num)

# class Leaf:

#     color = 'Green'

# def __init__(self, color):

#     self.color = color

 

# leaf1 = Leaf('Blue')

# color1 = leaf1.color

# leaf1.color = 'Orange'

# color2 = leaf1.color

# color3 = Leaf.color

# print(color1+color3+color2)

# class Fruit:

#     pass

# print(Fruit.__name__)

# class Audio:

 

#     def use(self):

#         print('To listen')

 

# class Video:

 

#     def use(self):

#         print('To see')

 
# class Movie(Audio, Video):

 
#     def use(self):

#         super().use()

 
# m1 = Movie()

# m1.use()

# dic={'a':{3:4,6:2},'t':5,7:{1:3,9:1}}
# print(dic[7][1])

# dic={1.2:2,0.4:4,6.5:5}
# for i in dic:
#     print(i,end="")

# dic={'a':4,'h':2,'w':0,5:4.3}
# dic.clear()
# print(dic)

# def fun(s):

#     if(len(s)==1):

#         return s[0].upper()

#     return fun(s[:-1])+s[-1].lower()


# print(fun("python"))

# def func(x):

#     if(len(x)==0):

#         return 

#     print(x[0]%2==0,end='')

#     return func(x[1:])

# func([1,2,3,4,5])

# def fun(a):

#     if(a>50):

#         return a-3

#     return fun(fun(a+5))

# def op(a,b,c):

#     print(a+b-c)

# op(a=5,c=7,b=2)

# op(c=7,b=2,a=5)

# File: Cars.py



# def car():

#     print('A car')

 

# File: main.py



# from Cars import car

# def car():

#     print('Not a car')

# car()

# Code
# File: minions.py
# def fav_food():

#     print('Bananas')

# if __name__ == '__main__':

#     fav_food()

 

# # File: run_minions.py

# # Code

# # import minions.py

# print(fav_food().fav_food())

# import os

# print(os.listdir())

# print(os.path.exists('modules'))

# class Square:

 
#     def __init__(self, side):
#         self.side = side

#         self.area = side*side

 

# s1 = Square(Square(Square(2).side).area)

# print(s1.area)

# class Sum:

#    def __init__(self, n):

#         self.n = n

# num = 0

# if isinstance(int, object):

# #    num += 1

# # if isinstance(num, object):

# #     num += 4

# # if isinstance(Sum, object):

# #     num += 6

# # N = Sum(num)

# # if isinstance(N, (object, Sum)):

# #     num += 2

# # print(N.n + num)

# class Person:

#     def __init__(self, name, age):

#         self.name = name

#         self.age = age

# age = 50

 

# p1 = Person('Sam', 24)

# print(p1.name, p1.age)

