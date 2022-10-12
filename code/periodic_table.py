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
        print("You have exited the program")  # if the user types 7, they will get this message and the program will be closes. To re-open, they will have to type main() again. This will refresh the dictionary to an empty dictionary.

main()
