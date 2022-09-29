# 1.  Your task is to create slightly different animals, which should have the same properties and methods, but should implement the talk() method in different ways. For example. should a cat (when talking) say "Moew", a dog "Woff", a fish "Blub" and a Cow "Muuu". They should all share the following (private) properties: name (string), age (number), food (list of strings), and have the functions get_name, set_name, get_age, set_age, get_food, add_food, remove_food. Finally, all the animals must have the talk function, but that function must, as I said, be implemented in each animal, as the animals have different sounds.
# When you have made the classes, create instances of the classes and put in a list - loop through the list - and let all the animals talk! :)
class Animal():
    def __init__(self, name: str, age: int, food: list):
        self.name = name
        self.age = age
        self.food = food
    
    def get_name(self):
        return f"The animal is a {self.name}."

    def set_name(self, name):
        self.name = name
        return f"The goat has a name {self.name}"

    def get_age(self):
        return f"This animal is {self.age} years old."

    def set_age(self, new_age):
        self.age = new_age
        return f"The above animal has an age of {new_age}."

    def get_food(self):
        return f"The animal {self.name} feeds on {self.food}"

    def add_food(self, food):
        food = self.food.append(food)
        return f"The new diet is {self.food}."

    def remove_food(self, food):
        food = self.food.remove(food)
        return f"The new diet is {self.food}"

class Cat(Animal):
    def __init__(self, name, age, food, talk):
        super().__init__(name, age, food)
        self.talk = talk

    def talk(self):
        return f"Meow"

class Dog(Animal):
    def __init__(self, name, age, food, talk):
        super().__init__(name, age, food)
        self.talk = talk

    def talk(self):
        return f"Woff"

class Fish(Animal):
    def __init__(self, name, age, food, talk):
        super().__init__(name, age, food)
        self.talk = talk

    def talk(self):
        return f"Blub"

class Cow(Animal):
    def __init__(self, name, age, food, talk):
        super().__init__(name, age, food)
        self.talk = talk

    def talk(self):
        return f"Muu"

animal = Animal("Goat", "8", ["Grass", "plantain", "Starch"])
print(animal.get_name())
print(animal.set_name('Eobard'))
print(animal.get_age())
print(animal.set_age(8))
print(animal.get_food())
print(animal.add_food('leaves'))
print(animal.remove_food('Starch'))

cat = Cat("Snow", 6, ['meat', 'milk'], "Meow")
dog = Dog("Scooby", 10, ['meat', 'milk'], "Woof")
fish = Fish("Fluufy", 2, ['weed'], "Blub")
cow = Cow("Ron", 4, ['grass', 'feed mix'], "Muu")






#2 The snail climbs up 7 feet each day and slips back 2 feet each night. 
# How many days will it take the snail to get out of a well with the given depth?. 
# Using python, write a function to solve this problem. Sample Input: 31 Sample Output: 6


# Day 1: 7-2=5
# Day 2: 5+7-2=10
# Day 3: 10+7-2=15
# Day 4: 15+7-2=20
# Day 5: 20+7-2=25
# Day 6: 25+7=32 
# So, on Day 6 the snail will reach 32 feet and get out of the well at day, without slipping back that night.

well_height = 31

daily_distance = 7

nightly_distance = 2

snail_position = 0
days = 0

while snail_position < well_height:
   days += 1
   snail_position += daily_distance - nightly_distance
print(days)




#3 Write a function that takes a list of numbers and returns the largest number in the list.

def max_num(nums):
    return max(nums)

#4 Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters. Suppose the following input is supplied to the program: Hello world! Then, the output should be: UPPER CASE 1 LOWER CASE 9

def upper_lower_counter(sentence):
    upper = 0
    lower = 0
    for x in sentence:
        if x.isupper():
            upper += 1
        elif x.islower():
            lower += 1

    return "UPPER CASE " + str(upper) + "LOWER CASE " +str(lower)

