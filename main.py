from Car import *

q = Assigned(car_dataset_filename='./dataset/car.csv')
             #judge_filename='dataset/judge-without-labels.csv')

data = q.car_dataset
print(q.datatranslation(data))
