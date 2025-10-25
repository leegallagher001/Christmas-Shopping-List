# Christmas Shopping List - by Lee Gallagher

# This program creates a Christmas shopping list, allowing the user to add people, presents and prices to the list, find the most and least expensive
# presents on the list, and 

# (0) Declare Global variables

numPeople = 0
names = []
presents = []
prices = []

# (1) Opening Statement

print(" ----- Christmas Shopping List ----- ")
print("\n")
print("Hello, and welcome to the Christmas Shopping List program!")
print("\n")

# (2) Functions and procedures

def addToList(): # Menu Option 1 - Adding Items To List

    numPeople = int(input("Enter the number of people you want to buy presents for: "))

    for i in range(0, numPeople):
        name = input("Enter the name of the person: ")
        names.append(name)
        present = input("What do you want to buy them?: ")
        presents.append(present)
        price = int(input("What is your budget?: "))
        prices.append(price)
        print("\n")

def findMostExpensive(): # Menu Option 2 - Finding Most Expensive Item List

    maximum = prices[0]
    maxCounter = 0

    for index in range(0, len(prices)):
        if (prices[index] > maximum):
            maximum = prices[index]
            maxCounter = presents[index]
    print("The most expensive item was the " , maxCounter, ", costing ", maximum)

def findLeastExpensive(): # Menu Option 3 - Finding Least Expensive Item On Current List

    minimum = prices[0]
    minCounter = 0

    for index in range(0, len(prices)):
        if (minimum > prices[index]):
            minimum = prices[index]
            minCounter = presents[index]
    print("The least expensive item was the ", minCounter, ", costing ", minimum)

def findAmountOfItem(): # Menu Option 4 - Finding The Amount Of An Item On List

    item_query = input("Which item are you interested in?: ")
    item_count = 0

    for index in range(0, len(presents)):
        if (presents[index] == item_query):
            item_count +=1
    print("There are ", item_count, " ", item_query, " on your list.")


def viewList(): # Menu Option 5 - Opens Up Current List To View

    print("\n")
    print("Here is your shopping list so far:")
    print("\n")

    for index in range(0, len(names)):
        print("Name: ", names[index])
        print("Present: ", presents[index])
        print("Price: ", prices[index])
        print("\n")

# (3) Main Menu

print("Shopping List Main Menu")
print("\n")
print("1. Add People To Shopping List")
print("2. Find Most Expensive Item On List")
print("3. Find Least Expensive Item On List")
print("4. Find Amount Of Item On List")
print("5. View List")
print("6. Exit List Program")
print("\n")

# (4) Activate Functions

menuChoice = int(input("Choose An Option: "))

while menuChoice != 6:

    if menuChoice == 1:
        addToList()
        print("\n")
        menuChoice = int(input("Ready For Something Else? Choose Another Option: "))

    elif menuChoice == 2:
        findMostExpensive()
        print("\n")
        menuChoice = int(input("Ready For Something Else? Choose Another Option: "))

    elif menuChoice == 3:
        findLeastExpensive()
        print("\n")
        menuChoice = int(input("Ready For Something Else? Choose Another Option: "))

    elif menuChoice == 4:
        findAmountOfItem()
        print("\n")
        menuChoice = int(input("Ready For Something Else? Choose Another Option: "))

    elif menuChoice == 5:
        viewList()
        print("\n")
        menuChoice = int(input("Ready For Something Else? Choose Another Option: "))

    else:
        print("Menu Option Not Recognised. Please Try Again.")
        print("\n")
        menuChoice = int(input("Ready For Something Else? Choose Another Option: "))

# (5) Closing Remarks, End Of Program

print("\n")
print("I hope you enjoyed the Christmas Shopping List Program! Happy Xmas On Dec 25th!")
print("\n")
input("Press 'ENTER' to exit the program.")
exit()
