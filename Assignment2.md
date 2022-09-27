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

LINK TO CODE FILE: [pythagoreanTheorem.py](https://github.com/pgiambuzzi/INF502/blob/main/code/pythagoreanTheorem.py)

```python
import math

def pythagoreanTheorem(length_a, length_b):
   print(math.sqrt(length_a**2 + length_b**2))
   #I felt this was the most straightforward way of making this function, simply printing the result of hypotenuse calculation: c=sqrt(a^2+b^2)

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

link: [listmangler.py](https://github.com/pgiambuzzi/INF502/blob/main/code/listmangler.py)

```python
def list_mangler(list_in):
    list_new = []     #creating an empty list for our outputs
    for x in list_in: #creating a for loop to run through our original list
        if x % 2 == 0:
            list_new.append(x*2) #each even number in the given list is multiplied by 2
        else:
            list_new.append(x*3) #each odd number in the given list is multiplied by 3
    print(list_new)  #and the empty list is populated with our multiplication outputs
    
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

link: [grade_calc.py](https://github.com/pgiambuzzi/INF502/blob/main/code/grade_calc.py)

```python
def grade_calc(grades_in, to_drop):
    for x in range(1,to_drop+1): #need to tell python how many times to determine a minimum. A new minimum will be determined after each tim a min is removed.
        min_grade = min(grades_in) #calculates the minimum grade
        grades_in.remove(min_grade) #removes that min, then if to_drop is > 1, it will repeat corresponding to the value assigned to to_drop
    m = mean(grades_in) #the mean of the updated grades_in list is calculated
    if m >= 90: # a letter is assigned to each grade range and printed for the mean
        print("A")
    elif m >= 80 and m < 90:
        print("B")
    elif m >= 70 and m < 80:
        print("C")
    elif m >= 60 and m < 70:
        print("D")
    else:
        print("F")
        
#examples:
grade_calc([100, 20, 30, 90], 2)
A
grade_calc([100, 20, 30, 40], 3)
A
grade_calc([70, 40], 1)
C
grade_calc([34, 78, 93, 87, 45, 68, 98, 67, 85, 88, 90, 40, 20], 2)
C
```
In your solution markdown, please provide: a link to the .py file, a commented code, the output of a few examples (3-4).


**4. Write a function with the following signature:** `odd_even_filter(numbers)`.

The function accepts an input list of integers and returns a list with two sublists. The first sublist contains all even numbers in the input list and the second sublist contains all odd numbers.

link:

```python
def odd_even_filter(numbers):
    list_odd = [] #empty list for off numbers to go into
    list_even = [] #empty list for even numbers to go into
    for x in numbers: #for loop selects and adds even numbers to the empty list_even
        if x % 2 == 0:
            list_even.append(x)
        else:
            list_odd.append(x) #then selects and adds odd numbers to the empty list_odd
    print(list_even, list_odd) #then we print the two new lists side by side

#examples:
odd_even_filter([1, 3, 4, 6, 2, 5, 4, 7])
[4, 6, 2, 4] [1, 3, 5, 7]
```
In your solution markdown, please provide: a link to the .py file, a commented code, the output of a few examples (3-4).
