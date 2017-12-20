from datetime import datetime, timedelta
from time import sleep

from send import request


def run():
    cur = datetime.now() - timedelta(days=2)
    with open('output.tsv', 'w') as w:
        while True:
            cur_str = cur.strftime('%Y-%m-%d')
            print(cur_str)
            records = request(cur_str)
            for record in records:
                w.write(str(record))
                w.write('\n')
                w.flush()
            cur -= timedelta(days=1)
            sleep(0.1)


if __name__ == '__main__':
    run()
