# Assignment 2: Python Basics

* **INDIVIDUAL ASSIGNMENT**
* **Deadline**: Sept-27th 11:59PM
* **Value**: 100 points counted towards Homework category
* 
* **How to submit**: In your GitHub repository called *INF502* (same used for the Assignment 1) create a file called *"Assignment2.md"* with the following content:
  1. The problem's specification (as provided below in this file);
  2. A solution for each problem (in Python). Use the tag ```code``` to write the code along with the explanation.
  3. Explanation about the code (comments on variables and their meanings, explanation on why you used one or another approach, logical reasoning). The explanation can be either comments inside the code or text as a response to the problem in the markdown file.
  4. Create a folder called `code` and add the Python files (.py) with the solution. Link these files in your answer for each problem.
  Please remember to check if you invited me to see your repository (do so if you did not do for Assignment 1). I will evaluate the latest commit before 11:59PM (Sept-27th)

## Problems

**1. Write a function with the following signature:** `pythagoreanTheorem(length_a, length_b)`.

The function returns the length of the hypotenuse assuming that `length_a` and `length_b` are the lengths of the two legs of a right triangle (the legs that form the triangle's right angle). Hint: the `math` module might have useful functions to use.

```python
https://github.com/pgiambuzzi/INF502/blob/main/code/pythagoreanTheorem.py

import math

def pythagoreanTheorem(length_a, length_b):
   #I felt this was the most straightforward way of making this function, simply printing the result of hypotenuse calculation: c=sqrt(a^2+b^2)
   print(math.sqrt(length_a**2 + length_b**2))

#examples:
pythagoreanTheorem(2,8)
8.246211251235321
pythagoreanTheorem(3,9)
9.486832980505138
pythagoreanTheorem(5,6)
7.810249675906654

```
In your solution markdown, please provide: a link to the .py file, a commented code, the output of a few examples (3-4).

**2. Write a function with the following signature:** `list_mangler(list_in)`.

The function assumes that `list_in` is a list of integers, and returns a new list containing transformed elements of `list_in`. If the element is even, it's doubled. If the element is odd, it's tripled.

```python
def list_mangler(list_in):
    #creating an empty list for our outputs
    list_new = []
    #creating a for loop to run through our original list
    for item in list_in:
    #each even number in the given list is multiplied by 2
        if item % 2 == 0:
            list_new.append(item*2)
    #each odd number in the given list is multiplied by 3
        else:
            list_new.append(item*3)
    #and the empty list is populated with our multiplication outputs
    print(list_new)
    
#examples:
list_mangler([1, 2, 3, 4])
[3, 4, 9, 8]
list_mangler([5, 6, 7, 8])
[15, 12, 21, 16]
list_mangler([9, 10, 11, 12])
[27, 20, 33, 24]
```
In your solution markdown, please provide: a link to the .py file, a commented code, the output of a few examples (3-4).

**3. Write a function with the following signature:** `grade_calc(grades_in, to_drop)`.

The function accepts a list `grades_in` containing integer grades, drops the `to_drop` lowest grades (so, for `to_drop` equal to 2, the function should drop the 2 lowest grades), calculates the average of the grades left, and returns the letter grade this average corresponds to according to the letter grade scale for this course.

For example:

```
print(grade_calc([100, 90, 80, 95], 2)) # drops the 2 lowest grades (80 and 90)
'A'
```
In your solution markdown, please provide: a link to the .py file, a commented code, the output of a few examples (3-4).


**4. Write a function with the following signature:** `odd_even_filter(numbers)`.

The function accepts an input list of integers and returns a list with two sublists. The first sublist contains all even numbers in the input list and the second sublist contains all odd numbers.

For example:
```
print(odd_even_filter([1, 2, 3, 4, 5, 6, 7, 8, 9]))
[[2, 4, 6, 8], [1, 3, 5, 7, 9]]
print(odd_even_filter([3, 9, 43, 7]))
[[], [3, 9, 43, 7]]
print(odd_even_filter([71, 39, 98, 79, 5, 89, 50, 90, 2, 56]))
[[98, 50, 90, 2, 56], [71, 39, 79, 5, 89]]
```
In your solution markdown, please provide: a link to the .py file, a commented code, the output of a few examples (3-4).
