<?php

namespace ccxt;

// PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
// https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

use Exception as Exception; // a common import

class bleutrade extends bittrex {

    public function describe () {
        $timeframes = array (
            '15m' => '15m',
            '20m' => '20m',
            '30m' => '30m',
            '1h' => '1h',
            '2h' => '2h',
            '3h' => '3h',
            '4h' => '4h',
            '6h' => '6h',
            '8h' => '8h',
            '12h' => '12h',
            '1d' => '1d',
        );
        $result = array_replace_recursive (parent::describe (), array (
            'id' => 'bleutrade',
            'name' => 'Bleutrade',
            'countries' => array ( 'BR' ), // Brazil
            'rateLimit' => 1000,
            'version' => 'v2',
            'certified' => false,
            'has' => array (
                'CORS' => true,
                'fetchTickers' => true,
                'fetchOrders' => true,
                'fetchClosedOrders' => true,
                'fetchOrderTrades' => true,
                'fetchLedger' => true,
            ),
            'timeframes' => $timeframes,
            'hostname' => 'bleutrade.com',
            'urls' => array (
                'logo' => 'https://user-images.githubusercontent.com/1294454/30303000-b602dbe6-976d-11e7-956d-36c5049c01e7.jpg',
                'api' => array (
                    'public' => 'https://{hostname}/api/v2',
                    'account' => 'https://{hostname}/api/v2',
                    'market' => 'https://{hostname}/api/v2',
                    'v3Private' => 'https://{hostname}/api/v3/private',
                    'v3Public' => 'https://{hostname}/api/v3/public',
                ),
                'www' => 'https://bleutrade.com',
                'doc' => array (
                    'https://app.swaggerhub.com/apis-docs/bleu/white-label/3.0.0',
                ),
                'fees' => 'https://bleutrade.com/help/fees_and_deadlines',
            ),
            'api' => array (
                'account' => array (
                    'get' => array (
                        'balance',
                        'balances',
                        'depositaddress',
                        'deposithistory',
                        'order',
                        'orders',
                        'orderhistory',
                        'withdrawhistory',
                        'withdraw',
                    ),
                ),
                'public' => array (
                    'get' => array (
                        'candles',
                        'currencies',
                        'markethistory',
                        'markets',
                        'marketsummaries',
                        'marketsummary',
                        'orderbook',
                        'ticker',
                    ),
                ),
                'v3Public' => array (
                    'get' => array (
                        'assets',
                        'markets',
                        'ticker',
                        'marketsummary',
                        'marketsummaries',
                        'orderbook',
                        'markethistory',
                        'candles',
                    ),
                ),
                'v3Private' => array (
                    'get' => array (
                        'getbalance',
                        'getbalances',
                        'buylimit',
                        'selllimit',
                        'buylimitami',
                        'selllimitami',
                        'buystoplimit',
                        'sellstoplimit',
                        'ordercancel',
                        'getopenorders',
                        'getdeposithistory',
                        'getdepositaddress',
                        'getmytransactions',
                        'withdraw',
                        'directtransfer',
                        'getwithdrawhistory',
                        'getlimits',
                    ),
                ),
            ),
            'fees' => array (
                'funding' => array (
                    'withdraw' => array (
                        'ADC' => 0.1,
                        'BTA' => 0.1,
                        'BITB' => 0.1,
                        'BTC' => 0.001,
                        'BCC' => 0.001,
                        'BTCD' => 0.001,
                        'BTG' => 0.001,
                        'BLK' => 0.1,
                        'CDN' => 0.1,
                        'CLAM' => 0.01,
                        'DASH' => 0.001,
                        'DCR' => 0.05,
                        'DGC' => 0.1,
                        'DP' => 0.1,
                        'DPC' => 0.1,
                        'DOGE' => 10.0,
                        'EFL' => 0.1,
                        'ETH' => 0.01,
                        'EXP' => 0.1,
                        'FJC' => 0.1,
                        'BSTY' => 0.001,
                        'GB' => 0.1,
                        'NLG' => 0.1,
                        'HTML' => 1.0,
                        'LTC' => 0.001,
                        'MONA' => 0.01,
                        'MOON' => 1.0,
                        'NMC' => 0.015,
                        'NEOS' => 0.1,
                        'NVC' => 0.05,
                        'OK' => 0.1,
                        'PPC' => 0.1,
                        'POT' => 0.1,
                        'XPM' => 0.001,
                        'QTUM' => 0.1,
                        'RDD' => 0.1,
                        'SLR' => 0.1,
                        'START' => 0.1,
                        'SLG' => 0.1,
                        'TROLL' => 0.1,
                        'UNO' => 0.01,
                        'VRC' => 0.1,
                        'VTC' => 0.1,
                        'XVP' => 0.1,
                        'WDC' => 0.001,
                        'ZET' => 0.1,
                    ),
                ),
            ),
            'commonCurrencies' => array (
                'EPC' => 'Epacoin',
            ),
            'exceptions' => array (
                'Insufficient funds!' => '\\ccxt\\InsufficientFunds',
                'Invalid Order ID' => '\\ccxt\\InvalidOrder',
                'Invalid apikey or apisecret' => '\\ccxt\\AuthenticationError',
            ),
            'options' => array (
                // price precision by quote currency code
                'pricePrecisionByCode' => array (
                    'USD' => 3,
                ),
                'parseOrderStatus' => true,
                'disableNonce' => false,
                'symbolSeparator' => '_',
            ),
        ));
        // bittrex inheritance override
        $result['timeframes'] = $timeframes;
        return $result;
    }

