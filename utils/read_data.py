import json


def inject_test_data(file):
    """
        Read the content of the JSON file
    """
    with open(file) as f:
        raw_data = json.load(f)
    return raw_data