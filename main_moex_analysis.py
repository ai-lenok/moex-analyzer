#!/usr/bin/env python

import argparse
from moex_client import MoexClient

def main():
    parser = argparse.ArgumentParser(description='Analysis of Moscow Exchange Securities.')
    parser.add_argument('--security', help="Security for analysis")
    parser.add_argument('--date', help="Date of start analysis", default='1990-01-01')
    args = parser.parse_args()

    if args.security is not None:
        client = MoexClient()
        data, column = client.get_history_securities('stock', 'shares', 'TQBR', args.security, args.date)
        print(column)
        for item in data:
            print(item)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()