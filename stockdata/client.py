import requests
from models import StockPrice


class Client:
    def __init__(self, api_token: str) -> None:
        """Performs requests from StockData.org

        Args:
            api_token (str): API token provided by StockData.org
        """
        self._base_url = "https://api.stockdata.org/v1/data"
        self._api_token = api_token

    
    def _send_request(self, endpoint: str, symbols: list, **kwargs) -> dict:
        """Sends a GET request

        Args:
            endpoint (str): API endpoint name
            symbols (list): Specify stock symbol(s)

        Returns:
            _type_: dict
        """
        url = f'{self._base_url}/{endpoint}'
        params = {'api_token': self._api_token, 'symbols': symbols}
        params.update(kwargs)
        response = requests.get(
            url=url,
            params=params
        )
        response.raise_for_status()
        return response.json


    def get_stock_prices(self, symbols: list, **kwargs) -> list(StockPrice): # type: ignore
        """Get prices for US-listed stocks

        Args:
            symbols (list): Specify symbol(s) to return data
            **kwargs: Additional request parameters
                - extended_hours (bool, optional): Include pre and post market data. Defaults to False.
                - key_by_ticker (bool, optional): Key each quote by the ticker/symbol.. Defaults to False.

        Returns:
            _type_: list(StockPrice): 
        """
        response_json = self._send_request(symbols=symbols, kwargs=kwargs)
        return [StockPrice.from_dict(data) for data in response_json['data']]
    

    def get_intraday_adjusted(self, symbols: list, **kwargs):
        pass
