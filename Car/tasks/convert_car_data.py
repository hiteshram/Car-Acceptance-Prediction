def convert_car_data(self, car_full_data):
    
    ##Encoding the car data from categorical to integer ##
    import pandas as pd
    pd.options.display.max_columns = None
    pd.options.display.width = None
    pd.options.display.max_rows = None

    gdata = car_full_data
    gdata = pd.DataFrame(gdata) ##Converting into Dataframe to make easy for encoding ##
    ##Renaming the columns with the columns names provided in names list for the dataset ##
    gdata.rename(columns={0: 'buying', 1: 'maint', 2: 'doors', 3: 'persons', 4: 'lug_boot', 5: 'safety', 6: 'prediction'}, inplace=True)
    
     ##Using pandas factorize encoding the values here down ##
    gdata['buying'],_ = pd.factorize(gdata['buying']) 
    gdata['maint'],_ = pd.factorize(gdata['maint'])
    gdata['doors'],_ = pd.factorize(gdata['doors'])
    gdata['persons'],_ = pd.factorize(gdata['persons'])
    gdata['lug_boot'],_ = pd.factorize(gdata['lug_boot'])
    gdata['safety'],_ = pd.factorize(gdata['safety'])

    return gdata
