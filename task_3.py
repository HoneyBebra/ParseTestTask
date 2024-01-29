from utils.letu_drivers.api_driver import ApiDriver
import pandas as pd
from datetime import datetime

from utils.exceptions.bad_response import BadResponseCode


def main():
    api_driver = ApiDriver()

    brands = []
    names = []
    urls = []
    in_stock_statuses = []
    prices_without_discount = []
    prices_discount = []

    i = 0
    while True:
        try:
            data = api_driver.get_data(
                f'https://www.letu.ru/s/api/product/listing/v1/products?N=1dv8be0&Nrpp=50&No={i * 50}&innerPath=mainContent%5B3%5D&resultListPath=%2Fcontent%2FWeb%2FCategories%2FBrowse%20Pages%2FDefault%20Browse%20Page%20-%20DM%20-%20nika&pushSite=storeMobileRU'
            )
        except BadResponseCode as Er:
            print(Er)
            i += 1
            continue

        products = data.products
        if not products:
            break
        for product in products:
            brands.append(product.brandName)
            names.append(product.displayName)
            urls.append(f'https://www.letu.ru/product/{product.sefName}/{product.repositoryId}')
            in_stock_statuses.append('Нет' if product.isOutOfStock else 'Да')
            prices_without_discount.append(product.rawPrice)
            prices_discount.append(product.discountedPrice)
        i += 1

    df = pd.DataFrame({
        'Бренд': brands,
        'Наименование': names,
        'Ссылка': urls,
        'Доступен для заказа (есть остаток)': in_stock_statuses,
        'Цена до скидки': prices_without_discount,
        'Цена со скидкой или по карте лояльности': prices_discount
    })
    df['Дата'] = datetime.today().date()

    df.to_excel('./Данные задание 3.xlsx', index=False)


if __name__ == '__main__':
    main()
