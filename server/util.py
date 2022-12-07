import json
import pickle
import numpy as np

# Initializing variables

__locations = None
__data_columns = None
__model = None

# Price prediction 

def get_estimated_price(location,sqft,bath,bhk):

    try: 
        loc_index = __data_columns.index(location.lower())

        x = np.zeros(len(__data_columns))
        x[0] = sqft
        x[1] = bath
        x[2] = bhk
        if loc_index >= 0:
            x[loc_index] = 1    

        return round(__model.predict([x])[0],2)

    except:
        
        return f"Please pass the correct location you passed {location} as a location "


# Loading the pickle and json file to update the variables we initialized above

def load_saved_artifacts():
    
    print("Loading saved artifacts....")
    
    # Making the variables to be seen out of this script

    global __data_columns
    global __locations
    global __model

    # Reading the pickle file and updating the __model variable

    with open('./artifacts/house_price_prediction_model.pickle','rb') as f:
        __model = pickle.load(f)

    # Reading the json file and updating the __data_columns as well as the __locations column

    with open('./artifacts/columns.json','r') as f:
        __data_columns = json.load(f)['data_columns']

        # We slice the __data_columns because upto 3rd column we have
        # total_sqft,bhk and bath
        
        __locations = __data_columns[3:]

    print("Loading saved artifcats done!!!")

def get_location_names():
    return __locations

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    get_location_names()
    print(get_estimated_price('1st Phase JP Nagar',1000, 2, 2))
    print(get_estimated_price('1st Phase JP Nagar',1000, 3, 3))
