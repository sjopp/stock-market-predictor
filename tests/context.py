import os
import sys
import json
import pandas as pd
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
test_file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "resources")


def return_json_resource(file_path):
    with open(os.path.join(test_file_path, file_path)) as f:
        return json.load(f)


def return_dataframe_resource(file_path, columns):
    json_data = return_json_resource(file_path)
    return pd.DataFrame(json_data, columns=columns, dtype=np.float64).set_index('date')


import src

