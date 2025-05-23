## LIBRARIES
import requests
import json

url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/DOTM05/JSON-stat/2.0/en"
response = requests.get(url)
list = response.json()

ids = list["id"]
dimensions = list["dimension"]
sizes = list["size"]
values = list["value"]

#In order to extract the label for the statistic being reported in this dataset, first navigate to the dimension associated with 'STATISTICS' accessed by id[0]
index = dimensions[ids[0]]["category"]['index'][0] #Within "category", a dictionary object, the key "index" will provide the unique index for the stat being reported in the dataset. This returns a list, so extract the actual index with [0] 
statistic = dimensions[ids[0]]["category"]["label"][index] # Within category, the key "label" has a dictionary object, that has a label associated with the index accessed above

months_list = []
for i in range(0, sizes[1]):
    currentid = ids[1]
    index = dimensions[currentid]["category"]["index"][i]
    label = dimensions[currentid]["category"]["label"][index]
    months_list.append(label)

#The data is separated into 21 different bands
bands_list = []
for i in range(0, sizes[2]):
    currentid = ids[2]
    index = dimensions[currentid]["category"]["index"][i]
    label = dimensions[currentid]["category"]["label"][index]
    bands_list.append(label)

#Data is reported by county for 26 counties, and finally for All of Ireland
counties_list = []
for i in range(0, sizes[3]):
    currentid = ids[3]
    index = dimensions[currentid]["category"]["index"][i]
    label = dimensions[currentid]["category"]["label"][index]
    counties_list.append(label)

#The first 27 values reported will be associated with cars licensed in 2025 January (i.e. months_list[0]), across All bands (i.e. bands_list[0]), for each of the 26 counties, and finally Ireland
#I want to include the latest values from 2025 April in the app so I must skip values for the prior 3 months, and each month has 22 bands for 27 counties, and access from that value on
month = months_list[-1] #To access the final value in months list
band = bands_list[0]
value_number = ((sizes[1]-1)*sizes[2]*sizes[3])+1 #The first value reported for the final month will be 22 bands*27 counties * the number of prreceding months (sizes[1]-1) and add 1 to get the next value
cars_licenced = {}

value_number

for i in range(0, sizes[3]):
    currentid = ids[3]
    index = dimensions[currentid]["category"]["index"][i]
    label = dimensions[currentid]["category"]["label"][index]
    cars_licenced[label]=values[value_number+i]

