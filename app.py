import flask
import pickle
import pandas as pd
import cv2
import os
from difflib import SequenceMatcher
from csv import writer

UPLOAD_FOLDER = 'D:\\University of Colorado\\Subjects\\02_ML\\Project\\CarAcceptance'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


with open(f'model/car_accpetance_model.pkl', 'rb') as f:
    model = pickle.load(f)

app = flask.Flask(__name__, template_folder='templates')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/',methods=['GET', 'POST'])

def main():
    if flask.request.method == 'GET':
        return(flask.render_template('main.html'))
    
    if flask.request.method == 'POST':
        car_make = flask.request.form['Make']
        car_model = flask.request.form['Model']
        car_purchase_year = flask.request.form['Purchase_Year']
        car_selling_amount=flask.request.form['Selling_Amount']
        car_maintenance=flask.request.form['Maintenance']
        car_doors=flask.request.form['Doors']
        car_persons=flask.request.form['Persons']
        car_lugguage=flask.request.form['Lugguage']
        car_safety=flask.request.form['Safety']
        car_number=flask.request.form['car-license-number']
        
        car_image=flask.request.files['car-license-plate-img']
        car_image.save(os.path.join(app.config['UPLOAD_FOLDER'], 'image_test.jpg'))
        
        customer_image=flask.request.files['customer-img']
        customer_image.save(os.path.join(app.config['UPLOAD_FOLDER'], 'customer_test.jpg'))
        
        car_img = cv2.imread(UPLOAD_FOLDER+'\\image_test.jpg')    
        predicted_car_number=get_number_plate(car_img)
        
           
        
        face_recognizer_lbp = cv2.face.LBPHFaceRecognizer_create()
        face_recognizer_lbp.read('face_recognizer_lbp.xml')
        cust_img = cv2.imread(UPLOAD_FOLDER+'\\customer_test.jpg')
        resize_cust_img=cv2.resize(cust_img,(200,200))
        grey_cust_img = cv2.cvtColor(resize_cust_img,cv2.COLOR_BGR2GRAY)
        label,confidence = face_recognizer_lbp.predict(grey_cust_img)    
        
        police_record="No"
        if(confidence<40):
            police_record="Yes"
        else:
            police_record="No"
    
        [buying,maint,doors,persons,lug_boot,safety]=input_(car_make,car_model,car_purchase_year,car_selling_amount,car_maintenance,car_doors,car_persons,car_lugguage,car_safety)
        
            
        input_variables = pd.DataFrame([[buying,maint,doors,persons,lug_boot,safety]],
                                       columns=['buying', 'maint','doors','persons','lug_boot','safety'],
                                       dtype=int)
    
        original_prediction = model.predict(input_variables)[0]
        
        original_selling_amount=car_selling_amount
        depreciated_price=getdepreciatedvalue(car_make,car_model,car_purchase_year)
        depreciated_price=round(depreciated_price,2)
        final_prediction=original_prediction
        selling_amount=float(car_selling_amount)
        if((original_prediction=='unacc' or original_prediction=='acc' or original_prediction=='good') and (buying==0 or buying==1)):
            while(True):
                selling_amount=selling_amount-(selling_amount*0.1)
                [buying,maint,doors,persons,lug_boot,safety]=input_(car_make,car_model,car_purchase_year,selling_amount,car_maintenance,car_doors,car_persons,car_lugguage,car_safety)
                input_variables = pd.DataFrame([[buying,maint,doors,persons,lug_boot,safety]],
                                       columns=['buying', 'maint','doors','persons','lug_boot','safety'],
                                       dtype=int)
                prediction = model.predict(input_variables)[0]
                if(buying==2 or buying==3):
                    final_prediction=prediction
                    break
        
        '''
        values we are storing in the dataframe Model, make, purchase year, selling price, depreciated price, proposed price,profit observed, License plate verified, police record
        '''
        profit=abs(float(car_selling_amount)-float(selling_amount))
        car_verified=""
        car_similarity=SequenceMatcher(car_number,predicted_car_number).ratio()
        if(car_similarity>=0.9):
            car_verified="Yes"
        else:
            car_verified="No"
    
        append_list_as_row('Price_Prediction_Results.csv',[car_make,car_model,car_purchase_year,car_selling_amount,depreciated_price,selling_amount,profit,car_verified,police_record])
        append_list_as_row('License_Plate_Prediction_Results.csv',[car_number,predicted_car_number,car_similarity])
        append_list_as_row('Facial_Recognition_Prediction_Results.csv',[police_record,confidence])
        
        return flask.render_template('main.html',
                                     original_input={
                                                     #'Buying':buying,
                                                     #'Maintenance':maint,
                                                     #'Doors':doors,
                                                     #'Persons':persons,
                                                     #'Lugguage':lug_boot,
                                                     #'Safety':safety,
                                                     'Selling-Price':original_selling_amount,
                                                     'Depreciated-Price':depreciated_price,
                                                     'Proposed-Price':selling_amount,
                                                     #'Original-Prediction':original_prediction,
                                                     #'Final-Prediction':final_prediction,
                                                     'Original Car Number':car_number,
                                                     'Predicted Car Number':predicted_car_number,
                                                     'Police Record':police_record
                                                     },
                                     result=prediction
                                     )



