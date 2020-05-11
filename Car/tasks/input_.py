from Car.tasks.datatranslation import datatranslation

def input_(self, car_full_data):
#     buying = datatranslation(self, car_full_data)
#     print("Enter Maintainence in terms {low, med, high, vhigh} : ")
#     maint = input()
#     print("Enter number of doors in numbers of {2,3,4 and 5more} : ")
#     doors = input()
#     print("Enter number of persons can fit in the car in {2,4,more}: ")
#     persons = input()
#     print("Enter the lagguage boot available in terms of {small,med,big}: ")
#     lug_boot = input()
#     print("Enter the car safety in terms of {low,med,high}: ")
#     safety = input()
    buying = datatranslation(self, car_full_data)
    maint = input("Enter Maintainence in terms {low, med, high, vhigh} : ")
    doors = input("Enter number of doors in numbers of {2,3,4 and 5more} : ")
    persons = input("Enter number of persons can fit in the car in {2,4,more}: ")
    lug_boot = input("Enter the lagguage boot available in terms of {small,med,big}: ")
    safety = input("Enter the car safety in terms of {low,med,high}: ")
    if buying == 'vhigh':
        buying = 0
    elif buying == 'high':
        buying = 1
    elif buying == 'med':
        buying = 2
    else:
        buying = 3

    if maint == 'vhigh':
        maint = 0
    elif maint == 'high':
        maint = 1
    elif maint == 'med':
        maint = 2
    else:
        maint = 3

    if doors == 2:
        doors = 0
    elif doors == 3:
        doors = 1
    elif doors == 4:
        doors = 2
    else:
        doors = 3

    if persons == 2:
        persons = 0
    elif persons == 4:
        persons = 1
    else:
        persons = 2

    if lug_boot == 'small':
        lug_boot = 0
    elif lug_boot == 'med':
        lug_boot = 1
    elif lug_boot == 'big':
        lug_boot = 2
    else:
        print("Invalid")

    if safety == 'low':
        safety = 0
    elif safety == 'med':
        safety = 1
    elif safety == 'high':
        safety = 2
    else:
        print("Invalid")

    return (buying,maint,doors,persons,lug_boot,safety)
