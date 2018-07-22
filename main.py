import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like

from pandas_datareader import data
import datetime
from bokeh.plotting import figure, show, output_file


start = datetime.datetime(2018,6,1)
end = datetime.datetime(2018,6,30)

df = data.DataReader(name='AAPL', data_source='morningstar', start=start, end=end)

p = figure(x_axis_type='datetime', width=1000, height=300)
p.title.text = 'Candlestick Chart'

#df.index[df.Close > df.Open]