#!/usr/bin/env python

import argparse

from moex_chart import MoexChart
from moex_analyzer import MoexAnalizer
from moex_trend import MoexTrend


def main():
    args = parse_arguments()

    for security in args.security:
        engine_analyzer = MoexAnalizer('stock', 'shares', args.board, security, args.date)
        data_frame = engine_analyzer.get_data_frame()
        trend = MoexTrend()
        trend.print_trend(data_frame, security)

        if args.chart:
            chart = MoexChart()
            chart.draw(data_frame, security, args.date)
        print()


def parse_arguments():
    parser = argparse.ArgumentParser(description='Moscow Exchange Securities Analyzer.',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-s', '--security', help="Security for analysis", nargs='+', required=True)
    parser.add_argument('-b', '--board', help="Board where trade security", required=True)
    parser.add_argument('-d', '--date', help="Date of start analysis", default='1990-01-01')
    parser.add_argument('-c', '--chart', help="Draw chart", action='store_true')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    main()
