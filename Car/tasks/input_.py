from Car.tasks.datatranslation import datatranslation  ##Calling the datatranslation function to get the buying price in categorical which is entered as integer##

def input_(self, car_full_data):
    ## Getting input from the customer and asking some specific details that will allow us to predict whether it can be accepted or not.##
    ## Changing categorical to Integer data, using the unique values from convert_car_data function where orginall data is converted to integer ##
    ## So when encoded fro each value, those same values are used and assigned here to the categorical data##
  
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
    buying = datatranslation(self, car_full_data)  ##Getting categorical value from the data translation part ##
    maint = input("Enter Maintainence in terms {low, med, high, vhigh} : ") ##Asking user to input car specifications##
    doors = input("Enter number of doors in numbers of {2,3,4 and 5more} : ") ##Asking user to input car specifications##
    persons = input("Enter number of persons can fit in the car in {2,4,more}: ") ##Asking user to input car specifications##
    lug_boot = input("Enter the lagguage boot available in terms of {small,med,big}: ") ##Asking user to input car specifications##
    safety = input("Enter the car safety in terms of {low,med,high}: ") ##Asking user to input car specifications##
    
    ##Manually changing them to integer from categorical ##
    ##After encoding using the unique values of each value is known and assigned them accordingly##
    if buying == 'vhigh':   ##Manually changing them to integer from categorical ##
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

    return (buying,maint,doors,persons,lug_boot,safety)  #Returning the input data which customer specified catgeorical data,which that is converted into integer##
