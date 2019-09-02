# -*- coding: utf-8 -*-

# PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
# https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

from ccxt.base.exchange import Exchange
import hashlib
from ccxt.base.errors import ExchangeError
from ccxt.base.errors import AuthenticationError
from ccxt.base.errors import InsufficientFunds
from ccxt.base.errors import InvalidOrder
from ccxt.base.errors import InvalidNonce


class bitbay (Exchange):

    def describe(self):
        return self.deep_extend(super(bitbay, self).describe(), {
            'id': 'bitbay',
            'name': 'BitBay',
            'countries': ['MT', 'EU'],  # Malta
            'rateLimit': 1000,
            'has': {
                'CORS': True,
                'withdraw': True,
                'fetchMyTrades': True,
            },
            'urls': {
                'referral': 'https://auth.bitbay.net/ref/jHlbB4mIkdS1',
                'logo': 'https://user-images.githubusercontent.com/1294454/27766132-978a7bd8-5ece-11e7-9540-bc96d1e9bbb8.jpg',
                'www': 'https://bitbay.net',
                'api': {
                    'public': 'https://bitbay.net/API/Public',
                    'private': 'https://bitbay.net/API/Trading/tradingApi.php',
                    'v1_01Public': 'https://api.bitbay.net/rest',
                    'v1_01Private': 'https://api.bitbay.net/rest',
                },
                'doc': [
                    'https://bitbay.net/public-api',
                    'https://bitbay.net/en/private-api',
                    'https://bitbay.net/account/tab-api',
                    'https://github.com/BitBayNet/API',
                    'https://docs.bitbay.net/v1.0.1-en/reference',
                ],
                'fees': 'https://bitbay.net/en/fees',
            },
            'api': {
                'public': {
                    'get': [
                        '{id}/all',
                        '{id}/market',
                        '{id}/orderbook',
                        '{id}/ticker',
                        '{id}/trades',
                    ],
                },
                'private': {
                    'post': [
                        'info',
                        'trade',
                        'cancel',
                        'orderbook',
                        'orders',
                        'transfer',
                        'withdraw',
                        'history',
                        'transactions',
                    ],
                },
                'v1_01Public': {
                    'get': [
                        'trading/ticker',
                        'trading/ticker/{symbol}',
                        'trading/stats',
                        'trading/orderbook/{symbol}',
                        'trading/transactions/{symbol}',
                        'trading/candle/history/{symbol}/{resolution}',
                    ],
                },
                'v1_01Private': {
                    'get': [
                        'payments/withdrawal/{detailId}',
                        'payments/deposit/{detailId}',
                        'trading/offer',
                        'trading/config/{symbol}',
                        'trading/history/transactions',
                        'balances/BITBAY/history',
                        'balances/BITBAY/balance',
                        'fiat_cantor/rate/{baseId}/{quoteId}',
                        'fiat_cantor/history',
                    ],
                    'post': [
                        'trading/offer/{symbol}',
                        'trading/config/{symbol}',
                        'balances/BITBAY/balance',
                        'balances/BITBAY/balance/transfer/{source}/{destination}',
                        'fiat_cantor/exchange',
                    ],
                    'delete': [
                        'trading/offer/{symbol}/{id}/{side}/{price}',
                    ],
                    'put': [
                        'balances/BITBAY/balance/{id}',
                    ],
                },
            },
            'fees': {
                'trading': {
                    'maker': 0.3 / 100,
                    'taker': 0.0043,
                },
                'funding': {
                    'withdraw': {
                        'BTC': 0.0009,
                        'LTC': 0.005,
                        'ETH': 0.00126,
                        'LSK': 0.2,
                        'BCH': 0.0006,
                        'GAME': 0.005,
                        'DASH': 0.001,
                        'BTG': 0.0008,
                        'PLN': 4,
                        'EUR': 1.5,
                    },
                },
            },
            'exceptions': {
                '400': ExchangeError,  # At least one parameter wasn't set
                '401': InvalidOrder,  # Invalid order type
                '402': InvalidOrder,  # No orders with specified currencies
                '403': InvalidOrder,  # Invalid payment currency name
                '404': InvalidOrder,  # Error. Wrong transaction type
                '405': InvalidOrder,  # Order with self id doesn't exist
                '406': InsufficientFunds,  # No enough money or crypto
                # code 407 not specified are not specified in their docs
                '408': InvalidOrder,  # Invalid currency name
                '501': AuthenticationError,  # Invalid public key
                '502': AuthenticationError,  # Invalid sign
                '503': InvalidNonce,  # Invalid moment parameter. Request time doesn't match current server time
                '504': ExchangeError,  # Invalid method
                '505': AuthenticationError,  # Key has no permission for self action
                '506': AuthenticationError,  # Account locked. Please contact with customer service
                # codes 507 and 508 are not specified in their docs
                '509': ExchangeError,  # The BIC/SWIFT is required for self currency
                '510': ExchangeError,  # Invalid market name
            },
        })

    def fetch_markets(self, params={}):
        response = self.v1_01PublicGetTradingTicker(params)
        #
        #     {
        #         status: 'Ok',
        #         items: {
        #             'BSV-USD': {
        #                 market: {
        #                     code: 'BSV-USD',
        #                     first: {currency: 'BSV', minOffer: '0.00035', scale: 8},
        #                     second: {currency: 'USD', minOffer: '5', scale: 2}
        #                 },
        #                 time: '1557569762154',
        #                 highestBid: '52.31',
        #                 lowestAsk: '62.99',
        #                 rate: '63',
        #                 previousRate: '51.21',
        #             },
        #         },
        #     }
        #
        result = []
        items = self.safe_value(response, 'items')
        keys = list(items.keys())
        for i in range(0, len(keys)):
            key = keys[i]
            item = items[key]
            market = self.safe_value(item, 'market', {})
            first = self.safe_value(market, 'first', {})
            second = self.safe_value(market, 'second', {})
            baseId = self.safe_string(first, 'currency')
            quoteId = self.safe_string(second, 'currency')
            id = baseId + quoteId
            base = self.safe_currency_code(baseId)
            quote = self.safe_currency_code(quoteId)
            symbol = base + '/' + quote
            precision = {
                'amount': self.safe_integer(first, 'scale'),
                'price': self.safe_integer(second, 'scale'),
            }
            # todo: check that the limits have ben interpreted correctly
            # todo: parse the fees page
            result.append({
                'id': id,
                'symbol': symbol,
                'base': base,
                'quote': quote,
                'baseId': baseId,
                'quoteId': quoteId,
                'precision': precision,
                'active': None,
                'fee': None,
                'limits': {
                    'amount': {
                        'min': self.safe_float(first, 'minOffer'),
                        'max': None,
                    },
                    'price': {
                        'min': None,
                        'max': None,
                    },
                    'cost': {
                        'min': self.safe_float(second, 'minOffer'),
                        'max': None,
                    },
                },
                'info': item,
            })
        return result

    def fetch_my_trades(self, symbol=None, since=None, limit=None, params={}):
        self.load_markets()
        markets = [self.market_id(symbol)] if symbol else []
        request = {
            'markets': markets,
        }
        response = self.v1_01PrivateGetTradingHistoryTransactions(self.extend({'query': self.json(request)}, params))
        #
        #     {
        #         status: 'Ok',
        #         totalRows: '67',
        #         items: [
        #             {
        #                 id: 'b54659a0-51b5-42a0-80eb-2ac5357ccee2',
        #                 market: 'BTC-EUR',
        #                 time: '1541697096247',
        #                 amount: '0.00003',
        #                 rate: '4341.44',
        #                 initializedBy: 'Sell',
        #                 wasTaker: False,
        #                 userAction: 'Buy',
        #                 offerId: 'bd19804a-6f89-4a69-adb8-eb078900d006',
        #                 commissionValue: null
        #             },
        #         ]
        #     }
        #
        items = self.safe_value(response, 'items')
        result = self.parse_trades(items, None, since, limit)
        if symbol is None:
            return result
        return self.filter_by_symbol(result, symbol)

    def fetch_balance(self, params={}):
        self.load_markets()
        response = self.privatePostInfo(params)
        balances = self.safe_value(response, 'balances')
        if balances is None:
            raise ExchangeError(self.id + ' empty balance response ' + self.json(response))
        result = {'info': response}
        codes = list(self.currencies.keys())
        for i in range(0, len(codes)):
            code = codes[i]
            # rewrite with safeCurrencyCode, traverse by currency ids
            currencyId = self.currencyId(code)
            balance = self.safe_value(balances, currencyId)
            if balance is not None:
                account = self.account()
                account['free'] = self.safe_float(balance, 'available')
                account['used'] = self.safe_float(balance, 'locked')
                result[code] = account
        return self.parse_balance(result)

    def fetch_order_book(self, symbol, limit=None, params={}):
        self.load_markets()
        request = {
            'id': self.market_id(symbol),
        }
        orderbook = self.publicGetIdOrderbook(self.extend(request, params))
        return self.parse_order_book(orderbook)

    def fetch_ticker(self, symbol, params={}):
        self.load_markets()
        request = {
            'id': self.market_id(symbol),
        }
        ticker = self.publicGetIdTicker(self.extend(request, params))
        timestamp = self.milliseconds()
        baseVolume = self.safe_float(ticker, 'volume')
        vwap = self.safe_float(ticker, 'vwap')
        quoteVolume = None
        if baseVolume is not None and vwap is not None:
            quoteVolume = baseVolume * vwap
        last = self.safe_float(ticker, 'last')
        return {
            'symbol': symbol,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'high': self.safe_float(ticker, 'max'),
            'low': self.safe_float(ticker, 'min'),
            'bid': self.safe_float(ticker, 'bid'),
            'bidVolume': None,
            'ask': self.safe_float(ticker, 'ask'),
            'askVolume': None,
            'vwap': vwap,
            'open': None,
            'close': last,
            'last': last,
            'previousClose': None,
            'change': None,
            'percentage': None,
            'average': self.safe_float(ticker, 'average'),
            'baseVolume': baseVolume,
            'quoteVolume': quoteVolume,
            'info': ticker,
        }

    def fetch_ledger(self, code=None, since=None, limit=None, params={}):
        balanceCurrencies = []
        if code is not None:
            currency = self.currency(code)
            balanceCurrencies.append(currency['id'])
        request = {
            'balanceCurrencies': balanceCurrencies,
        }
        if since is not None:
            request['fromTime'] = since
        if limit is not None:
            request['limit'] = limit
        request = self.extend(request, params)
        response = self.v1_01PrivateGetBalancesBITBAYHistory({'query': self.json(request)})
        items = response['items']
        return self.parse_ledger(items, None, since, limit)

    def parse_ledger_entry(self, item, currency=None):
        #
        #    FUNDS_MIGRATION
        #    {
        #      "historyId": "84ea7a29-7da5-4de5-b0c0-871e83cad765",
        #      "balance": {
        #        "id": "821ec166-cb88-4521-916c-f4eb44db98df",
        #        "currency": "LTC",
        #        "type": "CRYPTO",
        #        "userId": "a34d361d-7bad-49c1-888e-62473b75d877",
        #        "name": "LTC"
        #      },
        #      "detailId": null,
        #      "time": 1506128252968,
        #      "type": "FUNDS_MIGRATION",
        #      "value": 0.0009957,
        #      "fundsBefore": {"total": 0, "available": 0, "locked": 0},
        #      "fundsAfter": {"total": 0.0009957, "available": 0.0009957, "locked": 0},
        #      "change": {"total": 0.0009957, "available": 0.0009957, "locked": 0}
        #    }
        #
        #    CREATE_BALANCE
        #    {
        #      "historyId": "d0fabd8d-9107-4b5e-b9a6-3cab8af70d49",
        #      "balance": {
        #        "id": "653ffcf2-3037-4ebe-8e13-d5ea1a01d60d",
        #        "currency": "BTG",
        #        "type": "CRYPTO",
        #        "userId": "a34d361d-7bad-49c1-888e-62473b75d877",
        #        "name": "BTG"
        #      },
        #      "detailId": null,
        #      "time": 1508895244751,
        #      "type": "CREATE_BALANCE",
        #      "value": 0,
        #      "fundsBefore": {"total": null, "available": null, "locked": null},
        #      "fundsAfter": {"total": 0, "available": 0, "locked": 0},
        #      "change": {"total": 0, "available": 0, "locked": 0}
        #    }
        #
        #    BITCOIN_GOLD_FORK
        #    {
        #      "historyId": "2b4d52d3-611c-473d-b92c-8a8d87a24e41",
        #      "balance": {
        #        "id": "653ffcf2-3037-4ebe-8e13-d5ea1a01d60d",
        #        "currency": "BTG",
        #        "type": "CRYPTO",
        #        "userId": "a34d361d-7bad-49c1-888e-62473b75d877",
        #        "name": "BTG"
        #      },
        #      "detailId": null,
        #      "time": 1508895244778,
        #      "type": "BITCOIN_GOLD_FORK",
        #      "value": 0.00453512,
        #      "fundsBefore": {"total": 0, "available": 0, "locked": 0},
        #      "fundsAfter": {"total": 0.00453512, "available": 0.00453512, "locked": 0},
        #      "change": {"total": 0.00453512, "available": 0.00453512, "locked": 0}
        #    }
        #
        #    ADD_FUNDS
        #    {
        #      "historyId": "3158236d-dae5-4a5d-81af-c1fa4af340fb",
        #      "balance": {
        #        "id": "3a7e7a1e-0324-49d5-8f59-298505ebd6c7",
        #        "currency": "BTC",
        #        "type": "CRYPTO",
        #        "userId": "a34d361d-7bad-49c1-888e-62473b75d877",
        #        "name": "BTC"
        #      },
        #      "detailId": "8e83a960-e737-4380-b8bb-259d6e236faa",
        #      "time": 1520631178816,
        #      "type": "ADD_FUNDS",
        #      "value": 0.628405,
        #      "fundsBefore": {"total": 0.00453512, "available": 0.00453512, "locked": 0},
        #      "fundsAfter": {"total": 0.63294012, "available": 0.63294012, "locked": 0},
        #      "change": {"total": 0.628405, "available": 0.628405, "locked": 0}
        #    }
        #
        #    TRANSACTION_PRE_LOCKING
        #    {
        #      "historyId": "e7d19e0f-03b3-46a8-bc72-dde72cc24ead",
        #      "balance": {
        #        "id": "3a7e7a1e-0324-49d5-8f59-298505ebd6c7",
        #        "currency": "BTC",
        #        "type": "CRYPTO",
        #        "userId": "a34d361d-7bad-49c1-888e-62473b75d877",
        #        "name": "BTC"
        #      },
        #      "detailId": null,
        #      "time": 1520706403868,
        #      "type": "TRANSACTION_PRE_LOCKING",
        #      "value": -0.1,
        #      "fundsBefore": {"total": 0.63294012, "available": 0.63294012, "locked": 0},
        #      "fundsAfter": {"total": 0.63294012, "available": 0.53294012, "locked": 0.1},
        #      "change": {"total": 0, "available": -0.1, "locked": 0.1}
        #    }
        #
        #    TRANSACTION_POST_OUTCOME
        #    {
        #      "historyId": "c4010825-231d-4a9c-8e46-37cde1f7b63c",
        #      "balance": {
        #        "id": "3a7e7a1e-0324-49d5-8f59-298505ebd6c7",
        #        "currency": "BTC",
        #        "type": "CRYPTO",
        #        "userId": "a34d361d-7bad-49c1-888e-62473b75d877",
        #        "name": "BTC"
        #      },
        #      "detailId": "bf2876bc-b545-4503-96c8-ef4de8233876",
        #      "time": 1520706404032,
        #      "type": "TRANSACTION_POST_OUTCOME",
        #      "value": -0.01771415,
        #      "fundsBefore": {"total": 0.63294012, "available": 0.53294012, "locked": 0.1},
        #      "fundsAfter": {"total": 0.61522597, "available": 0.53294012, "locked": 0.08228585},
        #      "change": {"total": -0.01771415, "available": 0, "locked": -0.01771415}
        #    }
        #
        #    TRANSACTION_POST_INCOME
        #    {
        #      "historyId": "7f18b7af-b676-4125-84fd-042e683046f6",
        #      "balance": {
        #        "id": "ab43023b-4079-414c-b340-056e3430a3af",
        #        "currency": "EUR",
        #        "type": "FIAT",
        #        "userId": "a34d361d-7bad-49c1-888e-62473b75d877",
        #        "name": "EUR"
        #      },
        #      "detailId": "f5fcb274-0cc7-4385-b2d3-bae2756e701f",
        #      "time": 1520706404035,
        #      "type": "TRANSACTION_POST_INCOME",
        #      "value": 628.78,
        #      "fundsBefore": {"total": 0, "available": 0, "locked": 0},
        #      "fundsAfter": {"total": 628.78, "available": 628.78, "locked": 0},
        #      "change": {"total": 628.78, "available": 628.78, "locked": 0}
        #    }
        #
        #    TRANSACTION_COMMISSION_OUTCOME
        #    {
        #      "historyId": "843177fa-61bc-4cbf-8be5-b029d856c93b",
        #      "balance": {
        #        "id": "ab43023b-4079-414c-b340-056e3430a3af",
        #        "currency": "EUR",
        #        "type": "FIAT",
        #        "userId": "a34d361d-7bad-49c1-888e-62473b75d877",
        #        "name": "EUR"
        #      },
        #      "detailId": "f5fcb274-0cc7-4385-b2d3-bae2756e701f",
        #      "time": 1520706404050,
        #      "type": "TRANSACTION_COMMISSION_OUTCOME",
        #      "value": -2.71,
        #      "fundsBefore": {"total": 766.06, "available": 766.06, "locked": 0},
        #      "fundsAfter": {"total": 763.35,"available": 763.35, "locked": 0},
        #      "change": {"total": -2.71, "available": -2.71, "locked": 0}
        #    }
        #
        #    TRANSACTION_OFFER_COMPLETED_RETURN
        #    {
        #      "historyId": "cac69b04-c518-4dc5-9d86-e76e91f2e1d2",
        #      "balance": {
        #        "id": "3a7e7a1e-0324-49d5-8f59-298505ebd6c7",
        #        "currency": "BTC",
        #        "type": "CRYPTO",
        #        "userId": "a34d361d-7bad-49c1-888e-62473b75d877",
        #        "name": "BTC"
        #      },
        #      "detailId": null,
        #      "time": 1520714886425,
        #      "type": "TRANSACTION_OFFER_COMPLETED_RETURN",
        #      "value": 0.00000196,
        #      "fundsBefore": {"total": 0.00941208, "available": 0.00941012, "locked": 0.00000196},
        #      "fundsAfter": {"total": 0.00941208, "available": 0.00941208, "locked": 0},
        #      "change": {"total": 0, "available": 0.00000196, "locked": -0.00000196}
        #    }
        #
        #    WITHDRAWAL_LOCK_FUNDS
        #    {
        #      "historyId": "03de2271-66ab-4960-a786-87ab9551fc14",
        #      "balance": {
        #        "id": "3a7e7a1e-0324-49d5-8f59-298505ebd6c7",
        #        "currency": "BTC",
        #        "type": "CRYPTO",
        #        "userId": "a34d361d-7bad-49c1-888e-62473b75d877",
        #        "name": "BTC"
        #      },
        #      "detailId": "6ad3dc72-1d6d-4ec2-8436-ca43f85a38a6",
        #      "time": 1522245654481,
        #      "type": "WITHDRAWAL_LOCK_FUNDS",
        #      "value": -0.8,
        #      "fundsBefore": {"total": 0.8, "available": 0.8, "locked": 0},
        #      "fundsAfter": {"total": 0.8, "available": 0, "locked": 0.8},
        #      "change": {"total": 0, "available": -0.8, "locked": 0.8}
        #    }
        #
        #    WITHDRAWAL_SUBTRACT_FUNDS
        #    {
        #      "historyId": "b0308c89-5288-438d-a306-c6448b1a266d",
        #      "balance": {
        #        "id": "3a7e7a1e-0324-49d5-8f59-298505ebd6c7",
        #        "currency": "BTC",
        #        "type": "CRYPTO",
        #        "userId": "a34d361d-7bad-49c1-888e-62473b75d877",
        #        "name": "BTC"
        #      },
        #      "detailId": "6ad3dc72-1d6d-4ec2-8436-ca43f85a38a6",
        #      "time": 1522246526186,
        #      "type": "WITHDRAWAL_SUBTRACT_FUNDS",
        #      "value": -0.8,
        #      "fundsBefore": {"total": 0.8, "available": 0, "locked": 0.8},
        #      "fundsAfter": {"total": 0, "available": 0, "locked": 0},
        #      "change": {"total": -0.8, "available": 0, "locked": -0.8}
        #    }
        #
        #    TRANSACTION_OFFER_ABORTED_RETURN
        #    {
        #      "historyId": "b1a3c075-d403-4e05-8f32-40512cdd88c0",
        #      "balance": {
        #        "id": "3a7e7a1e-0324-49d5-8f59-298505ebd6c7",
        #        "currency": "BTC",
        #        "type": "CRYPTO",
        #        "userId": "a34d361d-7bad-49c1-888e-62473b75d877",
        #        "name": "BTC"
        #      },
        #      "detailId": null,
        #      "time": 1522512298662,
        #      "type": "TRANSACTION_OFFER_ABORTED_RETURN",
        #      "value": 0.0564931,
        #      "fundsBefore": {"total": 0.44951311, "available": 0.39302001, "locked": 0.0564931},
        #      "fundsAfter": {"total": 0.44951311, "available": 0.44951311, "locked": 0},
        #      "change": {"total": 0, "available": 0.0564931, "locked": -0.0564931}
        #    }
        #
        #    WITHDRAWAL_UNLOCK_FUNDS
        #    {
        #      "historyId": "0ed569a2-c330-482e-bb89-4cb553fb5b11",
        #      "balance": {
        #        "id": "3a7e7a1e-0324-49d5-8f59-298505ebd6c7",
        #        "currency": "BTC",
        #        "type": "CRYPTO",
        #        "userId": "a34d361d-7bad-49c1-888e-62473b75d877",
        #        "name": "BTC"
        #      },
        #      "detailId": "0c7be256-c336-4111-bee7-4eb22e339700",
        #      "time": 1527866360785,
        #      "type": "WITHDRAWAL_UNLOCK_FUNDS",
        #      "value": 0.05045,
        #      "fundsBefore": {"total": 0.86001578, "available": 0.80956578, "locked": 0.05045},
        #      "fundsAfter": {"total": 0.86001578, "available": 0.86001578, "locked": 0},
        #      "change": {"total": 0, "available": 0.05045, "locked": -0.05045}
        #    }
        #
        #    TRANSACTION_COMMISSION_RETURN
        #    {
        #      "historyId": "07c89c27-46f1-4d7a-8518-b73798bf168a",
        #      "balance": {
        #        "id": "ab43023b-4079-414c-b340-056e3430a3af",
        #        "currency": "EUR",
        #        "type": "FIAT",
        #        "userId": "a34d361d-7bad-49c1-888e-62473b75d877",
        #        "name": "EUR"
        #      },
        #      "detailId": null,
        #      "time": 1528304043063,
        #      "type": "TRANSACTION_COMMISSION_RETURN",
        #      "value": 0.6,
        #      "fundsBefore": {"total": 0, "available": 0, "locked": 0},
        #      "fundsAfter": {"total": 0.6, "available": 0.6, "locked": 0},
        #      "change": {"total": 0.6, "available": 0.6, "locked": 0}
        #    }
        #
        timestamp = self.safe_integer(item, 'time')
        balance = self.safe_value(item, 'balance', {})
        currencyId = self.safe_string(balance, 'currency')
        code = self.safe_currency_code(currencyId)
        change = self.safe_value(item, 'change', {})
        amount = self.safe_float(change, 'total')
        direction = 'in'
        if amount < 0:
            direction = 'out'
            amount = -amount
        id = self.safe_string(item, 'historyId')
        # there are 2 undocumented api calls: (v1_01PrivateGetPaymentsDepositDetailId and v1_01PrivateGetPaymentsWithdrawalDetailId)
        # that can be used to enrich the transfers with txid, address etc(you need to use info.detailId as a parameter)
        referenceId = self.safe_string(item, 'detailId')
        type = self.parse_ledger_entry_type(self.safe_string(item, 'type'))
        fundsBefore = self.safe_value(item, 'fundsBefore', {})
        before = self.safe_float(fundsBefore, 'total')
        fundsAfter = self.safe_value(item, 'fundsAfter', {})
        after = self.safe_float(fundsAfter, 'total')
        return {
            'info': item,
            'id': id,
            'direction': direction,
            'account': None,
            'referenceId': referenceId,
            'referenceAccount': None,
            'type': type,
            'currency': code,
            'amount': amount,
            'before': before,
            'after': after,
            'status': 'ok',
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'fee': None,
        }

    def parse_ledger_entry_type(self, type):
        types = {
            'ADD_FUNDS': 'transaction',
            'BITCOIN_GOLD_FORK': 'transaction',
            'CREATE_BALANCE': 'transaction',
            'FUNDS_MIGRATION': 'transaction',
            'WITHDRAWAL_LOCK_FUNDS': 'transaction',
            'WITHDRAWAL_SUBTRACT_FUNDS': 'transaction',
            'WITHDRAWAL_UNLOCK_FUNDS': 'transaction',
            'TRANSACTION_COMMISSION_OUTCOME': 'fee',
            'TRANSACTION_COMMISSION_RETURN': 'fee',
            'TRANSACTION_OFFER_ABORTED_RETURN': 'trade',
            'TRANSACTION_OFFER_COMPLETED_RETURN': 'trade',
            'TRANSACTION_POST_INCOME': 'trade',
            'TRANSACTION_POST_OUTCOME': 'trade',
            'TRANSACTION_PRE_LOCKING': 'trade',
        }
        return self.safe_string(types, type, type)

    def parse_trade(self, trade, market):
        if 'tid' in trade:
            return self.parse_public_trade(trade, market)
        else:
            return self.parse_my_trade(trade, market)

    def parse_my_trade(self, trade, market=None):
        #
        #     {
        #         amount: "0.29285199",
        #         commissionValue: "0.00125927",
        #         id: "11c8203a-a267-11e9-b698-0242ac110007",
        #         initializedBy: "Buy",
        #         market: "ETH-EUR",
        #         offerId: "11c82038-a267-11e9-b698-0242ac110007",
        #         rate: "277",
        #         time: "1562689917517",
        #         userAction: "Buy",
        #         wasTaker: True,
        #     }
        #
        timestamp = self.safe_integer(trade, 'time')
        userAction = self.safe_string(trade, 'userAction')
        side = 'buy' if (userAction == 'Buy') else 'sell'
        wasTaker = self.safe_value(trade, 'wasTaker')
        takerOrMaker = 'taker' if wasTaker else 'maker'
        price = self.safe_float(trade, 'rate')
        amount = self.safe_float(trade, 'amount')
        cost = None
        if amount is not None:
            if price is not None:
                cost = price * amount
        feeCost = self.safe_float(trade, 'commissionValue')
        marketId = self.safe_string(trade, 'market')
        base = None
        symbol = None
        if marketId is not None:
            if marketId in self.markets_by_id:
                market = self.markets_by_id[marketId]
                symbol = market['symbol']
                base = market['base']
            else:
                baseId, quoteId = marketId.split('-')
                base = self.safe_currency_code(baseId)
                quote = self.safe_currency_code(quoteId)
                symbol = base + '/' + quote
        if market is not None:
            if symbol is None:
                symbol = market['symbol']
            if base is None:
                base = market['base']
        fee = None
        if feeCost is not None:
            fee = {
                'currency': base,
                'cost': feeCost,
            }
        order = self.safe_string(trade, 'offerId')
        # todo: check self logic
        type = 'limit' if order else 'market'
        return {
            'id': self.safe_string(trade, 'id'),
            'order': order,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'symbol': symbol,
            'type': type,
            'side': side,
            'price': price,
            'amount': amount,
            'cost': cost,
            'takerOrMaker': takerOrMaker,
            'fee': fee,
            'info': trade,
        }

    def parse_public_trade(self, trade, market=None):
        #
        #     {
        #         "date":1459608665,
        #         "price":0.02722571,
        #         "type":"sell",
        #         "amount":1.08112001,
        #         "tid":"0"
        #     }
        #
        timestamp = self.safe_timestamp(trade, 'date')
        id = self.safe_string(trade, 'tid')
        type = None
        side = self.safe_string(trade, 'type')
        price = self.safe_float(trade, 'price')
        amount = self.safe_float(trade, 'amount')
        cost = None
        if amount is not None:
            if price is not None:
                cost = price * amount
        symbol = None
        if market is not None:
            symbol = market['symbol']
        return {
            'id': id,
            'info': trade,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'symbol': symbol,
            'type': type,
            'side': side,
            'order': None,
            'takerOrMaker': None,
            'price': price,
            'amount': amount,
            'cost': cost,
            'fee': None,
        }

    def fetch_trades(self, symbol, since=None, limit=None, params={}):
        self.load_markets()
        market = self.market(symbol)
        request = {
            'id': market['id'],
        }
        response = self.publicGetIdTrades(self.extend(request, params))
        #
        #     [
        #         {
        #             "date":1459608665,
        #             "price":0.02722571,
        #             "type":"sell",
        #             "amount":1.08112001,
        #             "tid":"0"
        #         },
        #         {
        #             "date":1459698930,
        #             "price":0.029,
        #             "type":"buy",
        #             "amount":0.444188,
        #             "tid":"1"
        #         },
        #         {
        #             "date":1459726670,
        #             "price":0.029,
        #             "type":"buy",
        #             "amount":0.25459599,
        #             "tid":"2"
        #         }
        #     ]
        #
        return self.parse_trades(response, market, since, limit)

    def create_order(self, symbol, type, side, amount, price=None, params={}):
        self.load_markets()
        if type != 'limit':
            raise ExchangeError(self.id + ' allows limit orders only')
        market = self.market(symbol)
        request = {
            'type': side,
            'currency': market['baseId'],
            'amount': amount,
            'payment_currency': market['quoteId'],
            'rate': price,
        }
        return self.privatePostTrade(self.extend(request, params))

    def cancel_order(self, id, symbol=None, params={}):
        request = {
            'id': id,
        }
        return self.privatePostCancel(self.extend(request, params))

    def is_fiat(self, currency):
        fiatCurrencies = {
            'USD': True,
            'EUR': True,
            'PLN': True,
        }
        return self.safe_value(fiatCurrencies, currency, False)

    def withdraw(self, code, amount, address, tag=None, params={}):
        self.check_address(address)
        self.load_markets()
        method = None
        currency = self.currency(code)
        request = {
            'currency': currency['id'],
            'quantity': amount,
        }
        if self.is_fiat(code):
            method = 'privatePostWithdraw'
            # request['account'] = params['account']  # they demand an account number
            # request['express'] = params['express']  # whatever it means, they don't explain
            # request['bic'] = ''
        else:
            method = 'privatePostTransfer'
            if tag is not None:
                address += '?dt=' + str(tag)
            request['address'] = address
        response = getattr(self, method)(self.extend(request, params))
        return {
            'info': response,
            'id': None,
        }

    def sign(self, path, api='public', method='GET', params={}, headers=None, body=None):
        url = self.urls['api'][api]
        if api == 'public':
            query = self.omit(params, self.extract_params(path))
            url += '/' + self.implode_params(path, params) + '.json'
            if query:
                url += '?' + self.urlencode(query)
        elif api == 'v1_01Public':
            query = self.omit(params, self.extract_params(path))
            url += '/' + self.implode_params(path, params)
            if query:
                url += '?' + self.urlencode(query)
        elif api == 'v1_01Private':
            self.check_required_credentials()
            query = self.omit(params, self.extract_params(path))
            url += '/' + self.implode_params(path, params)
            if query:
                url += '?' + self.urlencode(query)
            nonce = self.milliseconds()
            payload = self.apiKey + nonce
            if body is not None:
                body = self.json(body)
            headers = {
                'Request-Timestamp': nonce,
                'Operation-Id': self.uuid(),
                'API-Key': self.apiKey,
                'API-Hash': self.hmac(self.encode(payload), self.encode(self.secret), hashlib.sha512),
                'Content-Type': 'application/json',
            }
        else:
            self.check_required_credentials()
            body = self.urlencode(self.extend({
                'method': path,
                'moment': self.nonce(),
            }, params))
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'API-Key': self.apiKey,
                'API-Hash': self.hmac(self.encode(body), self.encode(self.secret), hashlib.sha512),
            }
        return {'url': url, 'method': method, 'body': body, 'headers': headers}

    def handle_errors(self, httpCode, reason, url, method, headers, body, response, requestHeaders, requestBody):
        if response is None:
            return  # fallback to default error handler
        if 'code' in response:
            #
            # bitbay returns the integer 'success': 1 key from their private API
            # or an integer 'code' value from 0 to 510 and an error message
            #
            #      {'success': 1, ...}
            #      {'code': 502, 'message': 'Invalid sign'}
            #      {'code': 0, 'message': 'offer funds not exceeding minimums'}
            #
            #      400 At least one parameter wasn't set
            #      401 Invalid order type
            #      402 No orders with specified currencies
            #      403 Invalid payment currency name
            #      404 Error. Wrong transaction type
            #      405 Order with self id doesn't exist
            #      406 No enough money or crypto
            #      408 Invalid currency name
            #      501 Invalid public key
            #      502 Invalid sign
            #      503 Invalid moment parameter. Request time doesn't match current server time
            #      504 Invalid method
            #      505 Key has no permission for self action
            #      506 Account locked. Please contact with customer service
            #      509 The BIC/SWIFT is required for self currency
            #      510 Invalid market name
            #
            code = self.safe_string(response, 'code')  # always an integer
            feedback = self.id + ' ' + body
            exceptions = self.exceptions
            if code in self.exceptions:
                raise exceptions[code](feedback)
            else:
                raise ExchangeError(feedback)
