#!/usr/bin/env python

import argparse

from moex_chart import MoexChart
from moex_analyzer import MoexAnalizer


def main():
    args = parse_arguments()

    engine_analyzer = MoexAnalizer('stock', 'shares', args.board, args.security, args.date)
    data_frame = engine_analyzer.get_data_frame()

    chart = MoexChart()
    chart.draw(data_frame, args.security, args.date)


def parse_arguments():
    parser = argparse.ArgumentParser(description='Analysis of Moscow Exchange Securities.')
    parser.add_argument('--security', help="Security for analysis", required=True)
    parser.add_argument('--board', help="Board where trade security", required=True)
    parser.add_argument('--date', help="Date of start analysis", default='1990-01-01')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    main()
