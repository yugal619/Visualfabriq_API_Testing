
""" Requests Utilities """
import requests
import time
import logging


class RequestsUtils:

    @staticmethod
    def _request(host, path, method="GET", **kwargs):
        """
        Issues on HTTP request

        Args:
            :param host(str): host part of url e.g. http://127.0.0.12
            :param path(str): path part of url e.g. api/v2/update
            :param method(str, optional): defaults to "GET". GET,POST,PUT,PATCH,DELETE method

        Keyword Args:
            All keyword args supported by requests lib.
            Like:-

            data (str, dict or list, optional): request data as string, dictionary, list or tuple
            json (object, optional): json serialization data sent in body
            headers (dict, optional): dictionary of HTTP header to send with request
            proxies (dict, optional): dictionary mapping protocol to the url of the proxy

        Raises:
            error: HTTP exception if request is not successful after 10 retries

        Returns:
            object: Response object
        """

        url = host + path
        max_reties = kwargs.get("max_retires", 10)

        while max_reties > 0:
            try:
                time.sleep(1)
                logging.info(f"Sending {method} request for {url}, Max retires pending: {max_reties}")
                response = requests.request(method, url, **kwargs)
            except requests.RequestException as error:
                logging.info(f"HTTP exception occurred: {error} ")
                time.sleep(1)
                max_reties -= 1
                if max_reties == 0:
                    raise error
            else:
                logging.info(f"HTTP response code: {response.status_code}")
                return response

    @staticmethod
    def get(host, path, **kwargs):
        """
        Sends an HTTP GET request and returns response

        :param host(str): host part of url e.g. http://127.0.0.12
        :param path(str): path part of url e.g. api/v2/update
        :return: object: Response object
        """
        return RequestsUtils.process_request(host, path, method="GET", **kwargs)

    @staticmethod
    def process_request(host, path, method, **kwargs):
        logging_str = "\n ************************************************************* \n" +\
                      f"Method: {method}" + \
                      f"Host: {host}" + \
                      f"Path: {path}"

        headers = kwargs.get("headers")
        params = kwargs.get("params")
        data = kwargs.get("data")
        fail_on_error = bool(int(kwargs.get("fail_on_error", 1)))

        if "fail_on_error" in kwargs.keys():
            del kwargs['fail_on_error']
        if headers:
            logging_str += f"\ Headers : {str(headers)}"
        if params:
            logging_str += f"\ Params : {str(params)}"
        if data:
            logging_str += f"\ Data : {str(data)}"

        resp_obj = RequestsUtils._request(host, path, method, **kwargs)

        logging_str += f"\n Response \n Headers: {str(resp_obj.headers)}" +\
                        f"\n Status Code : {str(resp_obj.status_code)} " +\
                        f"\n Response Text : {str(resp_obj.text)} " +\
                        "*************************************************************"
        #
        # if resp_obj.status_code < 299:
        #     logging.debug(logging_str)
        # else:
        #     logging.info(logging_str)
        #     if fail_on_error is True:
        #         raise Exception(f"\n API call failed. Need Investigation")
        return resp_obj