    public function fetch_markets ($params = array ()) {
        // https://github.com/ccxt/ccxt/issues/5668
        $response = $this->publicGetMarkets ($params);
        $result = array();
        $markets = $this->safe_value($response, 'result');
        for ($i = 0; $i < count ($markets); $i++) {
            $market = $markets[$i];
            $id = $this->safe_string($market, 'MarketName');
            $baseId = $this->safe_string($market, 'MarketCurrency');
            $quoteId = $this->safe_string($market, 'BaseCurrency');
            $base = $this->safe_currency_code($baseId);
            $quote = $this->safe_currency_code($quoteId);
            $symbol = $base . '/' . $quote;
            $pricePrecision = 8;
            if (is_array($this->options['pricePrecisionByCode']) && array_key_exists($quote, $this->options['pricePrecisionByCode'])) {
                $pricePrecision = $this->options['pricePrecisionByCode'][$quote];
            }
            $precision = array (
                'amount' => 8,
                'price' => $pricePrecision,
            );
            // bittrex uses boolean values, bleutrade uses strings
            $active = $this->safe_value($market, 'IsActive', false);
            if (($active !== 'false') && $active) {
                $active = true;
            } else {
                $active = false;
            }
            $result[] = array (
                'id' => $id,
                'symbol' => $symbol,
                'base' => $base,
                'quote' => $quote,
                'baseId' => $baseId,
                'quoteId' => $quoteId,
                'active' => $active,
                'info' => $market,
                'precision' => $precision,
                'limits' => array (
                    'amount' => array (
                        'min' => $this->safe_float($market, 'MinTradeSize'),
                        'max' => null,
                    ),
                    'price' => array (
                        'min' => pow(10, -$precision['price']),
                        'max' => null,
                    ),
                ),
            );
        }
        return $result;
    }

    public function parse_order_status ($status) {
        $statuses = array (
            'OK' => 'closed',
            'OPEN' => 'open',
            'CANCELED' => 'canceled',
        );
        return $this->safe_string($statuses, $status, $status);
    }

    public function fetch_orders ($symbol = null, $since = null, $limit = null, $params = array ()) {
        // Possible $params
        // orderstatus (ALL, OK, OPEN, CANCELED)
        // ordertype (ALL, BUY, SELL)
        // depth (optional, default is 500, max is 20000)
        $this->load_markets();
        $market = null;
        $marketId = 'ALL';
        if ($symbol !== null) {
            $market = $this->market ($symbol);
            $marketId = $market['id'];
        }
        $request = array (
            'market' => $marketId,
            'orderstatus' => 'ALL',
        );
        $response = $this->accountGetOrders (array_merge ($request, $params));
        return $this->parse_orders($response['result'], $market, $since, $limit);
    }

    public function fetch_closed_orders ($symbol = null, $since = null, $limit = null, $params = array ()) {
        $response = $this->fetch_orders($symbol, $since, $limit, $params);
        return $this->filter_by($response, 'status', 'closed');
    }

    public function get_order_id_field () {
        return 'orderid';
    }

    public function parse_symbol ($id) {
        list($base, $quote) = explode($this->options['symbolSeparator'], $id);
        $base = $this->safe_currency_code($base);
        $quote = $this->safe_currency_code($quote);
        return $base . '/' . $quote;
    }

