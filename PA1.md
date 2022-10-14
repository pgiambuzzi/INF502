Explantion and Hurdles:
I first created a function that takes a user sequence file and puts it into a list, a function that calculates the
max number of matches based on the shift number provided by the user, and a function that does the same but for
calculating the max chain.  All of these functions were then put into a main function for more concise code.
One of the hurdles I had to overcome had to do with understanding the concept of lists. Once I realized that it is
possible to index lists rather than trying to select a nucleotide from a string, it became much easier to figure out
how to tell the user which shift resulted in the maximum chain or score. I realized that each result from a for loop
could be added to a list, and then that list could be indexed. Another chanallange was getting the syntax of the for
loops correct. Having if-else statements inside of for loops meant I had to be precise about where I put the commands
that would yield a result, like a print() or .append command. It also took time to think of as many exceptions as I
could. Syntax overall was a big hurdle.  When doing exception handling, I had to make sure that the variables the
exceptions were referring to were defined, and that the exceptions occurred in the appropriate order.

```python

# Random DNA Sequence Generator that writes the new sequence to a file:
# (This was not required for the project)

from random import choice

def random_sequence(length):
    nucleotides = ["A", "C", "G", "T"]
    sequence = ""
    sequence_file = input("Type a name for your new file: ") + ".txt"
    file = open(sequence_file, "x")
    for i in range(length):
        nucleotide = choice(nucleotides)
        sequence += nucleotide
    file.write(sequence)

# TA-DA! This allows us to put .txt files containing random DNA sequences into our working directory.

# Reading in files and changing to a list that we can edit rather than editting the original file:
def sequence1_to_list(file_1):  # the list created from this function will be used to add shifts to the sequence
    sequence_1_list = []  # creating an empty list which our comma-separated sequence will be put into
    sequence_1 = open(file_1, 'r')  # openning the file, which the user will be asked to input the name of later in our main() function
    sequence_1_read = sequence_1.read()  # reads the file into python
    sequence_1.close  # closes the file since we have read it in
    for x in range(len(sequence_1_read)):
        sequence_1_list.append(sequence_1_read[x])  # adding each nucleotide from the sequence file into our empty list
    return sequence_1_list

def sequence2_to_list(file_2):  # this function follows the same procedure as the previous one but for a second sequence file to be compared to the first
    sequence_2_list = []
    sequence_2 = open(file_2, "r")
    sequence_2_read = sequence_2.read()
    sequence_2.close
    for x in range(len(sequence_2_read)):
        sequence_2_list.append(sequence_2_read[x])
    return sequence_2_list

#The following function takes two sequence files that the user has provided, puts the score of each shift into a list, and then selects the maximum score from the list.
#This function then indexes this list of scores and spits out the number of shifts that yields the highest score.
#This function is also able to select 0 shifts as the optimal shift if that is the case.
def max_score():
    global shift  # avoids us running into an UnboundLocalError when shift is defined
    try:  #exception handling
        shift = int(input("Set the maximum number of base pair shifts: "))  # asks the user for the max number of shifts allowed, but we have to ensure python reads the input as an integer rather than a string
    except ValueError:  # a ValueError would typically be raised if the input for this were a string, float, or other non-integer type
        print("Invalid input type. Please try again and input an integer.")  # So when this Value error is raised, the program prints this message
        return
    if shift < 0:
        print("Negative values cannot be accepted for 'shift'. Please supply a positive integer.")
        return
    global list_1, list_2  # avoids us running into an UnboundLocalError when list_1 and list_2 are defined
    file_1 = input("Type the file name of your first sequence: ") + ".txt"  # asks the user for the name of the first sequence file they would like to use
    file_2 = input("Type the file name of your second sequence: ") + ".txt"  # asks the user for the name of the second sequence file they would like to use
    try:  # making an error exception for if the file name typed by the user does not exist or does not match a file in the user's library
        list_1 = sequence1_to_list(file_1)  # loading the user input file for sequence 1 into a list
        list_2 = sequence2_to_list(file_2)  # loading the user input file for sequence 2 into a list
    except FileNotFoundError:
        print("File not found. Try again.")  # if the file typed by the user does not match any existing files, this message will pop up
        return
    if len(list_1) != len(list_2): #  if the the two sequences provided are not of the same length, they should not be compared and this message will appear
        print("Error: the sequences being compared must have the same number of nucleotides (same length). Try again.")
        return
    if shift >= len(list_1):  # rejects a shift input equal to or greater than the number of nucleotides in a given sequence because otherwise there will be no nucleotides lining up between sequences to compare
        print("Number of shifts cannot equal or exceed the number of nucleotides in the sequence.")
    elif shift > 0: #when a number of shifts is provided, the following loop is run
        max_list = []  # creating an empty list in which the score for each shift will be entered
        score = 0 #setting the initial score to 0, before any matches are calculated
        for x in range(len(list_1)): #calculating the number of base pair matches for ZERO shifts
            if list_1[x] == list_2[x]:
                score += 1 #adds one point to the score for each base pair match between sequences
        max_list.append(score) #adds the score for ZERO shifts to an empty list which will soon be populated with more scores corresponding to subsequent shifts
        for x in range(1, shift + 1): #adding a dash to the sequence for each number from 1 to the value entered for shift argument
            list_1.insert(0, "-") #dashes are added at the beginning for sequence 1
            list_2.append("-") #dashes are added at the end for sequence 2
            score = 0 #setting the score back to 0 in preparation for the matches to be calculated following subsequent shifts
            for x in range(1, len(list_1)):
                if list_1[x] == list_2[x]: #pairs each element in the sequence list (nucleotides) and recognizes if there is a match
                    score += 1 #one point is added for each match between the two sequences
            max_list.append(score) #the matching score for each shift is saved to a list
        print("Max score:", max(max_list)) #from the list of scores for each shift, the highest score is printed
        index = max_list.index(max(max_list)) #selecting the index of the highest score, which corresponds to the number of shifts that resulted in the highest score
        print("Optimal shift:", index) #do not need to add 1 to the index number since the first element in the list corresponds to zero shifts and is at position zero
        to_remove = shift - index #calculates the difference between the max number of shifts requested and the optimal shift
        for x in range(1, to_remove+1): #this will return the DNA sequences with the optimal number of shifts rather than with the max number of shifts requested in the 'shift' argument of the function. +1 is needed here since we have to account for 0 shifts
            list_1.remove("-")
            list_2.remove("-")
        print(''.join(list_1)) #removing commas from each sequence and putting the lists into a string for easier visibility of the base pair matches
        print(''.join(list_2))
    elif shift == 0: #this calculates the score when no sequence shifts are requested, following the same procedure as before
        score = 0
        for x in range(len(list_1)):
            if list_1[x] == list_2[x]:
                score += 1
        print("Score:", score) #prints the score alone as a result of zero shifts
        print(''.join(list_1)) #removing commas from each sequence and putting the lists into a string for easier visibility of the base pair matches
        print(''.join(list_2))
    else: #tells the user that negative numbers cannot be supplied for the shift
        print("Negative values cannot be accepted for 'shift'. Please supply a positive integer.")


# The following function puts the chains of matching nucleotides into a list for each number of shifts
# It then calculates the max chain resulting from each shift
# The function then selects the highest maximum that have resulted from each shift up to the shift number requested
# The function then indexes that highest maximum from the list, and spits out the number of shifts that yielded that highest maximum
def max_chain():
    global shift  # avoids us running into an UnboundLocalError when shift is defined
    try:  # see exception handling explanations above^. same process followed here.
        shift = int(input("Set the maximum number of base pair shifts: "))  # asks the user for the max number of shifts allowed, but we have to ensure python reads the input as an integer rather than a string
    except ValueError:
        print("Invalid input type. Please try again and input an integer.")
        return
    if shift < 0:
        print("Negative values cannot be accepted for 'shift'. Please supply a positive integer.")
        return
    global list_1, list_2  # avoids us running into an UnboundLocalError when list_1 and list_2 are defined
    file_1 = input("Type the file name of your first sequence: ") + ".txt"  # asks the user for the name of the first sequence file they would like to use
    file_2 = input("Type the file name of your second sequence: ") + ".txt"  # asks the user for the name of the second sequence file they would like to use
    try:  # making an error exception for if the file name typed by the user does not exist or does not match a file in the user's library
        list_1 = sequence1_to_list(file_1)  # loading the user input file for sequence 1 into a list
        list_2 = sequence2_to_list(file_2)  # loading the user input file for sequence 2 into a list
    except FileNotFoundError:
        print("File not found. Try again.")  # if the file typed does not match any existing files, this message will pop up
        return
    list_1 = sequence1_to_list(file_1)  # loading the user input file for sequence 1 into a list
    list_2 = sequence2_to_list(file_2)  # loading the user input file for sequence 2 into a list
    if len(list_1) != len(list_2):  # if the the two sequences provided are not of the same length, they should not be compared and this message will appear
        print("Error: the sequences being compared must have the same number of nucleotides (same length). Try again.")
        return
    if shift >= len(list_1):  # rejects a shift input equal to or greater than the number of nucleotides in a given sequence because otherwise there will be no nucleotides lining up between sequences to compare
        print("Number of shifts cannot equal or exceed the number of nucleotides in the sequence.")
    elif shift > 0:  # when a number of shifts is provided, the following loop is run
        chains_list = []  # creating an empty list in which chains created for a single shift (or no shift) will be entered
        max_chains = []  # creating a list that will store the max chain generated from each list
        score = 0  # setting the initial score to 0, before any matches are calculated
        for x in range(len(list_1)):  # calculating the number of chain values for ZERO shifts
            if list_1[x] == list_2[x]:  # pairs each element in the sequence list (nucleotides) and recognizes if there is a match
                score += 1  # adds one point to the chain value for each base pair match between sequences
                chains_list.append(score)  # adds the chain values to a list that will store all the chains resulting from a shift
            else:
                score=0  # if the loop runs into a pair of nucleotides that DO NOT match, the score is RESET to zero
        max_chains.append(max(chains_list))  # adds the maximum chain obtained for ZERO shifts to an empty list which will soon be populated with more maximum chains corresponding to subsequent shifts
        for x in range(1, shift + 1):  # adding a dash to the sequence for each number from 1 to the value entered for shift argument
            list_1.insert(0, "-")  # dashes are added at the beginning for sequence 1
            list_2.append("-")  # dashes are added at the end for sequence 2
            score = 0  # setting the score back to 0 in preparation for the matches to be calculated following subsequent shifts
            for x in range(1, len(list_1)):
                if list_1[x] == list_2[x]:  # pairs each element in the sequence list (nucleotides) and recognizes if there is a match
                    score += 1  # one point is added for each contiguous match between the two sequences
                    chains_list.append(score)  # adds the chain values to a list that will store all the chains resulting from a shift
                else:
                    score = 0  # if the loop runs into a pair of nucleotides that DO NOT match, the score is RESET to zero
            max_chains.append(max(chains_list))  # the chain value for each shift is saved to a list
        print("Max chain:", max(max_chains))  # from the list of chains for each shift, the maximum chain is selected
        index = max_chains.index(max(max_chains))  # selecting the index of the highest chain, which corresponds to the number of shifts that resulted in the highest chain
        print("Optimal shift:", index)  # do not need to add 1 to the index number since the first element in the list corresponds to zero shifts and is at position zero
        to_remove = shift - index  # calculates the difference between the max number of shifts requested and the optimal shift
        for x in range(1, to_remove + 1):  # this will return the DNA sequences with the optimal number of shifts rather than with the max number of shifts requested in the 'shift' argument of the function. +1 is needed here since we have to account for 0 shifts
            list_1.remove("-")
            list_2.remove("-")
        print(''.join(list_1))  # removing commas from each sequence and putting the lists into a string for easier visibility of the base pair matches
        print(''.join(list_2))
    elif shift == 0:  # this calculates the max chain when no sequence shifts are requested, following the same procedure as before
        score = 0
        for x in range(len(list_1)):
            if list_1[x] == list_2[x]:
                score += 1
                chains_list.append(score)
            else:
                score = 0
        print("Max chain:", max(chains_list))  # prints the max chain alone as a result of zero shifts
        print(''.join(list_1))  # removing commas from each sequence and putting the lists into a string for easier visibility of the base pair matches
        print(''.join(list_2))

# Main function that queries the user for their sequence file names, approach, and number of shifts.
# depending on the input for approach, the function will either calculate the max score or max chain
def main():
    try:
        approach = int(input("Would you like to calculate the max score (1) or max chain (2)?: "))  # asks the user to select whether they want to calculate the max score or the max chain from the sequences they have provided. Again, me must convert the user's input to an integer
    except ValueError:
        print("Invalid input type. Please try again and input an integer.")
        return
    if approach == 1:
        max_score()
    elif approach == 2:
        max_chain()
    else:
        print("Please provide a valid approach (input 1 or 2).")
        return

main()


# Example 1:

# >>> main()
# Type the file name of your first sequence: >? sequence_1
# Type the file name of your second sequence: >? sequence_2
# Set the maximum number of base pair shifts: >? 15
# Would you like to calculate the max score (1) or max chain (2)?: >? 1
# Max score: 18
# Optimal shift: 11
# -----------TTTCCCTGCTAATACGATAACGACGCCACTGGAGGACCGTTAAAAATTTA
# ACTCTAAGAGTCTAGGCTGGGACTAAAGTAAAAGCGGCGATAGTGGAGTT-----------
#
# # Example 2:
#
# >>> main()
# Type the file name of your first sequence: >? sequence_1
# Type the file name of your second sequence: >? sequence_2
# Set the maximum number of base pair shifts: >? 15
# Would you like to calculate the max score (1) or max chain (2)?: >? 2
# Max chain: 5
# Optimal shift: 14
# --------------TTTCCCTGCTAATACGATAACGACGCCACTGGAGGACCGTTAAAAATTTA
# ACTCTAAGAGTCTAGGCTGGGACTAAAGTAAAAGCGGCGATAGTGGAGTT--------------


```
