attendance=int(input('enter a percentage:'))
if(attendance>=75):
    GP=0
    totalunit=0
    for i in range(1,6):
        scorepoint=int(input('enter the points:'))
        unit=int(input('enter the unit:'))
        totalunit+=unit
        gradepoint=scorepoint*unit
        GP+=gradepoint
    GPA=GP/totalunit
    print("your GPA for the courses is",GPA)
else:
    print('you have less than the required attendance for your grade')