    public function fetch_order_book ($symbol, $limit = null, $params = array ()) {
        $this->load_markets();
        $request = array (
            'market' => $this->market_id($symbol),
            'type' => 'ALL',
        );
        if ($limit !== null) {
            $request['depth'] = $limit; // 50
        }
        $response = $this->publicGetOrderbook (array_merge ($request, $params));
        $orderbook = $this->safe_value($response, 'result');
        if (!$orderbook) {
            throw new ExchangeError($this->id . ' publicGetOrderbook() returneded no result ' . $this->json ($response));
        }
        return $this->parse_order_book($orderbook, null, 'buy', 'sell', 'Rate', 'Quantity');
    }

    public function fetch_order_trades ($id, $symbol = null, $since = null, $limit = null, $params = array ()) {
        // Currently we can't set the makerOrTaker field, but if the user knows the order side then it can be
        // determined (if the side of the trade is different to the side of the order, then the trade is maker).
        // Similarly, the correct 'side' for the trade is that of the order.
        // The trade fee can be set by the user, it is always 0.25% and is taken in the quote currency.
        $this->load_markets();
        $request = array (
            'orderid' => $id,
        );
        $response = $this->accountGetOrderhistory (array_merge ($request, $params));
        return $this->parse_trades($response['result'], null, $since, $limit, array (
            'order' => $id,
        ));
    }

    public function fetch_transactions_by_type ($type, $code = null, $since = null, $limit = null, $params = array ()) {
        $this->load_markets();
        $method = ($type === 'deposit') ? 'accountGetDeposithistory' : 'accountGetWithdrawhistory';
        $response = $this->$method ($params);
        $result = $this->parseTransactions ($response['result']);
        return $this->filterByCurrencySinceLimit ($result, $code, $since, $limit);
    }

    public function fetch_deposits ($code = null, $since = null, $limit = null, $params = array ()) {
        return $this->fetch_transactions_by_type ('deposit', $code, $since, $limit, $params);
    }

    public function fetch_withdrawals ($code = null, $since = null, $limit = null, $params = array ()) {
        return $this->fetch_transactions_by_type ('withdrawal', $code, $since, $limit, $params);
    }

    public function parse_ohlcv ($ohlcv, $market = null, $timeframe = '1d', $since = null, $limit = null) {
        $timestamp = $this->parse8601 ($ohlcv['TimeStamp'] . '+00:00');
        return array (
            $timestamp,
            $this->safe_float($ohlcv, 'Open'),
            $this->safe_float($ohlcv, 'High'),
            $this->safe_float($ohlcv, 'Low'),
            $this->safe_float($ohlcv, 'Close'),
            $this->safe_float($ohlcv, 'Volume'),
        );
    }

    public function fetch_ohlcv ($symbol, $timeframe = '15m', $since = null, $limit = null, $params = array ()) {
        $this->load_markets();
        $market = $this->market ($symbol);
        $request = array (
            'period' => $this->timeframes[$timeframe],
            'market' => $market['id'],
            'count' => $limit,
        );
        $response = $this->publicGetCandles (array_merge ($request, $params));
        if (is_array($response) && array_key_exists('result', $response)) {
            if ($response['result']) {
                return $this->parse_ohlcvs($response['result'], $market, $timeframe, $since, $limit);
            }
        }
    }

    public function parse_trade ($trade, $market = null) {
        $timestamp = $this->parse8601 ($trade['TimeStamp'] . '+00:00');
        $side = null;
        if ($trade['OrderType'] === 'BUY') {
            $side = 'buy';
        } else if ($trade['OrderType'] === 'SELL') {
            $side = 'sell';
        }
        $id = $this->safe_string_2($trade, 'TradeID', 'ID');
        $symbol = null;
        if ($market !== null) {
            $symbol = $market['symbol'];
        }
        $cost = null;
        $price = $this->safe_float($trade, 'Price');
        $amount = $this->safe_float($trade, 'Quantity');
        if ($amount !== null) {
            if ($price !== null) {
                $cost = $price * $amount;
            }
        }
        return array (
            'id' => $id,
            'info' => $trade,
            'timestamp' => $timestamp,
            'datetime' => $this->iso8601 ($timestamp),
            'symbol' => $symbol,
            'type' => 'limit',
            'side' => $side,
            'order' => null,
            'takerOrMaker' => null,
            'price' => $price,
            'amount' => $amount,
            'cost' => $cost,
            'fee' => null,
        );
    }

