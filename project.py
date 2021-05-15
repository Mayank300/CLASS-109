import csv
import statistics as st
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv("project.csv") 
data = df["math score"].tolist()

mean = st.mode(data)
mode = st.mode(data)
median = st.median(data)
median = st.median(data)
std = st.stdev(data)

start_num1,end_num1 = mean - std, std + mean
start_num2,end_num2 = mean - (2 * std), (2 * std) + mean
start_num3,end_num3 = mean - (3 * std), (3 * std) + mean

df = ff.create_distplot([data],["data"],show_hist=False)
df.add_trace(go.Scatter(x=[mean,mean], y=[0,0.1], mode="lines", name="MEAN"))

df.add_trace(go.Scatter(x=[start_num1,start_num1], y=[0,0.1], mode="lines", name="STD1"))
df.add_trace(go.Scatter(x=[end_num1,end_num1], y=[0,0.1], mode="lines", name="STD1"))

df.add_trace(go.Scatter(x=[start_num2,start_num2], y=[0,0.1], mode="lines", name="STD2"))
df.add_trace(go.Scatter(x=[end_num2,end_num2], y=[0,0.1], mode="lines", name="STD2"))

df.add_trace(go.Scatter(x=[start_num3,start_num3], y=[0,0.1], mode="lines", name="STD3"))
df.add_trace(go.Scatter(x=[end_num3,end_num3], y=[0,0.1], mode="lines", name="STD3"))

df.show()




list_std1 = [to_show for to_show in data if to_show > start_num1 and to_show < end_num1]
list_std2 = [to_show for to_show in data if to_show > start_num2 and to_show < end_num2]
list_std3 = [to_show for to_show in data if to_show > start_num3 and to_show < end_num3]


print("")
print("")
print("")
print("")

print("MEAN of the data is {}".format(mean))
print("MODE of the data is {}".format(mode))
print("MEDIAN of the data is {}".format(median))

print("")


print("{}% of data in first std".format(((len(list_std1) / len(data)) * 100)))
print("{}% of data in second std".format(((len(list_std2) / len(data)) * 100)))
print("{}% of data in third std".format(((len(list_std3) / len(data)) * 100)))

print("")
print("")
print("")
print("")