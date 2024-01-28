import requests

from utils.letu_drivers.driver import Driver
from utils.exceptions.bad_response import BadResponseCode
from json_models.sku_model import SkuModel


class SkuApiDriver(Driver):
    def __init__(self):
        super().__init__()
        self.sku_model = SkuModel

        self.url = 'https://www.letu.ru/s/api/product/v2/product-detail/'

        self.prices_without_discount = []
        self.prices_discount = []
        self.statuses_in_stock = []

    def __add_data_to_arrays(
            self, price_without_discount: int | str, price_discount: int | str,
            statuses_in_stock: str
    ) -> None:
        self.prices_without_discount.append(price_without_discount)
        self.prices_discount.append(price_discount)
        self.statuses_in_stock.append(statuses_in_stock)

    def __get_sku_list(self, data) -> list | bool:
        sku_list = data.skuList
        if not sku_list:
            self.__add_data_to_arrays('Товар снят с продажи', 'Товар снят с продажи', 'Товар снят с продажи')
            return False
        return sku_list

    def __get_data_by_id(self, sku_id: str | int):
        self.headers['user-agent'] = self.user_agent.random
        url = self.url + str(sku_id)
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return self.sku_model.model_validate_json(response.text)
        raise BadResponseCode(response.url, response.status_code)

    @staticmethod
    def __get_sku_list_data(sku_list: list, sku_type_id: str | int) -> tuple:
        necessary_sku = dict()
        for sku in sku_list:
            if not sku_type_id or sku.id == str(sku_type_id):
                necessary_sku = sku
                break
            if sku == sku_list[-1]:
                necessary_sku = sku_list[0]

        return (
            necessary_sku.price.listPrice,
            necessary_sku.price.amount,
            'Да' if necessary_sku.isInStock else 'Нет'
        )

    def get_sku_data(self, skus_ids: list, skus_type_ids: list) -> tuple:
        for i in range(len(skus_ids)):
            try:
                data = self.__get_data_by_id(skus_ids[i])
            except BadResponseCode as Er:
                print(Er)
                self.__add_data_to_arrays('', '', '')
                continue

            if not data:
                continue
            sku_list = self.__get_sku_list(data)
            if not sku_list:
                continue

            price_without_discount, price_discount, status_in_stock = self.__get_sku_list_data(
                sku_list, skus_type_ids[i]
            )
            self.__add_data_to_arrays(price_without_discount, price_discount, status_in_stock)

        return self.prices_without_discount, self.prices_discount, self.statuses_in_stock
