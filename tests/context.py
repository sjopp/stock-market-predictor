import os
import sys
import json
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
test_file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "resources")


def return_json_test_resource(file_path):
    with open(os.path.join(test_file_path, file_path)) as f:
        return json.load(f)


import src
import tests

