def classifiers(self,integer_data):
    import matplotlib.pyplot as plt
    gdata = integer_data
    X_gdata = gdata.drop(columns='prediction')
    Y_gdata = gdata['prediction']
    knn_Accuracy = KNN(X_gdata,Y_gdata)
    NB_Accuarcy = NB(X_gdata,Y_gdata)
    SVM_Accuracy = SVM(X_gdata,Y_gdata)
    DTree_Accuracy = DTree(X_gdata,Y_gdata)
    RF_Accuracy = RF(X_gdata,Y_gdata)
    Accuracy_list = [knn_Accuracy,NB_Accuarcy,SVM_Accuracy,DTree_Accuracy,RF_Accuracy]
    Accuracy_list_names = ['KNN','NB','SVM','DT','RF']
    plt.bar(Accuracy_list_names,Accuracy_list,width=0.3)
    plt.show()


    # return (knn_Accuracy,NB_Accuarcy,SVM_Accuracy,DTree_Accuracy)

def KNN(X_gdata,Y_gdata):
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import LabelEncoder
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.metrics import mean_squared_error
    from math import sqrt
    from sklearn.metrics import accuracy_score
    encode_data = LabelEncoder()
    (X_train, X_test, Y_train, Y_test) = train_test_split(X_gdata, Y_gdata, test_size=0.2)
    y_gdata_prediction = encode_data.fit_transform(Y_gdata)
    rmse = []
    for k in range(20):
        k = k + 1
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(X_gdata, y_gdata_prediction)
        pred = knn.predict(X_gdata)
        mean_error = mean_squared_error(y_gdata_prediction, pred)
        rmse.append(sqrt(mean_error))
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train, Y_train)
    knn_y_pred = knn.predict(X_test)
    Accuracy = accuracy_score(Y_test, knn_y_pred)

    return Accuracy

def NB(X_gdata, Y_gdata):
    from sklearn.model_selection import train_test_split
    from sklearn.naive_bayes import GaussianNB
    from sklearn.metrics import accuracy_score
    (X_train, X_test, Y_train, Y_test) = train_test_split(X_gdata, Y_gdata, test_size=0.2)
    naive_b = GaussianNB()
    naive_b.fit(X_train,Y_train)
    y_pred = naive_b.predict(X_test)
    Accuracy = accuracy_score(Y_test,y_pred)

    return Accuracy


def SVM(X_gdata, Y_gdata):
    from sklearn.model_selection import train_test_split
    from sklearn import svm
    from sklearn.metrics import accuracy_score
    (X_train, X_test, Y_train, Y_test) = train_test_split(X_gdata, Y_gdata, test_size=0.2)
    svm_c = svm.SVC()
    svm_c.fit(X_train, Y_train)
    y_pred = svm_c.predict(X_test)
    Accuracy = accuracy_score(Y_test, y_pred)

    return Accuracy

def DTree(X_gdata,Y_gdata):
    from sklearn.model_selection import train_test_split
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.metrics import accuracy_score
    (X_train, X_test, Y_train, Y_test) = train_test_split(X_gdata, Y_gdata, test_size=0.2)
    decision_t = DecisionTreeClassifier()
    decision_t.fit(X_train,Y_train)
    y_pred = decision_t.predict(X_test)
    Accuracy = accuracy_score(Y_test, y_pred)
    return Accuracy

def RF(X_gdata,Y_gdata):
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.metrics import accuracy_score
    (X_train, X_test, Y_train, Y_test) = train_test_split(X_gdata, Y_gdata, test_size=0.2)
    random_f = RandomForestClassifier()
    random_f.fit(X_train,Y_train)
    y_pred = random_f.predict(X_test)
    Accuracy = accuracy_score(Y_test,y_pred)

    return Accuracy
