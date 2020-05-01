def datatranslation(self, car_full_data):

    import pandas as pd
    import datetime
    ## CODE STARTS HERE ##

    gdata = self.car_full_data
    x = datetime.datetime.now()
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
        car_value_after_n_yers = value * (1 - (20 / 100))
        n = period - 1
        car_value_after_n_yers = car_value_after_n_yers * ((1 - (10 / 100)) ** n)
    else:
        return None
    ## Comparing the Given Input Amount and Obtained actual ammount of car ##
    given_value = float(input("Enter car value that yoy wish to sell: "))
    if given_value == car_value_after_n_yers:
        return "Accepted"
    elif(given_value < car_value_after_n_yers):
        try:
            #print("Low",(abs(given_value - car_value_after_n_yers) / car_value_after_n_yers) * 100.0)
            if(((abs(given_value - car_value_after_n_yers) / car_value_after_n_yers) * 100.0) >= 50) :
                return "low"
            elif(((abs(given_value - car_value_after_n_yers) / car_value_after_n_yers) * 100.0)  >=10) and (((abs(given_value - car_value_after_n_yers) / car_value_after_n_yers) * 100.0) <= 100) :
                return "low"
            else:
                return "med"
        except ZeroDivisionError:
            return float('inf')
    elif (given_value > car_value_after_n_yers):
        try:
            if(((abs(given_value - car_value_after_n_yers) / car_value_after_n_yers) * 100.0) >= 50):
                return "vhigh"
            elif(((abs(given_value - car_value_after_n_yers) / car_value_after_n_yers) * 100.0)  >=10) and (((abs(given_value - car_value_after_n_yers) / car_value_after_n_yers) * 100.0) <= 100) :
                return "high"
            else:
                return "med"
        except ZeroDivisionError:
            return float('inf')
        