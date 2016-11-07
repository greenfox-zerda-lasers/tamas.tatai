apple_url = 'http://chart.finance.yahoo.com/table.csv?s=AAPL&a=9&b=7&c=2016&d=10&e=7&f=2016&g=d&ignore=.csv'

def download_stock(csv_url)
    response = request.urlopen()