#Test Average and Grade

#Enter 6 test scores
test1 = int(input('Enter score 1: '))
test2 = int(input('Enter score 2: '))
test3 = int(input('Enter score 3: '))
test4 = int(input('Enter score 4: '))
test5 = int(input('Enter score 5: '))
test6 = int(input('Enter score 6: '))

total =(test1 + test2 + test3 + test4 + test5+ test6)

#Calculate average
def calc_average(total):
    return total / 6

#Grading scale
def determine_score(grade):
    if 70 <= grade <= 100:
        return 'A'
    elif 60 <= grade <= 69:
        return 'B'
    elif 50 <= grade <= 59:
        return 'C'
    elif 40 <= grade <= 49:
        return 'D'
    elif 0 > grade <= 39:
        return 'fail'
    else:
        return'F'



grade = total
avg = calc_average(total)
abc_grade = determine_score(grade)

print("That's a(n): " + str(abc_grade))
print('Average grade is: ' + str(avg))