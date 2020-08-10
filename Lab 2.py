# Lab 02


"""

CSV: Forest Fires

#1 Which time of the year do forest fires occur the most often? Create
   a bar graph that displays the number of forest fires that occur during
   each month of the year.

#2 How do wind, rain, humidity, and temperature all play a role in the
   Initial Spread Index (ISI)? Create a graph that displays each factor's
   respective role in the ISI for each month.

#3 Does the Fine Fuel Moisture Code (FFMC) correlate with the Initial
   Spread Index (ISI)? In other words, can the moisture content of
   litter and other fine fuels increase or decrease the expected
   rate of fire spread? Create a line graph that displays the FFMC levels
   alongside the ISI levels throughout the year.

"""

x = open("forestfires.csv", "r")
heading = x.readline()
data1 = x.readlines()

def questionA():
    months = {"JAN": 0, "FEB":0, "MAR":0, "APR":0, "MAY":0, "JUN":0, "JUL":0, "AUG":0, "SEP":0, "OCT":0, "NOV":0, "DEC":0}
    for line in data1:
        line = line.split(",")
        months[line[2].upper()] += 1
    return months

##{'JAN': 2, 'FEB': 20, 'MAR': 54, 'APR': 9, 'MAY': 2, 'JUN': 17,
##'JUL': 32, 'AUG': 184, 'SEP': 172, 'OCT': 15, 'NOV': 1, 'DEC': 9}

def questionB():
    months = {"JAN": [], "FEB":[], "MAR":[], "APR":[], "MAY":[], "JUN":[], "JUL":[], "AUG":[], "SEP":[], "OCT":[], "NOV":[], "DEC":[]}
    for line in data1:
        line = line.split(",")
        if months[line[2].upper()] == []:
            months[line[2].upper()] = [float(line[8]), float(line[9]), float(line[10])]
        else:
            months[line[2].upper()][0] += float(line[8])
            months[line[2].upper()][1] += float(line[9])
            months[line[2].upper()][2] += float(line[10])
    return months

##{'JAN': [10.5, 178.0, 4.0], 'FEB': [192.69999999999996, 1114.0, 75.10000000000001],
##'MAR': [706.5000000000002, 2160.0, 268.3], 'APR': [108.4, 422.0, 42.0],
##'MAY': [29.3, 134.0, 8.9], 'JUN': [348.4, 767.0, 70.30000000000001],
##'JUL': [707.5000000000001, 1444.0, 119.5], 'AUG': [3980.2000000000025, 8370.0, 751.9000000000003],
##'SEP': [3373.3, 7369.0, 611.9000000000002], 'OCT': [256.40000000000003, 562.0, 51.900000000000006],
##'NOV': [11.8, 31.0, 4.5], 'DEC': [40.7, 346.0, 68.8]}


def questionC():
    month_dict = questionA()
    months = {"JAN": [], "FEB":[], "MAR":[], "APR":[], "MAY":[], "JUN":[], "JUL":[], "AUG":[], "SEP":[], "OCT":[], "NOV":[], "DEC":[]}
    for line in data1:
        line = line.split(",")
        if months[line[2].upper()] == []:
            months[line[2].upper()] = [float(line[4]), float(line[7])]
        else:
            months[line[2].upper()][0] += float(line[4])
            months[line[2].upper()][1] += float(line[7])
    for item in months:
        months[item][0] = round(months[item][0]/month_dict[item], 2)
        months[item][1] = round(months[item][1]/month_dict[item], 2)
    return months  
        
##{'JAN': [50.4, 1.45], 'FEB': [82.9, 3.35], 'MAR': [89.44, 7.11],
##'APR': [85.79, 5.38], 'MAY': [87.35, 4.6], 'JUN': [89.43, 11.78],
##'JUL': [91.33, 9.39], 'AUG': [92.34, 11.07], 'SEP': [91.24, 8.58],
##'OCT': [90.45, 7.15], 'NOV': [79.5, 1.1], 'DEC': [84.97, 3.47]}

"""

JSON: Wholesale Customers

#1 Find the percentage of money spent on each product in Oporto.
   Create a pie chart that displays these percentages.

#2 Considering the distance between Lisbon and Oporto, and the fact that
   Oporto is located further outwards on the coast, which region
   spends more money on wholesale products that supply the retail
   industry, and which region spends more money on wholesale products
   that supply the tourist industry (through restaurants, cafes, etc)?

#3 Which type of product dominates the others in terms of wholesale, across all regions?
   In other words, which subcategory of wholesale product do wholesale customers (from
   all the regions provided) spend the most money on annually? 
    
"""

import json
from pprint import pprint

info = open("wholesale.json", "r")
i = json.load(info)
data = i["data"]
info.close()

