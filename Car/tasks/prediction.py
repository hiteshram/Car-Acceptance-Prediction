def prediction(self,car_full_data,integer_data):
    (buying, maint, doors, persons, lug_boot, safety) = self.input_(car_full_data)   ##Getting the car specifications from input function and used them for prediction##
    gdata = integer_data  ##Training the model, integer data is used##
    X_gdata = gdata.drop(columns='prediction') ## Dividing for training and testing ##
    Y_gdata = gdata['prediction']
    print(DTree(X_gdata,Y_gdata,buying, maint, doors, persons, lug_boot, safety)) ##Training data is sent along with the input parameters##

def DTree(X_gdata,Y_gdata,buying, maint, doors, persons, lug_boot, safety):
    from sklearn.model_selection import train_test_split
    from sklearn.tree import DecisionTreeClassifier 
    (X_train, X_test, Y_train, Y_test) = train_test_split(X_gdata, Y_gdata, test_size=0.2) ##Training and testing division, training 80% and testing 20%##
    decision_t = DecisionTreeClassifier() ##Decision tree used to trian the model ##
    decision_t.fit(X_train,Y_train)
    y_pred = decision_t.predict(X_test)
    pre = decision_t.predict([[buying, maint, doors, persons, lug_boot, safety]]) ##Predicting the output based on the model trained##
    print(" Dear Customer our decision is: ",pre)
