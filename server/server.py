from flask import Flask, request, jsonify
import util

app = Flask(__name__)

# A route where we get the location names from our saved artifact columns

@app.route('/get_location_names',methods=['GET'])
def get_location_names():

    response = jsonify({
        'locations': util.get_location_names()
    })

    response.headers.add('Access-Control-Allow-Origin','*')

    return response

# A route for both getting and posting values to be passed
# We use post to pass the parameters and get method to get the result

@app.route('/predict_home_price',methods=['GET','POST'])
def predict_home_price():

    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location,total_sqft,bhk,bath)
    })

    response.headers.add('Access-Control-Allow-Origin','*')

    return response

# This will enable the load_saved_artifacts and app.run function to be run when the server.py is called

if __name__ == '__main__':
    util.load_saved_artifacts()
    app.run()

