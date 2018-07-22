import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like

from pandas_datareader import data as pdr
import datetime
from bokeh.plotting import figure, show, output_file
from bokeh.embed import components
from bokeh.resources import CDN

import fix_yahoo_finance as yf 

start = datetime.datetime(2018,1,1) 
end = datetime.datetime(2018,3,10) 
yf.pdr_override()  
df = pdr.get_data_yahoo(tickers="GOOG", start=start, end=end)

df['Middle'] = (df.Open+df.Close)/2
df['Height'] = abs(df.Open-df.Close)

p = figure(x_axis_type='datetime', width = 1000, height=300, sizing_mode = "scale_width") 
p.title.text = "Candlestick Chart" 
p.grid.grid_line_alpha = 0.3
hours_12 = 12*60*60*1000 

p.segment(df.index, df.High, df.index, df.Low, color='Black')
p.rect(df.index,df.Middle, hours_12, df['Height'], fill_color="#CCFFFF", line_color="black")

script, div = components(p)
cdn_js = CDN.js_files
cdn_css = CDN.css_files
