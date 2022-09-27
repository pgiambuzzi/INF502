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