    public function parse_ledger_entry_type ($type) {
        // deposits don't seem to appear in here
        $types = array (
            'TRADE' => 'trade',
            'WITHDRAW' => 'transaction',
        );
        return $this->safe_string($types, $type, $type);
    }

    public function parse_ledger_entry ($item, $currency = null) {
        //
        // trade (both sides)
        //
        //     {
        //         ID => 109660527,
        //         TimeStamp => '2018-11-14 15:12:57.140776',
        //         Asset => 'ETH',
        //         AssetName => 'Ethereum',
        //         Amount => 0.01,
        //         Type => 'TRADE',
        //         Description => 'Trade +, order $id 133111123',
        //         Comments => '',
        //         CoinSymbol => 'ETH',
        //         CoinName => 'Ethereum'
        //     }
        //
        //     {
        //         ID => 109660526,
        //         TimeStamp => '2018-11-14 15:12:57.140776',
        //         Asset => 'BTC',
        //         AssetName => 'Bitcoin',
        //         Amount => -0.00031776,
        //         Type => 'TRADE',
        //         Description => 'Trade -, order $id 133111123, $fee -0.00000079',
        //         Comments => '',
        //         CoinSymbol => 'BTC',
        //         CoinName => 'Bitcoin'
        //     }
        //
        // withdrawal
        //
        //     {
        //         ID => 104672316,
        //         TimeStamp => '2018-05-03 08:18:19.031831',
        //         Asset => 'DOGE',
        //         AssetName => 'Dogecoin',
        //         Amount => -61893.87864686,
        //         Type => 'WITHDRAW',
        //         Description => 'Withdraw => 61883.87864686 to address DD8tgehNNyYB2iqVazi2W1paaztgcWXtF6; $fee 10.00000000',
        //         Comments => '',
        //         CoinSymbol => 'DOGE',
        //         CoinName => 'Dogecoin'
        //     }
        //
        $code = $this->safe_currency_code($this->safe_string($item, 'CoinSymbol'), $currency);
        $description = $this->safe_string($item, 'Description');
        $type = $this->parse_ledger_entry_type ($this->safe_string($item, 'Type'));
        $referenceId = null;
        $fee = null;
        $delimiter = ($type === 'trade') ? ', ' : '; ';
        $parts = explode($delimiter, $description);
        for ($i = 0; $i < count ($parts); $i++) {
            $part = $parts[$i];
            if (mb_strpos($part, 'fee') === 0) {
                $part = str_replace('fee ', '', $part);
                $feeCost = floatval ($part);
                if ($feeCost < 0) {
                    $feeCost = -$feeCost;
                }
                $fee = array (
                    'cost' => $feeCost,
                    'currency' => $code,
                );
            } else if (mb_strpos($part, 'order id') === 0) {
                $referenceId = str_replace('order id', '', $part);
            }
            //
            // does not belong to Ledger, related to parseTransaction
            //
            //     if (mb_strpos($part, 'Withdraw') === 0) {
            //         $details = explode(' to address ', $part);
            //         if (strlen ($details) > 1) {
            //             address = $details[1];
            //     }
            //
        }
        $timestamp = $this->parse8601 ($this->safe_string($item, 'TimeStamp'));
        $amount = $this->safe_float($item, 'Amount');
        $direction = null;
        if ($amount !== null) {
            $direction = 'in';
            if ($amount < 0) {
                $direction = 'out';
                $amount = -$amount;
            }
        }
        $id = $this->safe_string($item, 'ID');
        return array (
            'id' => $id,
            'info' => $item,
            'timestamp' => $timestamp,
            'datetime' => $this->iso8601 ($timestamp),
            'direction' => $direction,
            'account' => null,
            'referenceId' => $referenceId,
            'referenceAccount' => null,
            'type' => $type,
            'currency' => $code,
            'amount' => $amount,
            'before' => null,
            'after' => null,
            'status' => 'ok',
            'fee' => $fee,
        );
    }

    public function fetch_ledger ($code = null, $since = null, $limit = null, $params = array ()) {
        //
        //     if ($code === null) {
        //         throw new ExchangeError($this->id . ' fetchClosedOrders requires a `symbol` argument');
        //     }
        //
        $this->load_markets();
        $request = array();
        //
        //     if ($code !== null) {
        //         $currency = $this->market ($code);
        //         $request['asset'] = $currency['id'];
        //     }
        //
        $response = $this->v3PrivateGetGetmytransactions (array_merge ($request, $params));
        return $this->parse_ledger($response['result'], $code, $since, $limit);
    }

