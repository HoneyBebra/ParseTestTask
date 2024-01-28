import requests

from utils.letu_drivers.driver import Driver
from utils.exceptions.bad_response import BadResponseCode
from json_models.base_api_model import BaseApiModel


class ApiDriver(Driver):
    def __init__(self):
        super().__init__()

        self.base_api_model = BaseApiModel

    def get_data(self, url: str):
        self.headers['user-agent'] = self.user_agent.random
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return self.base_api_model.model_validate_json(response.text)
        raise BadResponseCode(url, response.status_code)
