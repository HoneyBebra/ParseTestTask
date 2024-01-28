import unittest

from utils.letu_drivers.api_driver import ApiDriver
from utils.letu_drivers.sku_api_driver import SkuApiDriver


class TestApi(unittest.TestCase):
    def setUp(self):
        self.skus_ids = ['104800719', '118800773']
        self.skus_type_ids = ['119700898', '134101037']

        self.products_url = f'https://www.letu.ru/s/api/product/listing/v1/products?N=1vn20zz&Nrpp=50&No=0&innerPath=mainContent%5B2%5D&resultListPath=%2Fcontent%2FWeb%2FBrands%2FPages%2FBrand%20Page&pushSite=storeMobileRU'

    def test_api_driver(self):
        api_driver = ApiDriver()
        self.assertEqual(
            str(type(api_driver.get_data(self.products_url))),
            "<class 'json_models.base_api_model.BaseApiModel'>"
        )

    def test_sku_api_driver(self):
        sku_api_driver = SkuApiDriver()
        self.assertNotEqual(
            sku_api_driver.get_sku_data(self.skus_ids, self.skus_type_ids),
            (['', ''], ['', ''], ['', ''])
        )