def append_list_as_row(file_name, list_of_elem):
    with open(file_name, 'a+', newline='') as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow(list_of_elem)

def get_number_plate(img):
    import numpy as np
    import cv2
    import imutils
    #import sys
    import pytesseract
    #import pandas as pd
    
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    img = imutils.resize(img, width=500)
    #cv2.imshow("Original Image", img)
    #cv2.waitKey(0)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #cv2.imshow("Preprocess 1 - Grayscale Conversion", gray_img)
    #cv2.waitKey(0)
    gray_img = cv2.bilateralFilter(gray_img, 11, 17, 17)
    #cv2.imshow("Preprocess 2 - Bilateral Filter", gray_img)
    #cv2.waitKey(0)
    c_edge = cv2.Canny(gray_img, 170, 200)
    #cv2.imshow("Preprocess 3 - Canny Edges", c_edge)
    #cv2.waitKey(0)
    cnt, new = cv2.findContours(c_edge, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cnt = sorted(cnt, key = cv2.contourArea, reverse = True)[:30]
    NumberPlateCount = None
    im2 = img.copy()
    cv2.drawContours(im2, cnt, -1, (0,255,0), 3)
    #cv2.imshow("Top 30 Contours", im2)
    #cv2.waitKey(0)
    #count = 0

    for c in cnt:
        perimeter = cv2.arcLength(c, True)      #Getting perimeter of each contour
        approx = cv2.approxPolyDP(c, 0.02 * perimeter, True)
        if len(approx) == 4:            #Selecting the contour with 4 corners/sides.
            NumberPlateCount = approx
            break
    
    masked = np.zeros(gray_img.shape,np.uint8)
    new_image = cv2.drawContours(masked,[NumberPlateCount],0,255,-1)
    new_image = cv2.bitwise_and(img,img,mask=masked)

    configr = ('-l eng --oem 1 --psm 3')
    text_no = pytesseract.image_to_string(new_image, config=configr)
    return text_no


def input_(car_make,car_model,purchase_year,selling_amount,maint,doors,persons,lug_boot,safety):
    
    buying = datatranslation(car_make,car_model,purchase_year,selling_amount)
    if buying == 'vhigh':
        buying = 0
    elif buying == 'high':
        buying = 1
    elif buying == 'med':
        buying = 2
    else:
        buying = 3

    if maint == 'vhigh':
        maint = 0
    elif maint == 'high':
        maint = 1
    elif maint == 'med':
        maint = 2
    else:
        maint = 3

    if doors == 2:
        doors = 0
    elif doors == 3:
        doors = 1
    elif doors == 4:
        doors = 2
    else:
        doors = 3

    if persons == 2:
        persons = 0
    elif persons == 4:
        persons = 1
    else:
        persons = 2

    if lug_boot == 'small':
        lug_boot = 0
    elif lug_boot == 'med':
        lug_boot = 1
    elif lug_boot == 'big':
        lug_boot = 2
    else:
        print("Invalid")

    if safety == 'low':
        safety = 0
    elif safety == 'med':
        safety = 1
    elif safety == 'high':
        safety = 2
    else:
        print("Invalid")

    return [buying,maint,doors,persons,lug_boot,safety]


def getdepreciatedvalue(car_make,car_model,purchase_year):
    import datetime
    ## CODE STARTS HERE ##

    gdata = pd.read_csv('./dataset/car.csv')
    
    x = datetime.datetime.now()
    c_year = x.year
    #y = gdata["Year"].apply(lambda y: c_year - y)
    new_gdata = pd.DataFrame(gdata, columns= ['Make', 'Model', 'MSRP'])
    make_input = car_make
    model_input = car_model
    value = (new_gdata.loc[new_gdata['Model'] == model_input, 'MSRP'].iloc[0])
    value = value.replace(',','')
    value = int(value[1:])
    year = int(purchase_year)
    period = c_year - year
    if (period <= 1):
        car_value_after_n_yers = value * (1 - (20/100))
            
    elif (period > 1):
        car_value_after_n_yers = value * (1 - (20 / 100))
        n = period - 1
        car_value_after_n_yers = car_value_after_n_yers * ((1 - (10 / 100)) ** n)
    
    return car_value_after_n_yers


def datatranslation(car_make,car_model,purchase_year,selling_amount):

    import datetime
    ## CODE STARTS HERE ##

    gdata = pd.read_csv('./dataset/car.csv')
    
    x = datetime.datetime.now()
    c_year = x.year
    #y = gdata["Year"].apply(lambda y: c_year - y)
    new_gdata = pd.DataFrame(gdata, columns= ['Make', 'Model', 'MSRP'])
    make_input = car_make
    model_input = car_model
    value = (new_gdata.loc[new_gdata['Model'] == model_input, 'MSRP'].iloc[0])
    value = value.replace(',','')
    value = int(value[1:])
    year = int(purchase_year)
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
    given_value = float(selling_amount)

    if(given_value <= car_value_after_n_yers):
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
        


if __name__ == '__main__':
    app.run()