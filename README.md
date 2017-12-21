# Stock Split Calendar (Python API)
Python interface to www.investing.com/stock-split-calendar/

## Pregenerated file containing stock split from 1982 to 2017/12/20

- [stock-splits-1982-2017_12_20.tsv](https://github.com/philipperemy/stock-split-calendar/blob/master/stock-splits-1982-2017_12_20.tsv) [Hit the download button on the right]
- ~59943 records
- Given for convenience (generate yours by running the script)!

## The API

- **```investing.get_stock_split_calendar(date='2017-04-10', debug=True)```**
  - `date`: Day of which to execute the query.
  - `debug`: True (default) will print some information to the console.
  - `returns`: List of the stock split records (name, symbol, country, factor, date)

## Example of output

<p align="center">
  <img src="ssc.png" width="500"><br/>
  <i>Stock split calendar for 2017/12/15.</i>
</p>


This translates to:
```
2017-12-15
-      C&S Asset Management                      032040                south_korea           1:5
-      Cayman Golden Century                     900280                south_korea           1.152:1
-      STX                                       011810                south_korea           1:10
-      Sumeet Industries Ltd                     SUIN                  india                 1.08:1
-      Marindi Metals                            MZN                   australia             1.011:1
-      Transurban Group                          TCL                   australia             1.005:1
-      Faes Farma                                FAE                   spain                 1.034:1
-      Think Smart SA                            THK                   spain                 1.026:1
-      Feedback Tech                             8091                  taiwan                1:1.43
-      Concierge Tech                            CNCGD                 usa                   1:30
-      Indata                                    IDTA                  poland                1:10
-      Nordic Mining                             NOMIN                 norway                1.004:1
```

## Usage

```
git clone https://github.com/philipperemy/stock-split-calendar.git
cd stock-split-calendar
pip3 install -r requirements.txt
python3 main.py # will connect to investing.com and start fetching the stock splits in output.tsv
```

You can see the progression by opening another terminal and running this command:
```
cd stock-split-calendar
tail -f output.tsv
```

