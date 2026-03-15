import json
import pickle
import numpy as np
import os
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

__location = None
__data_columns = None
__model = None


def get_estimated_price(location, sqft, bhk, bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1 

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk

    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)


def get_location_names():
    return __location


def load_saved_artifacts():
    print("loading saved artifacts... start")

    global __data_columns
    global __location
    global __model

    base_path = os.path.dirname(__file__)  # server directory
    artifacts_path = os.path.join(base_path, "artifacts")

    with open(os.path.join(artifacts_path, "columns.json"), "r") as f:
        __data_columns = json.load(f)['data_columns']
        __location = __data_columns[3:]

    with open(os.path.join(artifacts_path, "bengore_home_price_model.pickle"), "rb") as f:
        __model = pickle.load(f)
    print("loading saved artifacts... done")


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st block jayanagar', 1000, 3, 2))
    print(get_estimated_price('chandapura', 1000, 3, 2))
    print(get_estimated_price('yelenahalli', 1000, 3, 2))