import pandas as pd
import os
import quandl
import time

auth_tok = "EWNaopf2RfNaVEL4XL2q"

data = quandl.get("WIKI/KO", trim_start = "2000-12-12", trim_end = "2014-12-30", authtoken=auth_tok)

print(data)

