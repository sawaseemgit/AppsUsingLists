print("Welcome to the Grade Sorter App")
gradeList = []
firstScore = int(input("Enter the first grade: "))
gradeList.append(firstScore)
secondScore = int(input("Enter the second grade: "))
gradeList.append(secondScore)
thirdScore = int(input("Enter the third grade: "))
gradeList.append(thirdScore)
forthScore = int(input("Enter the forth grade: "))
gradeList.append(forthScore)

print('Your grades are: ', gradeList)
gradeList.sort(reverse=True)
print('Your grades from highest to lowest are: ', gradeList)

print('The lowest two grades will now be dropped')
removedGrade = gradeList.pop()
print("Removed grade: ", removedGrade)
removedGrade = gradeList.pop()
print("Removed grade: ", removedGrade)
print('Your remaining grades are: ', gradeList)
print('Nice work! Your highest grade is: ', gradeList[0])
