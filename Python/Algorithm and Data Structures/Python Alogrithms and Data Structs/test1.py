import requests, csv
# from datetime import date, datetime
# from dateutil.relativedelta import relativedelta

# newest_available_date = "2018-03-27"

# end_date = datetime.strptime(newest_available_date, "%Y-%m-%d")
# #end_date = end_date.strftime("%Y-%m-%d")

# start_date = end_date - relativedelta(months=+3)
# start_date = start_date.strftime("%Y-%m-%d")

# print(start_date)


csv_url = "https://data.nasdaq.com/api/v3/datasets/WIKI/AAPL.csv?start_date=1985-05-01&end_date=1997-07-01&order=asc"
req = requests.get(csv_url)
url_content = req.content
csv_file = open('downloaded.csv', 'wb')

csv_file.write(url_content)
csv_file.close()