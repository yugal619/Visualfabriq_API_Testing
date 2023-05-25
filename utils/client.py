
from utils.request_util import RequestsUtils


class Client():

    def __init__(self, base_url, header, log):
        self.base_url = base_url
        self.header = header
        self.log = log
        self.log.info("Client Util is initialized")

    def verify_valid_data(self, input, fail_on_error=True):
        uri = '/Prod/next-birthday'
        params = {
            "dateofbirth": input['dateofbirth'],
            "unit": input['unit']
        }
        response = RequestsUtils.get(host=self.base_url, path=uri, headers=self.header, params=params,
                                      fail_on_error=fail_on_error)
        assert response.status_code == 200, f"[FAILURE] Status code is not correct. \n Actual - {response.status_code}" \
                                            f"\nExpected = {200}"
        value = input.get("expected_output")
        assert value in response.json()['message'], f'[FAILURE] Actual output - {response.json()["message"]} \n' \
                                                    f'Expected output - {value}'

    def verify_invalid_data(self, input, fail_on_error=True):
        uri = '/Prod/next-birthday'
        response = RequestsUtils.get(host=self.base_url, path=uri, headers=self.header, params=input,
                                      fail_on_error=fail_on_error)
        assert response.status_code > 299, f'[FAILURE] Actual Status code - {response.status_code} \n' \
                                           f'Expected status code ">299" as input is invalid \n' \
                                           f'Input - {input["params"]}'
