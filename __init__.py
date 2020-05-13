class Assigned:
    def __init__(self, car_full_data,car_categorical_data):
        self.car_full_data = car_full_data
        self.car_categorical_data = car_categorical_data
        #self.judge_filename = judge_filename

        import pandas as pd
        # First load the dataset into pandas dataframe
        self.car_full_data = pd.read_csv(car_full_data,delimiter=',')
        self.car_categorical_data = pd.read_csv(car_categorical_data,delimiter = ',', header = None)




    #Imported methods
    from .tasks.datatranslation import datatranslation
    from .tasks.convert_car_data import convert_car_data
    # from .tasks.knn import knn
    # from .tasks.Naive_Bayern import Naive_Bayern
    # from .tasks.SVM import svm
    # from .tasks.Decision_Tree import decision_tree
    from .tasks.classifiers import classifiers
    from .tasks.input_ import input_
    from .tasks.prediction import prediction
    from .tasks.Detection import detection









































