import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like

from pandas_datareader import data
import datetime

start = datetime.datetime(2018,6,1)
end = datetime.datetime(2018,6,30)

df = data.DataReader(name='AAPL', data_source='morningstar', start=start, end=end)
print(df)