def question1():
    newdict = {"Fresh Products": 0, "Milk Products": 0, "Grocery Products": 0, "Frozen Products": 0, "Detergents and Paper Products": 0, "Delicatessen Products": 0}
    for d in data:
        if d["Region"] == "Oporto":
            newdict["Fresh Products"] += d["Annual spending on fresh products"]
            newdict["Milk Products"] += d["Annual spending on milk products"]
            newdict["Grocery Products"] += d["Annual spending on grocery products"]
            newdict["Frozen Products"] += d["Annual spending on frozen products"]
            newdict["Detergents and Paper Products"] += d["Annual spending on detergents and paper products"]
            newdict["Delicatessen Products"] += d["Annual spending on delicatessen products"]
    return newdict

##{'Fresh Products': 464721, 'Milk Products': 239144, 'Grocery Products': 433274,
##'Frozen Products': 190132, 'Detergents and Paper Products': 173311,
##'Delicatessen Products': 54506}

def percentages():
    products = question1()
    total = 0
    for num in products.values():
        total += num
    for item in products:
        products[item] = str(round((products[item]/total) * 100, 2)) + "%"
    return products

##{'Fresh Products': '29.88%', 'Milk Products': '15.38%', 'Grocery Products': '27.86%',
## 'Frozen Products': '12.23%', 'Detergents and Paper Products': '11.14%',
## 'Delicatessen Products': '3.51%'}
    
def question2():
    newdict = {"Retail": {"Lisbon": 0, "Oporto": 0, "Other regions":0},
               "Hotel/Restaurant/Cafe": {"Lisbon": 0, "Oporto": 0, "Other regions":0}}
    for d in data:
        if d["Industry"] == "retail":
            if d["Region"] == "Lisbon":
                newdict["Retail"]["Lisbon"] += 1
            elif d["Region"] == "Oporto":
                newdict["Retail"]["Oporto"] += 1
            elif d["Region"] == "other region":
                newdict["Retail"]["Other regions"] += 1
        elif d["Industry"] == "hotel/restaurant/cafe":
            if d["Region"] == "Lisbon":
                newdict["Hotel/Restaurant/Cafe"]["Lisbon"] += 1
            elif d["Region"] == "Oporto":
                newdict["Hotel/Restaurant/Cafe"]["Oporto"] += 1
            elif d["Region"] == "other region":
                newdict["Hotel/Restaurant/Cafe"]["Other regions"] += 1
    return newdict

##{'Retail': {'Lisbon': 18, 'Oporto': 19, 'Other regions': 105},
##'Hotel/Restaurant/Cafe': {'Lisbon': 59, 'Oporto': 28, 'Other regions': 211}}

def question3():
    newdict = {"Fresh": {"Lisbon":0, "Oporto":0, "other region":0},
               "Frozen": {"Lisbon":0, "Oporto":0, "other region":0},
               "Milk": {"Lisbon":0, "Oporto":0, "other region":0},
               "Grocery": {"Lisbon":0, "Oporto":0, "other region":0},
               "Detergents and Paper": {"Lisbon":0, "Oporto":0, "other region":0},
               "Delicatessen": {"Lisbon":0, "Oporto":0, "other region":0}}
    for d in data:
        newdict["Fresh"][d["Region"]] += d["Annual spending on fresh products"]
        newdict["Milk"][d["Region"]] += d["Annual spending on milk products"]
        newdict["Grocery"][d["Region"]] += d["Annual spending on grocery products"]
        newdict["Frozen"][d["Region"]] += d["Annual spending on frozen products"]
        newdict["Detergents and Paper"][d["Region"]] += d["Annual spending on detergents and paper products"]
        newdict["Delicatessen"][d["Region"]] += d["Annual spending on delicatessen products"]
    return newdict

##{'Fresh': {'Lisbon': 854833, 'Oporto': 464721, 'other region': 3960577},
##'Frozen': {'Lisbon': 231026, 'Oporto': 190132, 'other region': 930492},
##'Milk': {'Lisbon': 422454, 'Oporto': 239144, 'other region': 1888759},
##'Grocery': {'Lisbon': 570037, 'Oporto': 433274, 'other region': 2495251},
##'Detergents and Paper': {'Lisbon': 204136, 'Oporto': 173311, 'other region': 890410},
##'Delicatessen': {'Lisbon': 104327, 'Oporto': 54506, 'other region': 512110}}


import numpy as np
import matplotlib.pyplot as plt

# JSON Graphs

def jgraph1():
    a = question1()
    labels = a.keys()
    sizes = a.values()
    colors = ["darkcyan", "royalblue", "paleturquoise", "lightskyblue", "mediumaquamarine", "darkslategray"]
    patches, texts = plt.pie(sizes, colors = colors, shadow = True, startangle = 90)
    plt.legend(patches, labels)
    plt.axis("equal")
    plt.title("Percentage of Products Brought by Wholesale Customers in Oporto, Portugal")
    plt.show()
    
