import requests
from models import StockPrice


class Client:
    def __init__(self, api_token: str) -> None:
        """_summary_

        Args:
            api_token (str): _description_
        """
        self._base_url = "https://api.stockdata.org/v1/data"
        self._api_token = api_token


    def get_stock_prices(
            self,
            symbols: list,
            extended_hours: bool = False,
            key_by_ticker: bool = False):
        """Get prices for US-listed stocks

        Args:
            symbols (list): Specify symbol(s) to return data for
            extended_hours (bool, optional): Include pre and post market data. Defaults to False.
            key_by_ticker (bool, optional): Key each quote by the ticker/symbol.. Defaults to False.

        Returns:
            list(StockPrice): 
        """
        url = f'{self._base_url}/quote'
        response = requests.get(
            url=url,
            params={
                'api_token': self._api_token,
                'symbols': symbols
            }
        )
        for data in response.json()['data']:
            print(data)

        return [StockPrice.from_dict(data) for data in response.json()['data']]
