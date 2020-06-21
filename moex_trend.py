#!/usr/bin/env python
class MoexTrend:
    def __init__(self):
        pass

    def print_trend(self, data_frame, security_name):
        price_last = data_frame.iloc[-1].price
        price_yesterday = data_frame.iloc[-2].price
        price_week_ago = data_frame.iloc[-11:-6].price.mean()
        price_month_ago = data_frame.iloc[-27:-21].price.mean()
        price_year_ago = data_frame.iloc[-207:-201].price.mean()

        diff_yesterday = (price_last - price_yesterday) / price_yesterday
        diff_week = (price_last - price_week_ago) / price_week_ago
        diff_month = (price_last - price_month_ago) / price_month_ago
        diff_year = (price_last - price_year_ago) / price_year_ago

        print("{} Day change:   {:.2%}".format(security_name, diff_yesterday))
        print("{} Week change:  {:.2%}".format(security_name, diff_week))
        print("{} Month change: {:.2%}".format(security_name, diff_month))
        print("{} Year change:  {:.2%}".format(security_name, diff_year))
