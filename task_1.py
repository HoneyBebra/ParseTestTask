import pandas as pd
from datetime import datetime

from utils.letu_drivers.sku_api_driver import SkuApiDriver


def get_sku_ids(urls: list) -> tuple:
    skus_ids = []
    skus_type_ids = []
    for url in urls:
        url_split = url.split('/')
        if 'sku' in url:
            skus_ids.append(url_split[-3])
            skus_type_ids.append(url_split[-1])
        else:
            skus_ids.append(url_split[-1])
            skus_type_ids.append('')

    return skus_ids, skus_type_ids


def main():
    df = pd.read_excel('Задание для Разработчик.xlsx', sheet_name='Задание 1')
    urls = df['Конкурент ссылка'].tolist()
    skus_ids, skus_type_ids = get_sku_ids(urls)

    letu_sku_api_driver = SkuApiDriver()
    prices_without_discount, prices_discount, statuses_in_stock = letu_sku_api_driver.get_sku_data(
        skus_ids, skus_type_ids
    )

    df['Цена до скидки'] = prices_without_discount
    df['Цена со скидкой или по карте лояльности'] = prices_discount
    df['Доступен для заказа (есть остаток)'] = statuses_in_stock
    df['Дата'] = datetime.today().date()
    df.to_excel('./Данные задание 1.xlsx', index=False)


if __name__ == "__main__":
    main()
