from argparse import ArgumentParser
from datetime import datetime, timedelta

from stock_split_calendar.investing import get_stock_split_calendar

DATE_FORMAT = '%Y-%m-%d'


def arg_parse():
    arg_p = ArgumentParser()
    arg_p.add_argument('--start_date', type=str, default='1990-01-01')
    arg_p.add_argument('--end_date', type=str, default='now')
    arg_p.add_argument('--output_tsv_filename', type=str, default='output.tsv')
    return arg_p


def run():
    arg_p = arg_parse().parse_args()
    print('*' * 80)
    print(arg_p)
    print('*' * 80)

    if arg_p.end_date == 'now':
        cur = datetime.now()
    else:
        cur = datetime.strptime(arg_p.end_date, DATE_FORMAT)

    start_date = datetime.strptime(arg_p.start_date, DATE_FORMAT)

    with open(arg_p.output_tsv_filename, 'w') as w:
        while cur > start_date:
            cur_str = cur.strftime(DATE_FORMAT)
            print(cur_str)
            records = get_stock_split_calendar(cur_str)
            for record in records:
                w.write(str(record))
                w.write('\n')
                w.flush()
            cur -= timedelta(days=1)


if __name__ == '__main__':
    run()
