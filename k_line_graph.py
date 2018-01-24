import pandas as pd
from pandas_datareader import data as pdr 

import fix_yahoo_finance as yf 

import matplotlib.pyplot as pyt 
import matplotlib.finance as mpf
from bokeh.plotting import figure, show, output_file


# get the data from yahoo database
yf.pdr_override
df = pdr.get_data_yahoo("SPY", start = "2017-01-01", end = "2017-12-31")

w = 12 * 60 * 60 * 1000 # day to ms
df["date"] = pd.to_datetime(df.index)

inc = df.Close > df.Open
dec = df.Open > df.Close

TOOLS = "pan,wheel_zoom,box_zoom,reset,save"

# create a new figure for plotting using bokeh and specify the figure property values
p = figure(x_axis_type = "datetime", tools = TOOLS, plot_width = 1000, title = "SPY Candletick")

# The orientation of the major tick labels can be controlled with the major_lable_orientation
# property. This property accepts the values "horizontal" or "vertical" or a floating point
# number that gives the angle (in radians) to rotate from the horizontal
p.xaxis.major_label_orientation = 3.14 / 4

# alpha signifies the floating point between 0 (tranparent) to 1 (opaque)
# the line specifies the alpha for the grid lines to the plot
p.grid.grid_line_alpha = 0.3

# configure and add segment glyphs to the figure
p.segment(df.date, df.High, df.date, df.Low, color = "red")

# adds vbar glyphs to the figure
p.vbar(df.date[inc], w, df.Open[inc], df.Close[inc], fill_color = "green", line_color = "black")
p.vbar(df.date[dec], w, df.Open[dec], df.Close[dec], fill_color = "red", line_color = "black")

# generate simple standalone HTML documents for bokeh visulization
output_file("candlestick.html", title = "candlestick.py example")

# open a browser
show(p)
