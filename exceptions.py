import json

import requests

from config import keys


class APIException(Exception):
    pass


class Converter:
    @staticmethod
    def get_price(base: str, quote: str, amount: str):

        # quote_ticker, base_ticker = keys[quote], keys[base]
        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Нет такой валюты — {base}. Список доступных валют тут: /values.')
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Нет такой валюты — {quote}. Список доступных валют тут: /values.')
        try:
            amount = float(amount)
        except ValueError:
            raise APIException('Количество валюты должно быть числом!!')

        if quote == base:
            raise APIException('Вы ввели одинаковые валюты')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base_ticker}&tsyms={quote_ticker}')
        exchange_rate = float(json.loads(r.content)[quote_ticker])
        total_amount = exchange_rate * amount

        return total_amount
