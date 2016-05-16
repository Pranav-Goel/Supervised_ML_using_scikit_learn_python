#Our end goal with "labeling" data is to categorize it.
# With investing, we really have just two categories. There's outperform(1) or under-perform(0).
#there can be more categories
#First, we need to compare it to something. In our case, we're going to compare to "market," or the S&P 500 index.
#our main data set is Yahoo Finance, but we want to combine this data set with another - quandl

import pandas as pd
import os
import time
from datetime import datetime

path = "F:\scikit-ml-svm-python\intraQuarter"

def Key_Stats(gather="Total Debt/Equity (mrq)"):
    statspath = path+'/_KeyStats'
    stock_list = [x[0] for x in os.walk(statspath)]
    df = pd.DataFrame(columns = ['Date','Unix','Ticker','DE Ratio','Price','SP500'])

    sp500_df = pd.DataFrame.from_csv("YAHOO-INDEX_GSPC.csv")

    for each_dir in stock_list[1:25]:
        each_file = os.listdir(each_dir)
        ticker = each_dir.split("\\")[1]
        if len(each_file) > 0:
            for file in each_file:
                date_stamp = datetime.strptime(file, '%Y%m%d%H%M%S.html')
                unix_time = time.mktime(date_stamp.timetuple())
                full_file_path = each_dir+'/'+file
                source = open(full_file_path,'r').read()
                try:
                    value = float(source.split(gather+':</td><td class="yfnc_tabledata1">')[1].split('</td>')[0])

                    try:
                        sp500_date = datetime.fromtimestamp(unix_time).strftime('%Y-%m-%d')
                        row = sp500_df[(sp500_df.index == sp500_date)]
                        sp500_value = float(row["Adjusted Close"])
                    except:
                        sp500_date = datetime.fromtimestamp(unix_time-259200).strftime('%Y-%m-%d')
                        row = sp500_df[(sp500_df.index == sp500_date)]
                        sp500_value = float(row["Adjusted Close"])


                    stock_price = float(source.split('</small><big><b>')[1].split('</b></big>')[0])
                    print("stock_price:",stock_price,"ticker:", ticker)



                    df = df.append({'Date':date_stamp,
                                    'Unix':unix_time,
                                    'Ticker':ticker,
                                    'DE Ratio':value,
                                    'Price':stock_price,
                                    'SP500':sp500_value}, ignore_index = True)
                except Exception as e:
                    pass

    save = gather.replace(' ','').replace(')','').replace('(','').replace('/','')+('.csv')
    print(save)
    df.to_csv(save)



Key_Stats()