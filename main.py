################ Function Definitions ################

# Shows the user what options they have
def displayMenu():

  print("1. Add a Student")

  print("2. Remove a Student")

  print("3. Add Quiz Grade for Student")

  print("4. List a Student's Quiz Grades")

  print("5. Get Student's Letter Grade")

  print("6. Quit")

# Prompts the user to enter a numeric grade & ensures the user entered a valid float for the grade
def getNumberGradeFromUser():

  val = None

  while(val == None):
    try:
      test = float(input("Enter a Grade: "))
      val = test
    except:
      val = None
  
  return val
  
#Compares the grade (grade_average) number with the parameters then returns it as a letter grade
def getLetterGrade(grade):
  if(grade >= 90):
    return "A"
  elif(grade >= 80):
    return "B"
  elif(grade >= 70):
    return "C"
  elif(grade >= 60):
    return "D"
  elif(grade >= 50):
    return "E"
  else:
    return "F"
    
      # # # # # Variables # # # # #
    
userchoice = ""
student_name = ""
student_grades = []
student_records = {}
# set dictionary student_records{} key as student_names to equal the value as the student_grades list []
student_records[student_name] = student_grades

  ################ Main Program ################ 

# application loop to run UNTILL user enters "6" (Quit)
while(userchoice != "6"):
  print()
  # call the menu function to display options for user
  displayMenu()
  # Prompt the user to select an option
  userchoice = input("Select an Option: ")

  # if user's choice equals == "1"
  if(userchoice == "1"):
    student_name = input("Enter student name: ")
    #have student name added to dictionary key 
    student_records[student_name] = student_grades
    print(f"{student_name} added!")
    
  # if user's choice equals == "2"
  if(userchoice == "2"):
    student_name = input("Enter student to remove: ")
    # check if student is in dictionary
    if(student_name in student_records):
        # take out the entered name from dictionary
        student_records.pop(student_name)
        print(f"{student_name} removed!")
    else:
      print(f"{student_name} not in dictionary!")
      
  # if user's choice equals == "3"
  if(userchoice == "3"):
    student_name = input("Enter student name: ")
    # check if student is in dictionary
    if(student_name in student_records):
      # variable name for grade entered using the function getNumberGradeFromUser to ensure user validation
      new_grade = getNumberGradeFromUser()
      # adding new grades to the list student_grades 
      student_grades.append(new_grade)
      # making sure it is associated with the dictionary
      student_records[student_name] = student_grades 
      print(f"Added {new_grade} to {student_name}'s quizes.")
    else:
      print(f"{student_name} not in dictionary!")

  # if user's choice equals == "4"  
  if(userchoice == "4"):
    student_name = input("Enter a student name: ")
    # check if student name entered is in dictionary
    if(student_name in student_records):
      print(f"{student_name}'s Quizzes: ")
      # have grades printed out individually 
      for grade in student_grades:
        print(grade)
    else:
      print(f"{student_name} not in dictionary!")

  # if user's choice equals == "5"  
  if(userchoice == "5"):
    student_name = input("Enter student name: ")
    # check if student name in dictionary
    if(student_name in student_records):
      #Set variable name for calculating grade average &
      #Add all items in the student_grades list using the sum() function and devide it by the number of grades using the len() function.
      grade_average =     sum(student_grades)/len(student_grades)
      # create variable name to hold letter grade 
      letter_grade = getLetterGrade(grade_average)
      print(f"{student_name}'s current grade is a {letter_grade}") 