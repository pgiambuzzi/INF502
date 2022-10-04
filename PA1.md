```python

########################################

# Random DNA Sequence Generator that writes the new sequence to a file:

from random import choice

def random_sequence_1(length):
    nucleotides = ["A", "C", "G", "T"]
    sequence = ""
    file = open("sequence_1.txt", "x")
    for i in range(length):
        nucleotide = choice(nucleotides)
        sequence += nucleotide
    file.write(sequence)

def random_sequence_2(length):
    nucleotides = ["A", "C", "G", "T"]
    sequence = ""
    file = open("sequence_2.txt", "x")
    for i in range(length):
        nucleotide = choice(nucleotides)
        sequence += nucleotide
    file.write(sequence)

# TA-DA! We can now put two .txt files containing random DNA sequences into our working directory.

# Requesting inputs from user:

file_1 = input("Type the file name of your first sequence: ")
file_2 = input("Type the file name of your second sequence: ")
shift = input("Set the maximum number of base pair shifts: ")
approach = input("Would you like to calculate the max score (1) or max chain (2)?: ")

# Reading in files and changing to a list, adding dashes to the list corresponding to the number of shifts requested
# rather than editting the original file:

def sequence1_to_list(file_1):
    sequence_1_list = []
    sequence_1 = open(file_1, 'r')
    sequence_1_read = sequence_1.read()
    sequence_1.close
    for x in range(len(sequence_1_read)):
        sequence_1_list.append(sequence_1_read[x])
    return sequence_1_list

def sequence2_to_list(file_2):
    sequence_2_list = []
    sequence_2 = open(file_2, "r")
    sequence_2_read = sequence_2.read()
    sequence_2.close
    for x in range(len(sequence_2_read)):
        sequence_2_list.append(sequence_2_read[x])
    return sequence_2_list


#The following function takes a two sequences files that the user has provided and puts the score of each shift into a list and then selects the maximum score from the list.
#This function then indexes this list of scores and spits out the number of shifts that yields the highest score.
#This function is also able to select 0 shifts as the optimal shift if that is the case.
def max_score(shift):
    list_1 = sequence1_to_list(file_1) #loading the user input file for sequence 1 into a list
    list_2 = sequence2_to_list(file_2) #loading the user input file for sequence 2 into a list
    max_list = [] #creating an empty list in which the score for each shift will be entered
    if isinstance(shift, float) == True: #tells the user that decimal (type: float) values cannot be supplied, only integers
        print("Decimal values cannot be accepted for 'shift'. Please supply a positive integer.")
    elif shift > 0: #when a number of shifts is provided, the following loop is run
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


max_chain =

shifted_dna =


# # exceptions: could not find file; input is not a valid approach; input is not an integer; input cannot be negative;
# # input must be greater than 0; DNA sequences are not the same length; Error: shift number cannot exceed the
# # number of base pairs in the sequence. cannot accept decimal (type:float) values, function only accepts integers

# for max chain, subtract one point for each that does not match when going from one pair to the next

# for inputs, define all in beginning and then add those as your args for the functions in your main function

```