def jgraph2():
    a = question2()
    retail_data = (a["Retail"]["Lisbon"], a["Retail"]["Oporto"], a["Retail"]["Other regions"])
    other_data = (a["Hotel/Restaurant/Cafe"]["Lisbon"], a["Hotel/Restaurant/Cafe"]["Oporto"],
                  a["Hotel/Restaurant/Cafe"]["Other regions"])
    num_groups = 3
    fig, ax = plt.subplots()
    index = np.arange(num_groups)
    bar_width = 0.35
    opacity = 0.9
    rects1 = plt.bar(index, retail_data, bar_width,
                     alpha=opacity,
                     color='pink',
                     label = 'Retail')
    rects2 = plt.bar(index + bar_width, other_data, bar_width,
                     alpha=opacity,
                     color='skyblue',
                     label = 'Hotel/Restaurant/Cafe')
    plt.ylabel("Number of Wholesale Customers")
    plt.xticks(index+(bar_width/2), ('Lisbon', 'Oporto', 'Other regions'))
    plt.legend(fontsize = 11, framealpha=1)
    plt.title("Ratio of Wholesale Customers Shopping for Retail versus Hotel/Restaurant/Cafe")
    plt.show()

def jgraph3():
    a = question3()
    lisbon_data = (a["Fresh"]["Lisbon"], a["Frozen"]["Lisbon"],
                   a["Milk"]["Lisbon"], a["Grocery"]["Lisbon"],
                   a["Detergents and Paper"]["Lisbon"],
                   a["Delicatessen"]["Lisbon"])
    oporto_data = (a["Fresh"]["Oporto"], a["Frozen"]["Oporto"],
                   a["Milk"]["Oporto"], a["Grocery"]["Oporto"],
                   a["Detergents and Paper"]["Oporto"],
                   a["Delicatessen"]["Oporto"])
    other_data = (a["Fresh"]["other region"], a["Frozen"]["other region"],
                   a["Milk"]["other region"], a["Grocery"]["other region"],
                   a["Detergents and Paper"]["other region"],
                   a["Delicatessen"]["other region"])
    num_groups = 6
    fig, ax = plt.subplots()
    index = np.arange(num_groups)
    bar_width = 0.3
    opacity = 0.7
    rects1 = plt.bar(index, lisbon_data, bar_width,
                     alpha=opacity,
                     color="seagreen",
                     label = "Lisbon")
    rects2 = plt.bar(index + bar_width, oporto_data, bar_width,
                     alpha=opacity,
                     color="red",
                     label = "Oporto")
    rects3 = plt.bar(index + (bar_width*2), other_data, bar_width,
                     alpha=opacity,
                     color="coral",
                     label = "Other regions")
    plt.xlabel("Type of Product")
    plt.ylabel("Total Annual Spendings")
    plt.xticks(index+bar_width, ("Fresh", "Frozen",
                                "Milk", "Grocery",
                                "Detergents and Paper",
                                "Delicatessen"))
    plt.legend(fontsize = 11, framealpha=1)
    plt.title("Regional Distribution of Products Bought by Wholesale Customers")
    plt.show()


# CSV Graphs

def cgraph1():
    a = questionA()
    months = a.keys()
    y_pos = np.arange(len(months))
    num_fires = list(a.values())
    plt.barh(y_pos, num_fires, align='center', alpha=0.8, color="indianred")
    plt.title("Forest Fires Per Month")
    plt.yticks(y_pos, months)
    plt.xlabel("Number of Fires")
    plt.show()

def cgraph2():
    a = questionB()
    num = 12
    temp = []
    humidity = []
    wind = []
    for item in a.values():
        temp.append(item[0])
        humidity.append(item[1])
        wind.append(item[2])
    ind = np.arange(num)
    width = 0.55
    p1 = plt.bar(ind, temp, width, color = "lightcoral")
    p2 = plt.bar(ind, humidity, width, bottom=temp, color = "teal")
    p3 = plt.bar(ind, wind, width, bottom = (np.array(temp)+np.array(humidity)), color = "gold")
    plt.xticks(ind, a.keys())
    plt.ylabel("Sum of Temperature, Humidity, and Wind Levels")
    plt.legend((p1[0], p2[0], p3[0]), ("Temperature", "Humidity", "Wind"), fontsize = 11, framealpha=1, fancybox=True)
    plt.title("Contribution of Temperature, Humidity, and Wind to Forest Fires")
    plt.show()

from pylab import *

def cgraph3():
    a = questionC()
    y = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
    ffmc = []
    isi = []
    for item in y:
        ffmc.append(a[item][0])
        isi.append(a[item][1])
    plt.subplot(2,1,1)
    plt.plot(y, ffmc, color="olive", linewidth=3)
    plt.ylabel("FFMC Levels")
    plt.title("FFMC Progression")
    plt.grid(True)
    plt.subplot(2,1,2)
    plt.plot(y, isi, color="indianred", linewidth=3)
    plt.xlabel("Months")
    plt.ylabel("ISI Levels")
    plt.title("ISI Progression")
    plt.grid(True)
    plt.show()
    

# GRAPH FUNCTION CALLS

jgraph1()
#jgraph2()
#jgraph3()
#cgraph1()
#cgraph2()
#cgraph3()

    
    
    
    
        
    
