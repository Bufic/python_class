def student_Info():

    studentName = input("Enter your name: ")
    studentAge = int(input("Enter your age: "))
    studentGender = input("Enter your gender: ")
    studentphoneNumber = input("Enter your phone number: ")
    studentEmail = input("Enter your email address: ")
    
    student_file = {
        
        'name': studentName,
        'gender': studentGender,
        'age': studentAge,
        'phone_number': studentphoneNumber,
        'mail': studentEmail
    }
    
    return studentName, studentAge, studentGender, studentphoneNumber, studentEmail

    # print(f'student Name: {studentName}')
    # print(f'student Age: {studentAge}')
    # print(f'student Gender: {studentGender}')
    # print(f'student Phone Number: {studentphoneNumber}')
    # print(f'student Gender: {studentEmail}')
    
student_Info()    

#print(f"The student's name is {} and his phone number is {}, while his email address is {}.format(studentName,studentPhoneNumber,studentEmail)")