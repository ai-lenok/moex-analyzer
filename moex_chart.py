#!/usr/bin/env python
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import os


class MoexConstant:
    IMAGE_DIR = 'chart/'


class MoexChart:
    def __init__(self):
        pass

    def draw(self, data_frame, security_name, date):
        """
        Create image with chart of changing security price
        Image will put to path 'chart/{security_name}'

        :param data_frame: data for visualization.
        Format:
        |----------|----------|
        |---date---|---price--|
        |----------|----------|
        |2020-04-01|1000.00   |
        |2020-04-02|1001.00   |
        |----------|----------|
        Where column 'date' is index
        :param security_name: name of security. User for file name and top of chart.
        :param date: date from start show. Use like filter.
        """
        day_price = data_frame[date:].price
        week_price = data_frame.price.rolling(5).mean()[date:]
        month_price = data_frame.price.rolling(20).mean()[date:]
        year_price = data_frame.price.rolling(200).mean()[date:]
        date_x = data_frame[date:].index.values

        months = mdates.MonthLocator()
        format_date = mdates.DateFormatter('%Y-%m')

        fig, ax = plt.subplots(figsize=(16, 10))
        ax.set_title(security_name + ' price chart')

        plt.plot(date_x, day_price, 'red', label='Closing price of the day')
        plt.plot(date_x, week_price, 'yellow', label='Weekly moving average')
        plt.plot(date_x, month_price, 'blue', label='Monthly moving average')
        plt.plot(date_x, year_price, 'green', label='Yearly moving average')

        ax.set_ylabel('Rubles (₽)')
        ax.set_xlabel('Date')

        ax.xaxis.set_major_locator(months)
        ax.xaxis.set_major_formatter(format_date)

        ax.grid(True)

        plt.legend()

        if not os.path.exists(MoexConstant.IMAGE_DIR):
            os.mkdir(MoexConstant.IMAGE_DIR)
        fig.savefig(MoexConstant.IMAGE_DIR + security_name + '.png')
        fig.show()
