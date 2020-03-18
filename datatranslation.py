def datatranslation(self, car_dataset):

    import numpy as np
    import pandas as pd
    import datetime
    pd.options.display.max_columns = None
    pd.options.display.width = None

    #pd.options.display.max_rows = None
    ## CODE STARTS HERE ##

    gdata = self.car_dataset
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
                return "Very Low"
            elif(((abs(given_value - car_value_after_n_yers) / car_value_after_n_yers) * 100.0)  >=10) and (((abs(given_value - car_value_after_n_yers) / car_value_after_n_yers) * 100.0) <= 100) :
                return "Low"
            else:
                return "Med"
        except ZeroDivisionError:
            return float('inf')
    elif (given_value > car_value_after_n_yers):
        try:
            if(((abs(given_value - car_value_after_n_yers) / car_value_after_n_yers) * 100.0) >= 50):
                return "Very High"
            elif(((abs(given_value - car_value_after_n_yers) / car_value_after_n_yers) * 100.0)  >=10) and (((abs(given_value - car_value_after_n_yers) / car_value_after_n_yers) * 100.0) <= 100) :
                return "High"
            else:
                return "Med"
        except ZeroDivisionError:
            return float('inf')
