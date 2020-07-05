#!/usr/bin/env python

import sys
import pandas as pd
import numpy as np
from enum import Enum
from moex_client import MoexClient


class ErrorStatus(Enum):
    DO_NOT_HAVE_DATA = 1
    STRICT_FILTER = 2


ErrorMessages = {
    ErrorStatus.DO_NOT_HAVE_DATA: "There is no data to analyze.",
    ErrorStatus.STRICT_FILTER: "The server sent the data. But your date filter is too strict. "
                               "And we have no data to analyze. Try setting the date early."
}


class MoexAnalizer:
    def __init__(self, engine, market, board, security, date):
        self.engine = engine
        self.market = market
        self.board = board
        self.security = security
        self.date = date
        self.client = MoexClient()

    def get_data_frame(self):
        data, columns = self.client.get_history_securities(self.engine, self.market, self.board, self.security, '1990-01-01')
        data_frame = self.__generate_data_frame(data, columns)

        self.__check_data(data_frame)

        return data_frame

    def __generate_data_frame(self, data, columns):
        temp_frame = pd.DataFrame(data=data, columns=columns)
        date_frame = temp_frame.loc[:, ['TRADEDATE', 'CLOSE']]
        date_frame.columns = ['date', 'price']
        date_frame['date'] = date_frame['date'].apply(np.datetime64)
        return date_frame.set_index('date')

    def __check_data(self, data_frame):
        server_sent_data = 0 < len(data_frame)
        if not server_sent_data:
            self.__error(ErrorStatus.DO_NOT_HAVE_DATA)

        has_data_after_filtering_by_date = 0 < len(data_frame[self.date:])
        if not has_data_after_filtering_by_date:
            self.__error(ErrorStatus.STRICT_FILTER)

    def __error(self, status):
        print(ErrorMessages[status])

        print("Engine: {}, market: {}, board: {}, security: {}, date: {}"
              .format(self.engine, self.market, self.board, self.security, self.date))

        sys.exit(status.value)
