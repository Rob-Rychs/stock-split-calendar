from datetime import datetime, timedelta
from time import sleep

from send import request


def run():
    cur = datetime.now() - timedelta(days=2)
    while True:
        cur_str = cur.strftime('%Y-%m-%d')
        print(cur_str)
        request(cur_str)
        cur -= timedelta(days=1)
        sleep(0.1)


if __name__ == '__main__':
    run()
