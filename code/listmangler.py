def list_mangler(list_in):
    #creating an empty list for our outputs
    list_new = []
    #creating a for loop to run through our original list
    for x in list_in:
    #each even number in the given list is multiplied by 2
        if x % 2 == 0:
            list_new.append(x*2)
    #each odd number in the given list is multiplied by 3
        else:
            list_new.append(x*3)
    #and the empty list is populated with our multiplication outputs
    print(list_new)
