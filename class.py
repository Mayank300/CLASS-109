import random
import statistics as st
import plotly.figure_factory as ff
import plotly.graph_objects as go

result = []

for num in range(0,1000):
    num1 = random.randint(1,6)
    num2 = random.randint(1,6)

    result.append(num1 + num2)

mean = st.mean(result)
mode = st.mode(result)
median = st.median(result)
std = st.stdev(result)

start_num1,end_num1 = mean - std, std + mean
start_num2,end_num2 = mean - (2 * std), (2 * std) + mean
start_num3,end_num3 = mean - (3 * std), (3 * std) + mean


df = ff.create_distplot([result],["result"],show_hist=False)
df.add_trace(go.Scatter(x=[mean,mean], y=[0,0.17], mode="lines", name="MEAN"))

df.add_trace(go.Scatter(x=[start_num1,start_num1], y=[0,0.17], mode="lines", name="STD1"))
df.add_trace(go.Scatter(x=[end_num1,end_num1], y=[0,0.17], mode="lines", name="STD1"))

df.add_trace(go.Scatter(x=[start_num2,start_num2], y=[0,0.17], mode="lines", name="STD2"))
df.add_trace(go.Scatter(x=[end_num2,end_num2], y=[0,0.17], mode="lines", name="STD2"))

df.add_trace(go.Scatter(x=[start_num3,start_num3], y=[0,0.17], mode="lines", name="STD3"))
df.add_trace(go.Scatter(x=[end_num3,end_num3], y=[0,0.17], mode="lines", name="STD3"))



list_std1 = [res for res in result if res > start_num1 and res < end_num1]
list_std2 = [res for res in result if res > start_num2 and res < end_num2]
list_std3 = [res for res in result if res > start_num3 and res < end_num3]

print("")
print("")
print("")
print("")

print("MEAN of this data is {}".format(mean))
print("MODE of this data is {}".format(mode))
print("MEDIAN of this data is {}".format(median))
print("STD of this data is {}".format(std))

print("")
print("")
print("")
print("")

print("{}% of data in first std".format(((len(list_std1) / len(result)) * 100)))
print("{}% of data in second std".format(((len(list_std2) / len(result)) * 100)))
print("{}% of data in third std".format(((len(list_std3) / len(result)) * 100)))

print("")
print("")
print("")
print("")



# df.show()