#5 Using Object Oriented Programming, write a program that implements a dice game. The game should have two players, and each player should have a name and a score. The game should have a method called play that takes two players as arguments and simulates the game. The game should be played as follows:

# Each player rolls a die.
# The player with the highest roll wins the round.
# The winner gets one point added to their score.
# The game ends when one player has 5 points.
# The player with the most points at the end of the game wins.
# The program should print out the winner's name and score.
# If a player rolls a 6, they get an extra roll. If they roll a 6 again, they get another extra roll. If they roll a 6 a third time, they get an extra roll, but their turn ends.            

def __init__(self, name, score):
    self.name = name
    self.score = score

def play(self, player1, player2):
    while player1.score < 5 and player2.score < 5:
        player1_roll = player1.roll()
        player2_roll = player2.roll()
        if player1_roll > player2_roll:
            player1.score += 1
            print(f"{player1.name} wins the round!")
        elif player2_roll> player1_roll:
            player2.score += 1
            print (f"{player2.name} wins the round !")
        else:
            print("It's a tie!")
    if player1.score > player2.score:
        print(f"{player1.name} wins the game!")
    else:
        print(f"{player2.name} wins the game!")

def roll(self):
    import random
    roll = random.randint(1,6)
    print(f"{self.name} rolled a {roll}")
    if roll == 6:
        roll += self.roll()
    return roll

#6 Write a Python program that lists out all the default as well as custom properties of the class

class Footballer:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

footballer_10 = Footballer("Christiano", 37, 6.5)

print(dir(Footballer))

#7 Write a Program in Python to implement a Stack Data Structure using Class and Objects, with push, pop, and traversal methods.

class Stack:
    def __init__(self):
        self.stack = list()

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, data):
        self.stack.append(data)

    def peek(self):
        return self.stack[-1]

    def pop(self):
        if self.isEmpty():
            return ("Stack is empty!")
        return self.stack.pop()

    def size(self):
        return len(self.stack)

    def show(self):
        return self.stack

#8 Using list comprehension, write a program that takes a list of numbers and returns a list of the squares of the numbers.

print ([i**2 for i in range(2,5)])    

#9 Using only functions and lists, Implement a queue data structure. The queue should have the following methods: enqueue, dequeue, and size. The queue should be "first-in-first-out" (FIFO).

list_1 = list()
maximum = 5

def isEmpty():
    return len(list_1) == 0    


def isFull():
    return len(list_1) == maximum

def enqueue(element):
    if not isFull():
        list_1.insert(0,element)
        return list_1
    else:
        return 'list is already full'


def dequeue():
    if not isEmpty():
        list_1.pop()
        return list_1

    else:
        return 'yo the list is already empty'

def display(f):
    print(f)

display(enqueue(6))
display(enqueue(7))
display(enqueue(8))
display(enqueue(9))
display(enqueue(10))
display(isFull())
display(enqueue(1))
display(dequeue())
display(dequeue())
display(dequeue())
display(dequeue())
display(dequeue())
display(isEmpty())
display(dequeue())


#10 Using a while loop, implement merge sort algorithm.

def mergeSort(array):
    if len(array) > 1:

        midPoint = len(array)//2
        leftArray = array[:midPoint]
        rightArray = array[midPoint:]

        mergeSort(leftArray)
        mergeSort(rightArray)

        x = 0
        y = 0
        z = 0

        while x < len(leftArray) and y < len(rightArray):
            if leftArray[x] < rightArray[y]:
                array[z] = leftArray[x]
                x += 1
            else:
                array[z] = rightArray[y]
                y += 1
            z += 1

        
        while x < len(leftArray):
            array[z] = leftArray[x]
            x += 1
            z += 1

        while y < len(rightArray):
            array[z] = rightArray[y]
            y += 1
            z += 1


def printSortedArray(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()


if __name__ == '__main__':
    numbers = [4, 10, 6, 14, 2, 1, 8, 5]

    mergeSort(numbers)