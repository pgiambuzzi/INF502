def list_mangler(list_in):
    list_new = []     #creating an empty list for our outputs
    for x in list_in: #creating a for loop to run through our original list
        if x % 2 == 0:
            list_new.append(x*2) #each even number in the given list is multiplied by 2
        else:
            list_new.append(x*3) #each odd number in the given list is multiplied by 3
    print(list_new)  #and the empty list is populated with our multiplication outputs
