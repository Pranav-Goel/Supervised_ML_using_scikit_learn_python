import pandas as pd
import os
import time
from datetime import datetime

path ="F:\scikit-ml-svm-python\intraQuarter"
def Key_Stats(gather="Total Debt/Equity (mrq)"):
    statspath = path+'/_KeyStats'
    stock_list = [x[0] for x in os.walk(statspath)]
    #print(stock_list)
    for each_dir in stock_list[1:]:
        each_file = os.listdir(each_dir)
        ticker = each_dir.split("\\")[1]
        if len(each_file) > 0:
            for file in each_file:

                date_stamp = datetime.strptime(file, '%Y%m%d%H%M%S.html')
                unix_time = time.mktime(date_stamp.timetuple())
                #print(date_stamp, unix_time)
                full_file_path = each_dir+'/'+file
                print(full_file_path)
                source = open(full_file_path,'r').read()
                #print(source)
                #now we have the source code, and we need to get the value of total debt/equity ratio
                #we split by the gather term, and by observstion of the source code,
                #a further osequence of html tags and code separates the gather term and the value we need
                #so we add that to the split term as well.
                #second split is important sice first split will give entire data following split as well
                #closing table tag immediately follows value, so it can be used aptly
                value = source.split(gather+':</td><td class="yfnc_tabledata1">')[1].split('</td>')[0]
                print(ticker+":",value)
                #above is a crude method, regex is better
            time.sleep(15)

Key_Stats()

