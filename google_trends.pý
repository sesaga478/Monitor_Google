import pandas as pd
from pytrends.request import TrendReq
import matplotlib.pyplot as plt

def trends_time_reg(keywords=['Messi','Ronaldo'],frame='today 5-y'):
  # Set up pytrends
  #pytrends = TrendReq(hl='en-US', tz=360)
  pytrends = TrendReq()

  # Build the payload
  pytrends.build_payload(keywords, cat=0, timeframe=frame, geo='', gprop='')

  # Get interest over time
  df_time = pytrends.interest_over_time()
  df_region=pytrends.interest_by_region()

  # Plot the data
  plt.figure(figsize=(10, 6))
  df_time.plot()
  plt.title('Google Trends - {}'.format(frame))
  plt.xlabel('Date')
  plt.ylabel('Interest')
  plt.grid(True)

  # Show the plot
  plt.show()

  return df_time, df_region