    public function parse_order ($order, $market = null) {
        //
        // fetchOrders
        //
        //     {
        //         OrderId => '107220258',
        //         Exchange => 'LTC_BTC',
        //         Type => 'SELL',
        //         Quantity => '2.13040000',
        //         QuantityRemaining => '0.00000000',
        //         Price => '0.01332672',
        //         Status => 'OK',
        //         Created => '2018-06-30 04:55:50',
        //         QuantityBaseTraded => '0.02839125',
        //         Comments => ''
        //     }
        //
        $side = $this->safe_string_2($order, 'OrderType', 'Type');
        $isBuyOrder = ($side === 'LIMIT_BUY') || ($side === 'BUY');
        $isSellOrder = ($side === 'LIMIT_SELL') || ($side === 'SELL');
        if ($isBuyOrder) {
            $side = 'buy';
        }
        if ($isSellOrder) {
            $side = 'sell';
        }
        // We parse different fields in a very specific $order->
        // Order might well be closed and then canceled.
        $status = null;
        if ((is_array($order) && array_key_exists('Opened', $order)) && $order['Opened']) {
            $status = 'open';
        }
        if ((is_array($order) && array_key_exists('Closed', $order)) && $order['Closed']) {
            $status = 'closed';
        }
        if ((is_array($order) && array_key_exists('CancelInitiated', $order)) && $order['CancelInitiated']) {
            $status = 'canceled';
        }
        if ((is_array($order) && array_key_exists('Status', $order)) && $this->options['parseOrderStatus']) {
            $status = $this->parse_order_status($this->safe_string($order, 'Status'));
        }
        $symbol = null;
        $marketId = $this->safe_string($order, 'Exchange');
        if ($marketId === null) {
            if ($market !== null) {
                $symbol = $market['symbol'];
            }
        } else {
            if (is_array($this->markets_by_id) && array_key_exists($marketId, $this->markets_by_id)) {
                $market = $this->markets_by_id[$marketId];
                $symbol = $market['symbol'];
            } else {
                $symbol = $this->parse_symbol ($marketId);
            }
        }
        $timestamp = null;
        if (is_array($order) && array_key_exists('Opened', $order)) {
            $timestamp = $this->parse8601 ($order['Opened'] . '+00:00');
        }
        if (is_array($order) && array_key_exists('Created', $order)) {
            $timestamp = $this->parse8601 ($order['Created'] . '+00:00');
        }
        $lastTradeTimestamp = null;
        if ((is_array($order) && array_key_exists('TimeStamp', $order)) && ($order['TimeStamp'] !== null)) {
            $lastTradeTimestamp = $this->parse8601 ($order['TimeStamp'] . '+00:00');
        }
        if ((is_array($order) && array_key_exists('Closed', $order)) && ($order['Closed'] !== null)) {
            $lastTradeTimestamp = $this->parse8601 ($order['Closed'] . '+00:00');
        }
        if ($timestamp === null) {
            $timestamp = $lastTradeTimestamp;
        }
        $fee = null;
        $commission = null;
        if (is_array($order) && array_key_exists('Commission', $order)) {
            $commission = 'Commission';
        } else if (is_array($order) && array_key_exists('CommissionPaid', $order)) {
            $commission = 'CommissionPaid';
        }
        if ($commission) {
            $fee = array (
                'cost' => $this->safe_float($order, $commission),
            );
            if ($market !== null) {
                $fee['currency'] = $market['quote'];
            } else if ($symbol !== null) {
                $currencyIds = explode('/', $symbol);
                $quoteCurrencyId = $currencyIds[1];
                $fee['currency'] = $this->safe_currency_code($quoteCurrencyId);
            }
        }
        $price = $this->safe_float($order, 'Price');
        $cost = null;
        $amount = $this->safe_float($order, 'Quantity');
        $remaining = $this->safe_float($order, 'QuantityRemaining');
        $filled = null;
        if ($amount !== null && $remaining !== null) {
            $filled = $amount - $remaining;
        }
        if (!$cost) {
            if ($price && $filled) {
                $cost = $price * $filled;
            }
        }
        if (!$price) {
            if ($cost && $filled) {
                $price = $cost / $filled;
            }
        }
        $average = $this->safe_float($order, 'PricePerUnit');
        $id = $this->safe_string_2($order, 'OrderUuid', 'OrderId');
        return array (
            'info' => $order,
            'id' => $id,
            'timestamp' => $timestamp,
            'datetime' => $this->iso8601 ($timestamp),
            'lastTradeTimestamp' => $lastTradeTimestamp,
            'symbol' => $symbol,
            'type' => 'limit',
            'side' => $side,
            'price' => $price,
            'cost' => $cost,
            'average' => $average,
            'amount' => $amount,
            'filled' => $filled,
            'remaining' => $remaining,
            'status' => $status,
            'fee' => $fee,
        );
    }

