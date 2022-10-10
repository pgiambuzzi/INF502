# Assignment 3: Python Basics

* **INDIVIDUAL ASSIGNMENT**
* **Deadline**: Oct-11th 11:59PM
* **Value**: 100 points counted towards Homework category

**How to submit**: In your GitHub repository called *INF502* (same used for the HW assignments 1 and 2), create a file called *"Assignment3.md"* with the following content:
  1. The problem's specification (as provided below in this file);
  2. A brief textual explanation of you approach to solve the problem. Use the tag ```code``` if you need to show snippets of code along with the explanation (not required though).
  3. A link to the file with the solution. Add the `.py` file to the `code` folder (create one if you don't have it already!).
  
  Please remember to check if you invited me to see your repository (do so if you did not do for previous assignments). I will evaluate the latest commit before 11:59PM (Oct-11th)

## Problem 1: Wallets

Write a Python program that request a user to provide numbers representing the value in cash for different wallets. Your program should store these values in a list. The user should be able to add as many values as they want. One example of a filled `wallets` list (in this example, with 5 wallets) would be:

```
print(wallets)

Output: [1023, 984, 192, 1842, 12]
```

After the user adds the values for the wallets, your application should provide the following information:
* The fattest wallet has `$value` in it.
* The skinniest wallet has `$value` in it.
* All together, these wallets have `$value` in them.
* All together, the total value of these wallets is worth `$value` dimes.

Please try to think about different functions to complete your work.

## Problem 2: Periodic Table 

The Periodic Table of the Elements was developed to organize information about the elements that make up the Universe.
Write a terminal application that lets you enter information about each element in the periodic table.
Make sure you include the following information:
* symbol, name, atomic number, row, and column

You must save the elements in a dictionary where the `symbol` is the key and the other attributes are nested inside `symbol`. The nested keys are `name`, `number`, `row`, `column`.

To populate your dictionary with data, provide a menu of options to the users:

1. Search the element by symbol (see all the details).
2. Search by a property (`name`, `number`, `row`, `column`) and see the values for that property for all the elements in the table.
3. Enter a new element manually (type the information for each property)
4. Change the properties of an element (by symbol)
5. Export periodic table as a JSON file
6. Load periodic table from JSON file
7. Exit the program

Make sure you do the appropriate communication with the user to get the necessary information to complete each step.

```python

# Problem 1:

def wallet():
    values = input("Provide cash values for respective wallets (separate the values by space): ")
    wallets = values.split()
    for i in range(len(wallets)):
        wallets[i] = int(wallets[i])
    fattest = max(wallets)
    skinniest = min(wallets)
    total = sum(wallets)
    dimes = total/10
    print("The fattest wallet has", fattest, "in it.")
    print("The skinniest wallet has", skinniest, "in it.")
    print("All together, these wallets have a total of", total, "in them.")
    print("All together, the total value of these wallets is worth", dimes, "dimes.")

# Eample 1

# >>> wallet()
# Provide cash values for respective wallets (separate the values by space): >? 14 99 999 455
# The fattest wallet has 999 in it.
# The skinniest wallet has 14 in it.
# All together, these wallets have a total of 1567 in them.
# All together, the total value of these wallets is worth 156.7 dimes.

# Example 2

# wallet()
# Provide cash values for respective wallets (separate the values by space): >? 1023 984 192 1842 12
# The fattest wallet has 1842 in it.
# The skinniest wallet has 12 in it.
# All together, these wallets have a total of 4053 in them.
# All together, the total value of these wallets is worth 405.3 dimes.

# Problem 2:

#Nested dictionary
# symbol, name, atomic number, row, and column

periodic_table = {"sybmol": {"name": "", "number": "", "row": "", "column": ""}}

def print_menu():
    print("1. Search an element by symbol\n2. Search by a property\n3. Enter a new element manually\n4. Change the properties of an element\n5. Export periodic table as a JSON file\n6. Load periodic table from JSON file\n7. Exit the program")

def get_element(periodic_table, symbol):
    return periodic_table.get(symbol, -1)  #purpose of using -1 is to get the last value in the dictionary, because the -1 position of a list is technically the last value in a list.


def main():
    periodic_table = {"H": {"name": "Hydrogen", "number": 1, "row": 2, "column": 3},  "He": {"name": "Helium", "number": 4, "row": 5, "column": 6}}
    print_menu()
    option = int(input("Please select an option: "))
    while option != 7:
        if option == 1:
            symbol = input("Please type an element symbol to view an element's information: ")
            print(get_element(periodic_table, symbol))
        elif option == 2:
            prop = input("Please enter a property: ")
            if prop == "name":
                name = input("Please enter an element name: ")
                for key in periodic_table:
                    if periodic_table[key].get("name") == name:
                        print(key)
            elif prop == "number":
                number = int(input("Please type an atomic number: "))
                for key in periodic_table:
                    if periodic_table[key].get("number") == number:
                        print(key)
            elif prop == "row":
                row = int(input("Please type a row number: "))
                for key in periodic_table:
                    if periodic_table[key].get("row") == row:
                        print(key)
            elif prop == "column":
                column = int(input("Please type a column number: "))
                for key in periodic_table:
                    if periodic_table[key].get("column") == column:
                        print(key)
        elif option == 3:
            new_symbol = input("Provide a symbol for your element: ")
            new_name = input("Provide a name for your element: ")
            new_number = int(input("Provide an atomic number for your element: "))
            new_row = int(input("Provide a row number for your element: "))
            new_column = int(input("Provide a column number for your element: "))
            new_properties = {"name": new_name, "number": new_number, "row": new_row, "column": new_column}
            periodic_table.setdefault(new_symbol, new_properties)
            print(periodic_table)
        elif option == 4:
            element_change = input("Type the symbol of the element you would like to change: ")
            property_change = input("Type the property you would like to change: ")
            if property_change == "name":
                name_change = input("Type a new name: ")
                periodic_table[element_change].pop("name")
                periodic_table[element_change].update({"name": name_change})
                print(periodic_table)
            elif property_change == "number":
                number_change = int(input("Type a new atomic number: "))
                periodic_table[element_change].pop("number")
                periodic_table[element_change].update({"number": number_change})
                print(periodic_table)
            elif property_change == "row":
                row_change = int(input("Type a new row number: "))
                periodic_table[element_change].pop("row")
                periodic_table[element_change].update({"row": row_change})
                print(periodic_table)
            elif property_change == "column":
                periodic_table[element_change].pop("column")
                column_change = int(input("Type a new column number: "))
                periodic_table[element_change].update({"column": column_change})
                print(periodic_table)
            else:
                print("Please type a valid property: ")
        elif option == 5:  #exporting the periodic table as a .txt file
            file = open("periodic_table.txt", "x")
            file.write(str(periodic_table))
            file.close
        elif option == 6:
            periodic_table = {}
            new_table = input("Type the name of the file you want to upload: ")
            file = open(new_table)
            for line in file:
                key, value = line.split()
            periodic_table[key] = value
            print(a_dictionary)
        else:
            print("Error: option not available. Please select an option from the menu")
            break
        option = int(input("Please select an option: "))
    else:
        print("You have exited the program")


```
