import csv 
import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv('C:/Users/aadi_/Desktop/coding/python/archive/StudentsPerformance.csv')

readingScore = df['reading score'].to_list()

import statistics

mean = statistics.mean(readingScore)


median = statistics.median(readingScore)

mode = statistics.mode(readingScore)


sd = statistics.stdev(readingScore)

print('mean,median,sd,mode of weight is ,{},{},{} and {} repestivaly'.format(mean,statistics.median,sd,mode) )

w_first_sd_start,w_first_sd_end   = mean-sd,mean+sd
w_second_sd_start,w_second_sd_end = mean-(2*sd),mean + (2*sd)
w_third_sd_start,w_third_sd_end = mean-(3*sd),mean + (3*sd)

w_listOfDataWithinFirstSD = [result for result in readingScore if(result>w_first_sd_start and result<w_first_sd_end) ]
w_listOfDataWithinSecondSD = [result for result in readingScore if(result>w_second_sd_start and result<w_second_sd_end) ]
w_listOfDataWithinThirdSD = [result for result in readingScore if(result>w_third_sd_start and result<w_third_sd_end) ]

import plotly.graph_objects as go

print("{}% of data for weight lies within 1 standard deviation".format(len(w_listOfDataWithinFirstSD)*100.0/len(readingScore)))
print("{}% of data for weight lies within 2 standard deviation".format(len(w_listOfDataWithinSecondSD)*100.0/len(readingScore)))
print("{}% of data for weight lies within 3 standard deviation".format(len(w_listOfDataWithinThirdSD)*100.0/len(readingScore)))

fig = ff.create_distplot([df['reading score'].to_list()],['result'],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean], y=[0, 0.17], mode="lines", name="MEAN"))

fig.add_trace(go.Scatter(x=[w_first_sd_start,w_first_sd_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 start"))
fig.add_trace(go.Scatter(x=[w_second_sd_start,w_second_sd_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 start"))
fig.add_trace(go.Scatter(x=[w_third_sd_start,w_third_sd_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 start"))

fig.add_trace(go.Scatter(x=[w_first_sd_end,w_first_sd_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[w_second_sd_end,w_second_sd_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[w_third_sd_end,w_third_sd_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()