    public function parse_transaction ($transaction, $currency = null) {
        //
        //  deposit:
        //
        //     {
        //         Id => '96974373',
        //         Coin => 'DOGE',
        //         Amount => '12.05752192',
        //         TimeStamp => '2017-09-29 08:10:09',
        //         Label => 'DQqSjjhzCm3ozT4vAevMUHgv4vsi9LBkoE',
        //     }
        //
        // withdrawal:
        //
        //     {
        //         Id => '98009125',
        //         Coin => 'DOGE',
        //         Amount => '-483858.64312050',
        //         TimeStamp => '2017-11-22 22:29:05',
        //         Label => '483848.64312050;DJVJZ58tJC8UeUv9Tqcdtn6uhWobouxFLT;10.00000000',
        //         TransactionId => '8563105276cf798385fee7e5a563c620fea639ab132b089ea880d4d1f4309432',
        //     }
        //
        //     {
        //         "Id" => "95820181",
        //         "Coin" => "BTC",
        //         "Amount" => "-0.71300000",
        //         "TimeStamp" => "2017-07-19 17:14:24",
        //         "Label" => "0.71200000;PER9VM2txt4BTdfyWgvv3GziECRdVEPN63;0.00100000",
        //         "TransactionId" => "CANCELED"
        //     }
        //
        $id = $this->safe_string($transaction, 'Id');
        $amount = $this->safe_float($transaction, 'Amount');
        $type = 'deposit';
        if ($amount < 0) {
            $amount = abs ($amount);
            $type = 'withdrawal';
        }
        $currencyId = $this->safe_string($transaction, 'Coin');
        $code = $this->safe_currency_code($currencyId, $currency);
        $label = $this->safe_string($transaction, 'Label');
        $timestamp = $this->parse8601 ($this->safe_string($transaction, 'TimeStamp'));
        $txid = $this->safe_string($transaction, 'TransactionId');
        $address = null;
        $feeCost = null;
        $labelParts = explode(';', $label);
        if (strlen ($labelParts) === 3) {
            $amount = floatval ($labelParts[0]);
            $address = $labelParts[1];
            $feeCost = floatval ($labelParts[2]);
        } else {
            $address = $label;
        }
        $fee = null;
        if ($feeCost !== null) {
            $fee = array (
                'currency' => $code,
                'cost' => $feeCost,
            );
        }
        $status = 'ok';
        if ($txid === 'CANCELED') {
            $txid = null;
            $status = 'canceled';
        }
        return array (
            'info' => $transaction,
            'timestamp' => $timestamp,
            'datetime' => $this->iso8601 ($timestamp),
            'id' => $id,
            'currency' => $code,
            'amount' => $amount,
            'address' => $address,
            'tag' => null,
            'status' => $status,
            'type' => $type,
            'updated' => null,
            'txid' => $txid,
            'fee' => $fee,
        );
    }

    public function sign ($path, $api = 'public', $method = 'GET', $params = array (), $headers = null, $body = null) {
        $url = $this->implode_params($this->urls['api'][$api], array (
            'hostname' => $this->hostname,
        )) . '/';
        if ($api === 'v3Private' || $api === 'account') {
            $this->check_required_credentials();
            if ($api === 'account') {
                $url .= $api . '/';
            }
            if ((($api === 'account') && ($path !== 'withdraw')) || ($path === 'openorders')) {
                $url .= strtolower($method);
            }
            $request = array (
                'apikey' => $this->apiKey,
            );
            $request['nonce'] = $this->nonce ();
            $url .= $path . '?' . $this->urlencode (array_merge ($request, $params));
            $signature = $this->hmac ($this->encode ($url), $this->encode ($this->secret), 'sha512');
            $headers = array( 'apisign' => $signature );
        } else {
            $url .= $api . '/' . strtolower($method) . $path;
            if ($params) {
                $url .= '?' . $this->urlencode ($params);
            }
        }
        return array( 'url' => $url, 'method' => $method, 'body' => $body, 'headers' => $headers );
    }
}