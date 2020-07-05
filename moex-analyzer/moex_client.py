#!/usr/bin/env python
import requests

class MoexClient:
    """
    Implementation free API Moscow Exchange
    https://iss.moex.com/iss/reference/ - official documentation Moscow Exchange
    """

    def __init__(self):
        pass

    def get_all_securities(self):
        """
        List of all securities
        Very slow method

        https://iss.moex.com/iss/reference/5 - official documentation

        Example:
        data, column = client.get_all_securities()

        :return:
        result - list of all securities
        columns - list with names of one security
        """
        start = 0
        shift = 1
        result = []
        columns = []
        while shift > 0:
            url = 'https://iss.moex.com/iss/securities.json'
            res = requests.get(url, {'start': start})
            json = res.json()
            data = json['securities']['data']
            columns = json['securities']['columns']
            shift = len(data)
            start = start + shift
            result = result + data
        return result, columns

    def get_security(self, security):
        """
        Get info about security

        https://iss.moex.com/iss/reference/13 - official documentation

        Example:
        data, column = client.get_security('MOEX')

        :param security: name of security for searching

        :return:
        info about security
        column with names of info about security
        """
        url = 'https://iss.moex.com/iss/securities/{}.json'.format(security)
        res = requests.get(url)
        json = res.json()
        data = json['boards']['data']
        columns = json['boards']['columns']
        return data, columns

    def get_indices(self, security):
        """
        Return list of indices which security has

        https://iss.moex.com/iss/reference/160 - official documentation

        Example:
        data, column = client.get_indices('MOEX')

        :param security: name of security for searching

        :return:
        list of indices which security has
        list of names columns
        """
        url = 'https://iss.moex.com/iss/securities/{}/indices.json'.format(security)
        res = requests.get(url)
        json = res.json()
        data = json['indices']['data']
        column = json['indices']['columns']
        return data, column

    def get_aggregates(self, security, date):
        """
        Aggregates result of day by security

        https://iss.moex.com/iss/reference/214 - official documentation

        Example:
        data, column = client.get_indices('MOEX', '2020-06-01')
        :param security: name of security for searching
        :param date: day of aggregation
        :return:
        list of indices which security has
        list of names columns
        """
        url = 'https://iss.moex.com/iss/securities/{}/aggregates.json'.format(security)
        res = requests.get(url, {'date': date})
        json = res.json()
        print(json)

    def get_history_securities(self, engine, market, board, security, date):
        """
        Get history security trading from date

        https://iss.moex.com/iss/reference/65 - official documentation
        
        Example:
        data, column = client.get_history_securities('stock', 'shares', 'TQBR', 'MOEX', '2014-01-01')
        
        :param engine: have not found all categories :(
        :param market: 'shares', 'bonds'
        :param board: 'TQBR', 'TQTF', 'EQLV', 'EQRB'
        :param security: name of security for searching
        :param date: date of start list
        :return:
        list of securities with trading sum by days
        list of names columns
        """
        url = 'https://iss.moex.com/iss/history/engines/{}/markets/{}/boards/{}/securities/{}.json?'\
            .format(engine, market, board, security)

        start = 0
        shift = 1
        data = []
        column = []
        while shift > 0:
            res = requests.get(url, {'start': start, 'from': date, 'sort_column': 'TRADEDATE', 'sort_order': 'asc'})
            json = res.json()
            current_data = json['history']['data']
            data = data + current_data
            column = json['history']['columns']
            shift = len(current_data)
            start = start + shift
        return data, column
