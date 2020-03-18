class Assigned:
    def __init__(self, car_dataset_filename):
        self.car_dataset = car_dataset_filename
        #self.judge_filename = judge_filename

        import pandas as pd
        # First load the dataset into pandas dataframe
        self.car_dataset = pd.read_csv(car_dataset_filename,delimiter=',')
        #self.judge_dataset = pd.read_csv(judge_filename,delimiter=',')




    #Imported methods
    from .tasks.datatranslation import datatranslation





















