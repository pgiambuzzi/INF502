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

# Function that calculates the max number of matches from a DNA strand in a .txt file, prints the resulting
# shifted string of nucleotides, and preserves the original, un-shifted list of nucleotides.

def max_score(shift):
    list_1 = sequence1_to_list(file_1)
    list_2 = sequence2_to_list(file_2)
    for x in range(1, shift + 1):
        list_1.insert(0, "-")
        list_2.append("-")
    print(''.join(list_1))
    print(''.join(list_2))
    score = 0
    for x in range(len(list_1)):
        if list_1[x] == list_2[x]:
            score+=1
    print(score)

#how do i do a shift for each number in range(shift)?
#how do i select which shift is optimal?

#The following function puts the score of each shift into a list and then selects the maximum score from the list.
#This function then indexes this list of scores and spits out the number of shifts that yields the highest score.
#NEEDS FIXING: it needs to print the sequence shifted corresponsding to the max score, not the inputted shift value
#QUESTION: does the shift number have to be greater than 0??
def max_score1(shift):
    list_1 = sequence1_to_list(file_1)
    list_2 = sequence2_to_list(file_2)
    max_list = []
    for x in range(1, shift + 1):
        list_1.insert(0, "-")
        list_2.append("-")
        score = 0
        for x in range(len(list_1)):
            if list_1[x] == list_2[x]:
                score += 1
        max_list.append(score)
    print("Max score:", max(max_list))
    index = max_list.index(max(max_list))
    print("Optimal shift:", index+1)
    print(''.join(list_1))
    print(''.join(list_2))

max_value = max(input_list)
index = input_list.index(max_value)


max_chain =

shifted_dna =


# # exceptions: could not find file; input is not a valid approach; input is not an integer; input cannot be negative;
# # input must be greater than 0; DNA sequences are not the same length; Error: shift number cannot exceed the
# # number of base pairs in the sequence.

# for max chain, subtract one point for each that does not match when going from one pair to the next

# for inputs, define all in beginning and then add those as your args for the functions in your main function

```
