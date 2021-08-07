import pytest

from cryptofeed.defines import ASK, BID, KRAKEN
from cryptofeed.exchanges.kraken import Kraken


kraken = Kraken(config='config.yaml')


def test_get_order_book():
    book = kraken.l2_book_sync('BTC-USD')
    assert len(book[BID]) > 0


def test_get_recent_trades():
    trades = list(kraken.trades_sync('BTC-USD'))[0]
    assert len(trades) > 0
    assert trades[0]['feed'] == KRAKEN
    assert trades[0]['symbol'] == 'BTC-USD'


def test_ticker():
    t = kraken.ticker_sync('BTC-USD')
    assert t['symbol'] == 'BTC-USD'
    assert t['feed'] == KRAKEN
    assert BID in t
    assert ASK in t


def test_historical_trades():
    trades = []
    for t in kraken.trades_sync('BTC-USD', start='2021-01-01 00:00:01', end='2021-01-01 00:00:05'):
        trades.extend(t)
    assert len(trades) == 13

    trades = []
    for t in kraken.trades_sync('BTC-USD', start='2021-01-01 00:00:01', end='2021-01-01 01:00:00'):
        trades.extend(t)
    assert len(trades) == 2074


@pytest.mark.skipif(not kraken.key_id or not kraken.key_secret, reason="No api key provided")
def test_get_account_balance():
    balance = kraken.get_account_balance()
    assert balance['error'] == []


@pytest.mark.skipif(not kraken.key_id or not kraken.key_secret, reason="No api key provided")
def test_get_open_orders():
    open_orders = kraken.get_open_orders()
    assert open_orders['error'] == []


@pytest.mark.skipif(not kraken.key_id or not kraken.key_secret, reason="No api key provided")
def test_get_open_orders_trades():
    open_orders = kraken.get_open_orders({'trades': 'true'})
    assert open_orders['error'] == []


@pytest.mark.skipif(not kraken.key_id or not kraken.key_secret, reason="No api key provided")
def test_get_closed_orders():
    closed_orders = kraken.get_closed_orders()
    assert closed_orders['error'] == []


@pytest.mark.skipif(not kraken.key_id or not kraken.key_secret, reason="No api key provided")
def test_get_closed_orders_trades():
    closed_orders = kraken.get_closed_orders({'trades': 'true'})
    assert closed_orders['error'] == []


@pytest.mark.skipif(not kraken.key_id or not kraken.key_secret, reason="No api key provided")
def test_query_orders_info():
    orders_info = kraken.query_orders_info()
    assert orders_info['error'][0] == 'EGeneral:Invalid arguments'

@pytest.mark.skipif(not kraken.key_id or not kraken.key_secret, reason="No api key provided")
def test_get_get_trades_history():
    trades_history = kraken.get_trades_history()
    assert trades_history['error'] == []


@pytest.mark.skipif(not kraken.key_id or not kraken.key_secret, reason="No api key provided")
def test_get_get_trades_history_params():
    trades_history = kraken.get_trades_history({'trades': 'true', 'type': 'any position'})
    assert trades_history['error'] == []


@pytest.mark.skipif(not kraken.key_id or not kraken.key_secret, reason="No api key provided")
def test_get_query_trades_info():
    trades_info = kraken.query_trades_info({})
    assert trades_info['error'][0] == 'EGeneral:Invalid arguments'


@pytest.mark.skipif(not kraken.key_id or not kraken.key_secret, reason="No api key provided")
def test_get_ledgers_info():
    ledgers_info = kraken.get_ledgers_info()
    assert ledgers_info['error'] == []


@pytest.mark.skipif(not kraken.key_id or not kraken.key_secret, reason="No api key provided")
def test_get_trade_volume():
    trade_volume = kraken.get_trade_volume()
    assert trade_volume['result']['currency'] == 'ZUSD'

@pytest.mark.skipif(not kraken.key_id or not kraken.key_secret, reason="No api key provided")
def test_trade_history():
    trade_history = kraken.trade_history()
    # for trade in trade_history:
    #     for k, v in trade.items():
    #         print(f"{k} => {v}")
    assert len(trade_history) != 0

@pytest.mark.skipif(not kraken.key_id or not kraken.key_secret, reason="No api key provided")
def test_ledger():
    ledger = kraken.ledger()
    # for trade in trade_history:
    #     for k, v in trade.items():
    #         print(f"{k} => {v}")
    assert len(ledger) != 0