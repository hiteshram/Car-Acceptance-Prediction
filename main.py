from Car import *

q = Assigned(car_full_data ='./dataset/car.csv',
             car_categorical_data = './dataset/car_data.csv')



data = q.car_full_data
d = q.car_categorical_data
integer_data = q.convert_car_data(d)
print(q.prediction(data,integer_data))



