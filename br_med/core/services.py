from datetime import date
from http import HTTPStatus

import requests
from django.conf import settings

from br_med.core.exceptions import VATRequestError


class VATService:
    def __init__(self):
        self.base_url = settings.VAT_URL.rstrip("/")
        self.session = requests.Session()

    def request(self, method, endpoint, data=None, query_params=None) -> dict:
        full_url = self.base_url + endpoint
        response = self.session.request(method=method, url=full_url, params=query_params, data=data)
        if response.status_code != HTTPStatus.OK:
            raise VATRequestError(
                f"Erro ao buscar dados no servico VAT | "
                f"Endpoint: {method} {endpoint} {query_params} {data} | "
                f"Response: {response.text}"
            )
        return response.json()

    def post(self, endpoint, data, query_params=None) -> dict:
        method = "POST"
        return self.request(method=method, endpoint=endpoint, data=data, query_params=query_params)

    def get(self, endpoint, query_params=None) -> dict:
        method = "GET"
        return self.request(method=method, endpoint=endpoint, query_params=query_params)

    def currencies(self) -> dict:
        endpoint = "/currencies"
        currencies = self.get(endpoint=endpoint)
        return currencies

    def rates(self, period: date = None) -> dict:
        endpoint = "/rates"
        query_params = {"base": "USD"}
        if period:
            query_params.update({"date": period})
        return self.get(endpoint=endpoint, query_params=query_params)
