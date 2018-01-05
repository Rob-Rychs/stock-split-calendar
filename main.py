from datetime import datetime, timedelta
from time import sleep

from stock_split_calendar.investing import get_stock_split_calendar


def run():
    cur = datetime.now() - timedelta(days=2)
    with open('output.tsv', 'w') as w:
        while True:
            cur_str = cur.strftime('%Y-%m-%d')
            print(cur_str)
            records = get_stock_split_calendar(cur_str)
            for record in records:
                w.write(str(record))
                w.write('\n')
                w.flush()
            cur -= timedelta(days=1)
            sleep(0.1)


if __name__ == '__main__':
    run()
