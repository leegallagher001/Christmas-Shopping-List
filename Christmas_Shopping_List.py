# Christmas Shopping List - by Lee Gallagher

# This program creates a Christmas shopping list, allowing the user to add people, presents and prices to the list, find the most and least expensive
# presents on the list, and 

# Original version used temporary lists, but this one uses JSON

# (0) Imports & Declare Global Variables

import json

shopping_list = "christmas_shopping_list.json" # imported JSON file

numPeople = 0

# (1) Opening Statement

print(" ----- Christmas Shopping List ----- ")
print("\n")
print("Hello, and welcome to the Christmas Shopping List program!")
print("\n")

# (2) Functions and procedures

def addToList(): # Menu Option 1 - Adding Items To List

    numPeople = int(input("Enter the number of people you want to buy presents for: "))

    list_entry = {}

    for i in range(0, numPeople):

        with open (shopping_list, 'r') as f:
            list_entries = json.load(f)

            list_entry["name"] = input("Enter the name of the person: ")
            list_entry["present"] = input("What do you want to buy them?: ")
            list_entry["price"] = int(input("What is your budget?: "))
            print("\n")

            list_entries.append(list_entry)

        with open (shopping_list, 'w') as f:
            json.dump(list_entries, f, indent=4)
            

def findMostExpensive(): # Menu Option 2 - Finding Most Expensive Item List

   with open (shopping_list, 'r') as f:
       list_entries = json.load(f)

       maximum = 0
       maxCounter = ""

       for list_entry in list_entries:
           if (list_entry["price"] > maximum):
               maximum = list_entry["price"]
               maxCounter = list_entry["present"]

   print("The most expensive item on the list is the ", maxCounter, ", costing ", maximum)

def findLeastExpensive(): # Menu Option 3 - Finding Least Expensive Item On Current List

   with open (shopping_list, 'r') as f:
       list_entries = json.load(f)

       minimum = 2000000000 # an inelegant solution, but it worked (so long as one of the presents doesn't cost 2 billion!)
       minCounter = ""

       for list_entry in list_entries:
           if (minimum > list_entry["price"]):
               minimum = list_entry["price"]
               minCounter = list_entry["present"]

   print("The least expensive item on the list is the ", minCounter, ", costing ", minimum)

def findAmountOfItem(): # Menu Option 4 - Finding The Amount Of An Item On List

    with open (shopping_list, 'r') as f:
        list_entries = json.load(f)

        item_query = input("Which item are you interested in?: ")
        item_count = 0

        for list_entry in list_entries:
            if (list_entry["present"] == item_query):
                item_count +=1

    print("There are ", item_count, " ", item_query, " on your list.")


def viewList(): # Menu Option 5 - Opens Up Current List To View

    print("\n")
    print("Here is your shopping list so far:")
    print("\n")

    with open (shopping_list, 'r') as f:
        list_entries = json.load(f)

        for list_entry in list_entries:
            print("Name: ", list_entry["name"])
            print("Present: ", list_entry["present"])
            print("Price: ", list_entry["price"])
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
