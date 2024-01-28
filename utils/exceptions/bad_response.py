class BadResponseCode(Exception):
    def __init__(self, url, code):
        self.message = f'Код ответа от {url} = {code}'
        super().__init__(self.message)
