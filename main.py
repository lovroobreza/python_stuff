import csv
import pandas

#3with open("./files/weather_data.csv") as data_file:
   # data = csv.reader(data_file)
#    temps=[]
 #   for line in data:
  #      print(line)

data = pandas.read_csv("./files/weather_data.csv")

print(data["temp"].max())