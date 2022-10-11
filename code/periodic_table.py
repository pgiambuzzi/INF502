def print_menu():
    print("1. Search an element by symbol\n2. Search by a property\n3. Enter a new element manually\n4. Change the properties of an element\n5. Export periodic table as a JSON file\n6. Load periodic table from JSON file\n7. Exit the program")

def get_element(periodic_table, symbol):
    return periodic_table.get(symbol, -1)  #purpose of using -1 is to get the last value in the dictionary, because the -1 position of a list is technically the last value in a list.

def main():
    periodic_table = {}
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
            file_name = input("Type a name for your file: ")
            file = open(file_name, "w")
            file.write(str(periodic_table))
            file.close()
        elif option == 6:
            new_table = input("Type the name of the file you want to upload: ")
            file = open(new_table, "r")
            periodic_table = eval(file.read())
            print(periodic_table)
            file.close()
        else:
            print("Error: option not available. Please select an option from the menu")
            break
        option = int(input("Please select an option: "))
    else:
        print("You have exited the program")
     
main()
