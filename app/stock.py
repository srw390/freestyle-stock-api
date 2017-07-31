import pandas_datareader as pdr
from datetime import datetime
import code
import csv
from datetime import date, timedelta
import matplotlib.pyplot as plt
import numpy as np

# Install mathplot and pandas_datareader
stocks = []

def stock_reader():
    csv_file_path = "data/nasdaq_company.csv"
    with open(csv_file_path, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        stocks = [dict(row) for row in reader]
        return stocks

def stock_pydata(stock, start, end):
    data_source = 'google'
    response = pdr.data.DataReader(stock, data_source, str(start), str(end))
    return response

def stock_quote():
    stock = input("Please enter the stock quote: ")
    start = input("Please enter start date E.g. 2017-07-24: ")
    end = input("Please enter historical date E.g. 2017-06-24: ")
    response = stock_pydata(stock, start, end)
    print (response)

def stock_sector():
    symbols = stock_reader()
    usr = input("Please select a sector E.g. Finance :")
    print ("{:<8} {:<15} {:<10}".format('Symbol','Name','Industry'))
    for sym in symbols:
        if sym.get("Sector") == usr:
            print ("{:<8} | {:<15} | {:<10}".format(sym.get("Symbol"), sym.get("Name"), sym.get("Industry")))

def stock_industry():
    symbols = stock_reader()
    usr = input("Please select a Indsutry E.g. Aerospace :")
    print ("{:<8} {:<15} {:<10}".format('Symbol','Name','Sector'))
    for sym in symbols:
        if sym.get("Industry") == usr:
            print ("{:<8} | {:<15} | {:<10}".format(sym.get("Symbol"), sym.get("Name"), sym.get("Sector")))

def stock_plot():
    stock = input("Please enter the stock quote: ")
    time = input("""
    Please provide timeline E.g. 3Y, 1Y, 6M, 3M, 1M to plot stock price graph
            """)
    timeline = {'1M': 30,
                '3M': 90,
                '6M': 180,
                '1Y': 365,
                '3Y': 1095,
            }
    days = timeline.get(time, None)
    if days:
        start = str(date.today() - timedelta(days=days)) #> '2017-07-09'
        end = str(date.today()) #> '2017-07-24'
        response = stock_pydata(stock, start, end)
        fig = plt.figure()
        subplot = fig.add_subplot(111)
        subplot.plot(response[["Close"]], color='lightblue', linewidth=3)
        fig.suptitle('Chart Price: {0}'.format(stock), fontsize=20)
        plt.xlabel('Date', fontsize=18)
        plt.ylabel('Price $', fontsize=16)
        plt.show()
    else:
        print("please select right time line")
        return

def default():
    print ("Please make a proper selection")

msg = """
------------------------
PRODUCTS APPLICATION
------------------------
Welcome @SRW390!
"""

print(msg)

menu = """
    options              | description
    -------------------  | -------------
    'Show By Industry'   | Display a list of stock by Industry.
    'Show By Sector'     | Show Stocks based on Sector.
    'Historical Prices'  | Show historical prices by symbol.
    'Plot Stock Graph'   | Plot historical prices.
"""

user = input(menu)

choices = {
            'Show By Industry': stock_industry,
            'Show By Sector': stock_sector,
            'Historical Prices': stock_quote,
            'Plot Stock Graph': stock_plot,
            'Default': default
        }

try:
    choices.get(user.title())()
except TypeError:
    default()
