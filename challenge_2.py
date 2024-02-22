# Accept user input to create a list of integers
num_list = []
n = int(input("Enter the number of integers you want to add to the list: "))
for i in range(n):
    num = int(input("Enter an integer: "))
    num_list.append(num)

# Compute the sum of all the integers in the list
sumOfList = 0
for num in num_list:
    sumOfList = sumOfList + num

# Print the sum of all the integers in the list
print("The sum of all the integers in the list is:", sumOfList)

# Create a tuple containing the names of five of your favorite books.
# Then, use a for loop to print each book name on a separate line.
favoriteBooks = ("The theory of everything", "Think like a fool", "Java mastery", "Python for dummies", "Planet earth")
for book in favoriteBooks:
    print(book)


# Take user input, add it to a dictionary and print the dictionary
name = input("Enter your name: ")
age = input("Enter your age: ")
favoriteColor = input("Enter your favorite color: ")
person = {'name': name, 'age': age, 'favoriteColor': favoriteColor}
print(person)


# Take user inputs to create two sets and print values that are common in both
firstSet = set()
j = int(input("How many values for the first set?"))
for k in range(j):
    num = int(input("Enter an integer: "))
    firstSet.add(num)

secondSet = set()
j = int(input("How many values for the second set?"))
for k in range(j):
    num = int(input("Enter an integer: "))
    secondSet.add(num)
common = firstSet.intersection(secondSet)
print("Common values in both sets {} ".format(common))


# Create a program that stores a list of words.
# Create a new list that contains only the words that have an odd number of characters.
words = ["words", "banana", "Hello", "Hi", "anaesthetics", "world", "eye", "done"]
odd_length_words = [word for word in words if len(word) % 2 != 0]
print("A list of words with an odd number of characters: {}".format(odd_length_words))



