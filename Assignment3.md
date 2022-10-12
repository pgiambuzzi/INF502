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


link to code for Problem 1: [wallet.py](https://github.com/pgiambuzzi/INF502/blob/main/code/wallet.py)

link to code for Problem 2: [periodic_table.py](https://github.com/pgiambuzzi/INF502/blob/main/code/periodic_table.py)


```python

# Problem 1:

# Approach explanation: the string values that the user inputs into the wallet can be turned into a list using .string
# which allows us to index the list and calculate maximums and minimums (and do other mathematical procedures).
# After the input strings are turned into integers, we can use the simple max(), min(), and Sum() functions to find the
# fattest and skinniest wallets, as well as the total and amount in dimes (by dividing total by 10).

def wallet():
    values = input("Provide cash values for respective wallets (separate the values by space): ")  # input values must be separated by space for .split to work
    wallets = values.split()  # puts input strings into a list
    for i in range(len(wallets)):
        wallets[i] = int(wallets[i])  # turns each member of the list into an integer
    fattest = max(wallets)  # calculates the highest wallet value
    skinniest = min(wallets)  # calculates the lowest wallet value
    total = sum(wallets)  # adds every wallet value together to get the total
    dimes = total/10  # divides the total by 10 to see how many dimes the total value is worth
    print("The fattest wallet has", fattest, "in it.")  # in the following lines, the object that we saved the result to for respective mathematical operations is printed with an explanation for concisions's sake
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

# Approach explanation: To make the main function a bit more concise, I created a function that prints the menu and one
# that gets the symbol key of the dictionary outside the main function. They then appear alone in the main function for
# more a more concise looking main function. The while loop was used so that each time the user is done with an option,
# the program will again prompt them with "Select an option" until they choose to exit the program. I separated the
# if/elif/else arguments by option number. Throughout the function, each user input is assigned to a variable, and those
# variables are used to see which property or element is being referenced.

def print_menu():  #prints the options to be selected in the program
    print("1. Search an element by symbol\n2. Search by a property\n3. Enter a new element manually\n4. Change the properties of an element\n5. Export periodic table as a JSON file\n6. Load periodic table from JSON file\n7. Exit the program")

def get_element(periodic_table, symbol):  # retrieves the key and values for the corresponding input given
    return periodic_table.get(symbol, -1)  #purpose of using -1 is to get the last value in the dictionary, because the -1 position of a list is technically the last value in a list.

def main():
    periodic_table = {}  # creates an empty dictionary which we will populate uaing the options from the menu
    print_menu()
    while True: #creates an infinite loop
        try:
            option = int(input("Please select an option: "))  # converts the input into an integer
            break  # stops the infinite loop if option is entered correctly
        except ValueError:  # directs the ValueError to print a specific message if the input is a string
            print("Error: Please provide an integer from 1 to 7, no strings allowed.")
    while option != 7:
        if option == 1:
            symbol = input("Please type an element symbol to view an element's information: ")
            print(get_element(periodic_table, symbol))  # will return the values corresponding to the key given by the user
            if symbol not in periodic_table:
                print("Not available. Try again.")  # will tell the user if the symbol they typed is not in the periodic table and will prompt them to start over
        elif option == 2:
            prop = input("Please enter a property: ")
            if prop == "name":
                for key in periodic_table:
                    print(periodic_table[key].get("name"))  # prints the value corresponding to the name value for the element provided
            elif prop == "number":
                for key in periodic_table:
                    print(periodic_table[key].get("number"))  # prints the value corresponding to the number value for the element provided
            elif prop == "row":
                for key in periodic_table:
                    print(periodic_table[key].get("row"))  # prints the value corresponding to the row value for the element provided
            elif prop == "column":
                for key in periodic_table:
                    print(periodic_table[key].get("column"))  # prints the value corresponding to the column value for the element provided
            else:
                print("Not available. Try again.")  # will tell the user if the property they typed is not valid and will prompt them to start over
        elif option == 3:  # this will ask the user for all the info the program will need to create a new, complete dictionary entry
            new_symbol = input("Provide a symbol for your element: ")
            new_name = input("Provide a name for your element: ")
            new_number = int(input("Provide an atomic number for your element: "))
            new_row = int(input("Provide a row number for your element: "))
            new_column = int(input("Provide a column number for your element: "))
            new_properties = {"name": new_name, "number": new_number, "row": new_row, "column": new_column}  # the user input values are assigned to the corresponding keys of a new entry
            periodic_table.setdefault(new_symbol, new_properties)  # this will create a new dictionary entry using the properties given above
            print(periodic_table)
        elif option == 4:
            element_change = input("Type the symbol of the element you would like to change: ")
            property_change = input("Type the property you would like to change: ")
            if property_change == "name":
                name_change = input("Type a new name: ")
                periodic_table[element_change].pop("name")  # .pop will remove the existing name of the element
                periodic_table[element_change].update({"name": name_change})  # the removed name is then replaced with the user input
                print(periodic_table)
            elif property_change == "number":
                number_change = int(input("Type a new atomic number: "))
                periodic_table[element_change].pop("number")  # .pop will remove the existing number of the element
                periodic_table[element_change].update({"number": number_change})  # the removed number is then replaced with the user input
                print(periodic_table)
            elif property_change == "row":
                row_change = int(input("Type a new row number: "))
                periodic_table[element_change].pop("row")  # .pop will remove the existing row of the element
                periodic_table[element_change].update({"row": row_change})  # the removed row is then replaced with the user input
                print(periodic_table)
            elif property_change == "column":
                column_change = int(input("Type a new column number: "))
                periodic_table[element_change].pop("column")  # .pop will remove the existing column of the element
                periodic_table[element_change].update({"column": column_change})  # the removed column is then replaced with the user input
                print(periodic_table)
            else:
                print("Not available. Try again.")  # will tell the user if the property they typed is not valid and will prompt them to start over
        elif option == 5:  # exporting the periodic table as a .json file
            file_name = input("Type a name for your file: ")  # user names the file without .json written
            file_json = file_name + ".json"  # adds .json to the end of the file name provided by the user
            file = open(file_json, "w")  # opens a new file with the given name with permission to write
            file.write(str(periodic_table))  # write the file as a string of the periodic table dictionary
            file.close()  # closes the file so it can be stored while still in the program
        elif option == 6:  # importing a periodic table as a .json file
            new_table = input("Type the name of the file you want to upload: ")  # user gives the name of the file in their library without writing .json
            new_json = new_table + ".json"  # adds .json to the end of the file name provided by the user
            file = open(new_json, "r")  # opens the existing file with the given name with permission to read
            periodic_table = eval(file.read())  #  using eval() to turn the file from a string into a dictionary while reading
            print(periodic_table)
            file.close()  # closes the file so it can be stored while still in the program
        else:
            print("Error: option not available. Please select an option from the menu")  # if the option typed by the user is an integer not equal to 1, 2, 3, 4, 5, 6, or 7, it will tell the user the option is not valid
            break  # stops the error message from repeating infinitely
        option = int(input("Please select an option: "))  # queries the user to select an option again after each time they complete an option. This will keep happening unitl the user presses 7 to exit.
    else:
        print("You have exited the program")  # if the user types 7, they will get this message and the program will be closes. To re-open, they will have to type 
        
main()

# Example:

# >>> main()
# 1. Search an element by symbol
# 2. Search by a property
# 3. Enter a new element manually
# 4. Change the properties of an element
# 5. Export periodic table as a JSON file
# 6. Load periodic table from JSON file
# 7. Exit the program
# Please select an option: >? 6
# Type the name of the file you want to upload: >? chgahg
# {'C': {'name': 'Carbon', 'number': 1, 'row': 2, 'column': 3}, 'H': {'name': 'Hydrogen', 'number': 4, 'row': 5, 'column': 6}, 'Ga': {'name': 'Gallium', 'number': 1, 'row': 2, 'column': 3}, 'Hg': {'name': 'Mercury', 'number': 4, 'row': 5, 'column': 6}}
# Please select an option: >? 1
# Please type an element symbol to view an element's information: >? C
# {'name': 'Carbon', 'number': 1, 'row': 2, 'column': 3}
# Please select an option: >? 2
# Please enter a property: >? name
# Carbon
# Hydrogen
# Gallium
# Mercury
# Please select an option: >? 3
# Provide a symbol for your element: >? Xe
# Provide a name for your element: >? Xenon
# Provide an atomic number for your element: >? 45
# Provide a row number for your element: >? 23
# Provide a column number for your element: >? 12
# {'C': {'name': 'Carbon', 'number': 1, 'row': 2, 'column': 3}, 'H': {'name': 'Hydrogen', 'number': 4, 'row': 5, 'column': 6}, 'Ga': {'name': 'Gallium', 'number': 1, 'row': 2, 'column': 3}, 'Hg': {'name': 'Mercury', 'number': 4, 'row': 5, 'column': 6}, 'Xe': {'name': 'Xenon', 'number': 45, 'row': 23, 'column': 12}}
# Please select an option: >? 4
# Type the symbol of the element you would like to change: >? Xe
# Type the property you would like to change: >? number
# Type a new atomic number: >? 42
# {'C': {'name': 'Carbon', 'number': 1, 'row': 2, 'column': 3}, 'H': {'name': 'Hydrogen', 'number': 4, 'row': 5, 'column': 6}, 'Ga': {'name': 'Gallium', 'number': 1, 'row': 2, 'column': 3}, 'Hg': {'name': 'Mercury', 'number': 4, 'row': 5, 'column': 6}, 'Xe': {'name': 'Xenon', 'row': 23, 'column': 12, 'number': 42}}
# Please select an option: >? 5
# Type a name for your file: >? chgahgxe
# Please select an option: >? 6
# Type the name of the file you want to upload: >? chgahgxe
# {'C': {'name': 'Carbon', 'number': 1, 'row': 2, 'column': 3}, 'H': {'name': 'Hydrogen', 'number': 4, 'row': 5, 'column': 6}, 'Ga': {'name': 'Gallium', 'number': 1, 'row': 2, 'column': 3}, 'Hg': {'name': 'Mercury', 'number': 4, 'row': 5, 'column': 6}, 'Xe': {'name': 'Xenon', 'row': 23, 'column': 12, 'number': 42}}
# Please select an option: >? 7
# You have exited the program

```
