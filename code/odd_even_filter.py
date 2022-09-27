def odd_even_filter(numbers):
    list_odd = [] #empty list for off numbers to go into
    list_even = [] #empty list for even numbers to go into
    for x in numbers: #for loop selects and adds even numbers to the empty list_even
        if x % 2 == 0:
            list_even.append(x)
        else:
            list_odd.append(x) #then selects and adds odd numbers to the empty list_odd
    print(list_even, list_odd) #then we print the two new lists side by side
