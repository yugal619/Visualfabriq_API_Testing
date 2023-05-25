import os
import pytest
from utils.read_data import inject_test_data


current_directory = os.getcwd()
file = os.path.join(os.path.dirname(current_directory), "utils\data.json")


class Test_001_valiadte_time_left_for_dob_api:

    input_data = inject_test_data(file)

    @pytest.mark.parametrize("input", input_data['happy_path'])
    def test_001_for_valid_data(self, input):
        self.clientUtil.verify_valid_data(input)

    @pytest.mark.parametrize("input", input_data['edge_case_data'])
    def test_002_for_edge_cases(self, input):
        self.clientUtil.verify_valid_data(input)

    @pytest.mark.parametrize("input", input_data['invalid_data'])
    def test_003_for_invalid_data(self, input):
        self.clientUtil.verify_invalid_data(input)
