#1 Create a 2-D array and slice out the second number in the second column


numz = [[20,30],[12,89], [100,75]]

print(numz)
numz[1].pop(1)
print(numz)

#2 Write a python program to sort array element into the ascending/ descending order 
def my_sorting(input_list):
   for i in range(len(input_list)):
      for j in range(i+1,len(input_list)):
          if input_list[i] > input_list[j]:
              input_list[i],input_list[j] = input_list[j],input_list[i]
   return input_list

#3  Write a python program to find the maximum and minimum value in a given 2-D array

import numpy as np
x = np.arange(4).reshape((2, 2))
print("\nOriginal array:")
print(x)
print("\nMaximum value along the second axis:")
print(np.amax(x, 1))
print("Minimum value along the second axis:")
print(np.amin(x, 1))

#4. Write a python program to input 5 subject marks and calculate total marks, percentage and grade based on following criteria
#         percentage less than 50 (Grade C)
#         percentage equal to 50 and less than 80 (Grade B)
#         percentage equal to 80 and more than 80 (Grade A)

marks = {} 
total = 0 
subjects = ["Math", "English", "Physics", "Chemistry", "Hindi"] 
 
for subject in subjects: 
    marks[subject] = input("Enter " + subject + " marks : ") 
 
for key in marks.values(): 
    total += int(key) 
 
percentage = (total*100) / 500  
 
if percentage >= 80: 
    print("A") 
elif percentage >= 60: 
    print("B") 
elif percentage >= 50: 
    print("C") 
else: 
    print("Fail") 
 
print(f"With a percentage of {percentage}%")


#5. Write a python program to fetch only Email ID from text file which include following fields -:
#         Name
#         Mobile Number
#         Roll Number
#         Email ID


import re
fileToRead = 'readText.txt'
fileToWrite = 'emailExtracted.txt'
delimiterInFile = [',', ';']
def validateEmail(strEmail):
    # .* Zero or more characters of any type. 
    if re.match("(.)@(.).(.*)", strEmail):
        return True
    return False
def writeFile(listData):
    file = open(fileToWrite, 'w+')
    strData = ""
    for item in listData:
        strData = strData+item+'\n'
    file.write(strData)
listEmail = []
file = open(fileToRead, 'r') 
listLine = file.readlines()
for itemLine in listLine:
    item =str(itemLine)
    for delimeter in delimiterInFile:
        item = item.replace(str(delimeter),' ')
    
    wordList = item.split()
    for word in wordList:
        if(validateEmail(word)):
            listEmail.append(word)
if listEmail:
    uniqEmail = set(listEmail)
    print(len(uniqEmail),"emails collected!")
    writeFile(uniqEmail)
else:
    print("No email found.")

#6. Write a function for checking the speed of drivers. This function should have one parameter: speed.
#         If speed is less than 70, it should print “Ok”.
#         Otherwise, for every 5km above the speed limit (70), it should give the driver one demerit point and print the total number of demerit points. For example, if the speed is 80, it should print: “Points: 2”.
#         If the driver gets more than 12 points, the function should print: “License suspended”

def check_velocity(velocity):
    if velocity <= 70:
        return 'Ok'
    elif velocity >= 70:
        points = (velocity - 70) // 5
        print('points = {}'.format(points))
        if points >= 12:
            return 'License suspended'
check_velocity(80)
points = 2

# 7. Write a function called show_stars(rows). If rows is 5, it should print the following:

# *
# **
# *
# **
# ***


from ast import Break


rows = int(input('Enter the number of rows: '))
for i in range(rows):
    for j in range(i):
        print('*', end=' ')
    print('')
    print('\r')


#8. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5 between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.

numbers =[]
for x in range(1500, 2701):
    if (x%7==0) and (x%5==0):
        numbers.append(str(x))
print (','.join(numbers))

#9. Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number. Suppose the following input is supplied to the program: 34,67,55,33,12,98 Then, the output should be:

# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

values=input()
l=values.split(",")
t=tuple(l)
print(l)
print(t)

#10. Write a program that calculates and prints the value according to the given formula: Q = Square root of [(2 * C * D)/H] Following are the fixed values of C and H: C is 50. H is 30. D is the variable whose values should be input to your program in a comma-separated sequence. Example Let us assume the following comma separated input sequence is given to the program: 100,150,180 The output of the program should be: 18,22,24

import math
c=50
h=30
value = []
items=[x for x in input().split(',')]
for d in items:
    value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))

print(','.join(value))

#11. Write a function to compute 5/0 and use try/except to catch the exceptions.

def attemps():
    return 5/0

try:
    attemps()
except ZeroDivisionError:
    print ("division by zero!")
except:
    print ('Caught an exception')
finally:
    print ('In finally block for cleanup')

# 12. Create a nesting list that prints out the color and the car brand?
class car:
    def _init_(self, prize, color):
        self.prize = prize
        self.color = color

class cars:
    def _init_(self, list_of_cars):
        for one_car in list_of_cars:
            assert isinstance(one_car, car) # ensure you are only given cars
        self.my_cars = list_of_cars

    @property
    def prize(self):
        return [one_car.prize for one_car in self.my_cars]

    @property
    def color(self):
        return [one_car.color for one_car in self.my_cars]


a = car('prize1', 'red')
b = car('prize2', 'green')
c = car('prize3', 'azure')
cars = cars([a,b,c])
cars.prize
['prize1', 'prize2', 'prize3']
cars.color
['red', 'green', 'azure']

# 13. Create Bonus Question: Algorithm challenge: Create your own sorting algorithm?  
l = [[5,7],[4,1],[6,9]]
l.sort(key=lambda x: (x[1], -x[0]), reverse=True)
print(l)