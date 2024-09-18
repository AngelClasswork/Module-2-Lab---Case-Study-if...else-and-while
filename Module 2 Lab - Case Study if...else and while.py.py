#Your name: Angel Contreras
#The file name for your app: "Module 2 Lab - Case Study: if...else and while"
#A brief description of what your app will do: This program was made to input student data and check if each student has made the Dean's list or the Honor roll.


#Starting the programs loop, the user has to enter a name or "zzz" to end the program.
while True:
    last_name = input("Please enter the student's last name or zzz to quit: ")
    if last_name == ("zzz"):
        print("This program will now shut down.")
        break 
    first_name = input("Enter the student's first name: ")
    gpa = float(input("What is your gpa?: "))
        
#The calculation the program will use to check if the student makes the Dean's list and the Honor roll.
    
    if gpa>= 3.5:
        print(f"{first_name} {last_name} has made the Dean's list!")
        print(f"{first_name} {last_name} has made the Honor Roll.")
    elif gpa >= 3.25:
        print(f"{first_name} {last_name} has made the Honor Roll.")
        
# If both the Gpa requirement and the Honor roll requirements are not met the user will get this prompt.
    else: 
        print(f"{first_name} {last_name} has not made the Dean's list or Honor roll.")
 