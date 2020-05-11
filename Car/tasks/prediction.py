def prediction(self,car_full_data,integer_data):
    (buying, maint, doors, persons, lug_boot, safety) = self.input_(car_full_data)
    gdata = integer_data
    X_gdata = gdata.drop(columns='prediction')
    Y_gdata = gdata['prediction']
    print(DTree(X_gdata,Y_gdata,buying, maint, doors, persons, lug_boot, safety))

def DTree(X_gdata,Y_gdata,buying, maint, doors, persons, lug_boot, safety):
    from sklearn.model_selection import train_test_split
    from sklearn.tree import DecisionTreeClassifier
    (X_train, X_test, Y_train, Y_test) = train_test_split(X_gdata, Y_gdata, test_size=0.2)
    decision_t = DecisionTreeClassifier()
    decision_t.fit(X_train,Y_train)
    y_pred = decision_t.predict(X_test)
    pre = decision_t.predict([[buying, maint, doors, persons, lug_boot, safety]])
    print(" Hey our decision is: ",pre)
