# Stock Split Calendar (Python)
Python interface to www.investing.com/stock-split-calendar/

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
python3 main.py # will connect to investing.com and start fetching the stock splits.
```

## File containing stock split from 1982 to 2017/12/20 (~59943 records)

- [stock-splits-1982-2017_12_20.tsv](https://github.com/philipperemy/stock-split-calendar/blob/master/stock-splits-1982-2017_12_20.tsv)

