# Return total exercise score of student. One point is earned for every 10 points earned through exercises. Score returned must be converted to
# integer and rounded down.
def exercise_grade(exercise_total): 
    exercise_score = exercise_total / 10
    
    return int(exercise_score)

def exam_grade(exam_total): # Return if a student has failed the course if exam score is < 10.
    course_pass = True
    if exam_total < 10:
        course_pass = False
    
    return course_pass

def total_grade(exam_score, exercise_score): # Combined exam score and exercise score and return total grade.
    overall_course_points = exam_score + exercise_score
        
    return overall_course_points

def grade_point_conversion(student_score): # Convert and return student's total grade into their gradepoint.
    if 0 <= student_score <= 14:
        overall_course_points = 0
    elif 15 <= student_score <= 17:
        overall_course_points = 1
    elif 18 <= student_score <= 20:
        overall_course_points = 2
    elif 21 <= student_score <= 23:
        overall_course_points = 3
    elif 24 <= student_score <= 27:
        overall_course_points = 4
    elif 28 <= student_score <= 30:
        overall_course_points = 5
    
    return overall_course_points


def average_points(student_scores): # Return average score of all students in the course.
    course_average = sum(student_scores) / len(student_scores)
    
    return course_average

# Print list to show placement of students on gradepoint scale.
def grade_distribution(course_points : list):    
    x = 5
    while x >= 0:
        print(f"{x: >3}: ", end="")
        for i in course_points:
            if i == x:
                print("*", end="")
        print(end='\n')
            
        x -= 1    

def main():
    student_points = str(input("Exam points and exercises completed: "))
    #  Score list is used to store the total points an individual student has earned.  
    score_list = []
    #  Grade list is a list of the scores of each of the students that has been converted to a grade point.
    grade_list = []

    #  Total number of students in the course, counted with each score input.    
    student_count = 0
    #  Number of students that have passed based on their scores.
    student_pass = 0

    while student_points != "": # Stop receiving input when blankspace is entered.
        student_count += 1
          
        #  Separates exam and exercise scores into two separate items in a list.
        split = student_points.split(" ")
        #  For loop used to store then process exam and exercise scores individually.
        for i in range(len(split)):
            if i == 0:
                exam_total = int(split[i])
                exam_pass = exam_grade(exam_total)
            else:
                exercise_points = int(split[i])
                exercise_total = exercise_grade(exercise_points)

        #  If student passed exam, store grade point based on student performance. Otherwise, automatically
        #  store grade point of 0 if student failed exam.      
        if exam_pass == True:
            course_score = total_grade(exam_total, exercise_total)
            score_list.append(course_score)
            grade_list.append(grade_point_conversion(course_score))
            
            if course_score > 0:
                student_pass += 1
        else:
            course_score = total_grade(exam_total, exercise_total)
            score_list.append(course_score)
            grade_list.append(0)

        student_points = str(input("Exam points and exercises completed: "))

    print("Statistics: ")
    print(f"Points average: {average_points(score_list):.1f}")
    print(f"Pass percentage: {(student_pass / student_count) * 100:.1f}")
    print("Grade distribution:")
    grade_distribution(grade_list)
    
main()