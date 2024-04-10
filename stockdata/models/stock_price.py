from datetime import datetime
from dataclasses import dataclass, field
from dataclasses_json import config, dataclass_json
from typing import Optional
from dateutil.parser import parse


@staticmethod
def _str_to_timestamp(date_string):
    dt = parse(date_string)
    return dt.timestamp()


@dataclass_json
@dataclass
class StockPrice:
    ticker: str
    name: str
    exchange_short: Optional[str]
    exchange_long: Optional[str]
    mic_code: str
    currency: str
    price: float
    day_high: float
    day_low: float
    day_open: float
    _52_week_high: float = field(metadata=config(field_name='52_week_high'))
    _52_week_low: float = field(metadata=config(field_name='52_week_low'))
    market_cap: Optional[float]
    previous_close_price: float
    previous_close_price_time: datetime = field(metadata=config(
        field_name='previous_close_price_time',
        decoder=_str_to_timestamp,
        encoder=datetime.isoformat
    ))
    day_change: float
    volume: int
    is_extended_hours_price: bool
    last_trade_time: datetime = field(metadata=config(
        field_name='last_trade_time',
        decoder=_str_to_timestamp,
        encoder=datetime.isoformat
    ))