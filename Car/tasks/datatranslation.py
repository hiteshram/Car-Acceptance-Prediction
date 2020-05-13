def datatranslation(self, car_full_data):
## Finding the rate of depreciation of car and converting the amount entered by the customer to categorical data ##
## Rate of depreciation 20% for 1st year and 10% followed by each year ##
    import pandas as pd
    import datetime
    gdata = self.car_full_data      ## Getting Car data into gdata##
    x = datetime.datetime.now()     ##Present time##
    c_year = x.year
    #y = gdata["Year"].apply(lambda y: c_year - y)
    new_gdata = pd.DataFrame(gdata, columns= ['Make', 'Model', 'MSRP'])
    make_input = input("Enter Make: ")
    model_input = input("Enter model: ")
    value = (new_gdata.loc[new_gdata['Model'] == model_input, 'MSRP'].iloc[0])
    value = value.replace(',','')
    value = int(value[1:])
    year = int(input("Enter car purchase year: "))
    period = c_year - year
    if (period <= 1):
        car_value_after_n_yers = value * (1 - (20/100))

    elif (period > 1):
        car_value_after_n_yers = value * (1 - (20 / 100))       ##20% for first year Depriciation##
        n = period - 1
        car_value_after_n_yers = car_value_after_n_yers * ((1 - (10 / 100)) ** n)    ##10% after every year followed by 1st year ##
    else:
        return None
    ## Comparing the Given Input Amount and Obtained actual ammount of car ##
    given_value = float(input("Enter car value that yoy wish to sell: "))
    if given_value == car_value_after_n_yers:
        return "Accepted"
    elif(given_value < car_value_after_n_yers):
        try:
#             print("The Value of the car user wish to sell is: ", given_value, )
#             print("The Actual car value after N  year is: ", car_value_after_n_yers)
            #print("Low",(abs(given_value - car_value_after_n_yers) / car_value_after_n_yers) * 100.0)
            if(((abs(given_value - car_value_after_n_yers) / car_value_after_n_yers) * 100.0) >= 50) :  ##Calculating the depreciation percentage if it less and greater than 50 then vhigh is assigned##
                return "low"
            elif(((abs(given_value - car_value_after_n_yers) / car_value_after_n_yers) * 100.0)  >=10) and (((abs(given_value - car_value_after_n_yers) / car_value_after_n_yers) * 100.0) <= 50) :
                return "low"        ##Calculating the depreciation percentage if it less and greater than 10 and less than 50 then high is assigned##
            else:
                return "med"        ##less than 10% assigned as med ##
        except ZeroDivisionError:
            return float('inf')
    elif (given_value > car_value_after_n_yers):
        try:
#             print("The Value of the car user wish to sell is: ", given_value, )
#             print("The Actual car value after N  year is: ", car_value_after_n_yers)
            if(((abs(given_value - car_value_after_n_yers) / car_value_after_n_yers) * 100.0) >= 50):  ##Calculating the depreciation percentage if it more and greater than 50 then vhigh is assigned##
                return "vhigh"
            elif(((abs(given_value - car_value_after_n_yers) / car_value_after_n_yers) * 100.0)  >=10) and (((abs(given_value - car_value_after_n_yers) / car_value_after_n_yers) * 100.0) <= 50) :
                return "high"    ##Calculating the depreciation percentage if it more and greater than 10 and less than 50 then high is assigned##
            else:
                return "med"  ## less than 10% med is assigned ##
        except ZeroDivisionError:
            return float('inf')
        
