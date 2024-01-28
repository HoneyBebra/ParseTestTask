from fake_useragent import UserAgent


class Driver:
    def __init__(self):
        self.headers = {
            'authority': 'www.letu.ru',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'cookie': 'anonymous_user_cart=; anonymous_user_wishlist=; language=ru-RU; pseudo_user_id=pu261880968; rrSession=bd9ad9fab30e4853af0eb605af2e3cd4; ssaid=8b9fd060-bc56-11ee-81f9-07c0c866355f; _gid=GA1.2.26501978.1706279040; tmr_lvid=6b321e16cd615b4fd48a0177f03ec46d; tmr_lvidTS=1706279039628; _gcl_au=1.1.22393348.1706279040; _ym_uid=1706279040406001685; _ym_d=1706279040; iap.uid=e120245115e0462884bc174ce0ce8183; st_uid=3ff068e2f08fe5628d6aa7382dd749f2; mindboxDeviceUUID=594dba06-8949-48ed-b1c6-6f00a6c03acb; directCrm-session=%7B%22deviceGuid%22%3A%22594dba06-8949-48ed-b1c6-6f00a6c03acb%22%7D; uxs_uid=8c46bec0-bc56-11ee-86e9-d3bbb8548bcd; flocktory-uuid=08e4926a-5d4a-4ead-b63e-49c55468873f-7; _gpVisits={"isFirstVisitDomain":true,"idContainer":"10002591"}; _rc_sess=ee2a2bb9-fa5b-4075-8701-1d5dab40c8e8; _rc_uid=9aa9c530204b2a80220481c16f875d4e; hintAddressClarification=true; _ym_isad=1; cityDetected=true; anonymous_user_city=8113; _ga_QLKKCEW68Q=GS1.1.1706359032.2.1.1706370183.0.0.0; anonymous_user_last_viewed=129600401:12100009:129400072:12900020:109600009:118800773:92400039:140601465:67600054:106900152:140601578:81400017:4400075:60100054:63300208:104800719; _ym_visorc=w; _ga_BEJ24GFC22=GS1.1.1706404846.9.1.1706404964.44.0.0; COOKIE-BEARER=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ1MTY2NTIwMTEzNzIiLCJhdXRob3JpdGllcyI6IlJPTEVfQU5PTllNT1VTIiwic2l0ZUlkIjoic3RvcmVNb2JpbGVSVSIsImlhdCI6MTcwNjQwNDk2NCwiZXhwIjoxNzA2NDkxMzY0fQ.SaH64yB-Z6rsImBHTE7WDn8MctSD0fnP1bERjeGwHi7xXddvnhhAzG26nUWse58OEnBcV5PvpaT0ztpNy-us_Q; JSESSIONID=U2PdByna63GBl2D3xrDkHbjgGy8_.prod-wru-a-02; tmr_detect=1%7C1706404965561; __tld__=null; _ga=GA1.1.885850084.1706279037; _ga_DHNLLB7WSD=GS1.2.1706404848.9.1.1706404966.10.0.0; _ga_72YB0DGLLG=GS1.1.1706404848.9.1.1706404968.8.0.0; _ga_0NXH30EL4J=GS1.1.1706404848.9.1.1706404968.0.0.0',
            'referer': 'https://www.letu.ru/product/sesderma-syvorotka-uvlazhnyayushchaya-mandelac/132400959',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'traceparent': '00-1a9edf6270de05c356f300ebe003a3d5-efc7b5e8ff7d085d-01',
            'x-promo-msg': '8CDHp8P8LUWUlktA6uNgTw'
        }
        self.user_agent = UserAgent()
