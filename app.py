from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

#model = pickle.load(open('model.pkl','rb'))

filename = 'Lung_Cancer.pkl'
with open(filename, 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def hello_world():
    return render_template("lung_cancer.html")

#Parameters used for Prediction
# ['GENDER', 'AGE', 'SMOKING', 'YELLOW_FINGERS', 'ANXIETY',
#        'PEER_PRESSURE', 'CHRONIC DISEASE', 'FATIGUE ', 'ALLERGY ', 'WHEEZING',
#        'ALCOHOL CONSUMING', 'COUGHING', 'SHORTNESS OF BREATH',
#        'SWALLOWING DIFFICULTY', 'CHEST PAIN', 'LUNG_CANCER']

@app.route('/predict',methods=['POST', 'GET'])
def predict():
        if request.method == 'POST':
            int_features = [int(x) for x in request.form.values()]
            final = np.reshape(int_features, (1, -1))
            print(int_features)  #Checking Inputs Successfully Added
            print(final) #Reshaping into numpy array for Prediction
            prediction = model.predict(final)
            print(prediction) # Checking the Prediction Value
            output = prediction
            if output == 0:
                return render_template('lung_cancer.html', pred='Person Has Lung Cancer {}'.format(output))
            else:
                return render_template('lung_cancer.html', pred='Person Does Not Got Lung Cancer {}'.format(output))
        else:
            return render_template('lung_cancer.html')

if __name__ == '__main__':
    app.run(debug=True)
