import pickle
import numpy as np
model = pickle.load(open('model.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))


# create a function to predict the output

def predict_price(year, km, ps, month, model, brand, fuel, vehicletype, gearbox, damage):
    input = np.zeros(len(X.columns))
    input[0] = year
    input[1] = km
    input[2] = ps
    input[3] = month
    input[4] = len(year)

    input[5] = les['name'].transform([year])[0]
    input[6] = les['gearbox'].transform([gearbox])[0]
    input[7] = les['notRepairedDamage'].transform([damage])[0]
    input[8] = les['model'].transform([model])[0]
    input[9] = les['brand'].transform([brand])[0]
    input[10] = les['fuelType'].transform([fuel])[0]
    input[11] = les['vehicleType'].transform([vehicletype])[0]

    return model.predict([input])[0]


# create a flask app

from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [x for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Car Price should be $ {}'.format(output))


if __name__ == "__main__":
    app.run()