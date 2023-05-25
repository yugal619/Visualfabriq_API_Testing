import pytest
from utils.read_data import inject_test_data


class Test_001_valiadte_time_left_for_dob_api:

    d = inject_test_data("E:\\Visualfabriq_API_Testing\\utils\\data.json")

    @pytest.mark.parametrize("input", d['happy_path'])
    def test_001_for_valid_data(self, input):
        self.clientUtil.verify_valid_data(input)

    @pytest.mark.parametrize("input", d['edge_case_data'])
    def test_002_for_edge_cases(self, input):
        self.clientUtil.verify_valid_data(input)

    @pytest.mark.parametrize("input", d['invalid_data'])
    def test_003_for_invalid_data(self, input):
        self.clientUtil.verify_invalid_data(input)
