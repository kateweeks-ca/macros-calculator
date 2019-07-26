#imports
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#enter values
height = int(input("in inches please\n"))
age = int(input("age in years\n"))
weight = int(input("weight in lbs\n"))

#calculate bmr
BMR = (4.536* weight) + (15.88 * height) - (5 * age) + 5
print('bmr:', BMR)

#calculate TDEE based off 1-3 days exercise
TDEE = 1.375 * BMR
print('TDEE:', TDEE)


#calculate cutting calories 
deficit = input("percentage of deficit from 10-25%\n")
deficit = int(deficit) *.01
cutting = TDEE  * deficit


#calculate protein
proteinweight = input("select your percentage of protein based on bodyfat from 80%- 100%\n")
proteinweight = int(proteinweight) * .01
protein = weight * proteinweight

#calculate fat
fatweight = int(input("choose weighting for fat between 35% - 40%\n"))
fatweight = fatweight * .01
fat = weight * fatweight

#calculate carbs
x = (protein * 4) + (fat * 9)
carbs = (TDEE - cutting - x) / 4

#print macros & total cals
print('fat: ', fat, 'protein: ', protein, 'carbs: ', carbs)
print()
totalcal=(fat * 9) + (protein * 4) + (carbs * 4)
macros = {"fat": fat, "protein": protein, "carbs": carbs}
print(totalcal)


#enter breakfast totals
keys = ['fat', 'protein', 'carbs']
breakfast_values = input("Enter breakfast macros for fat protein & carbs seperated by a space: ")
blist  = (breakfast_values.split())
blist = [int(i) for i in blist]
breakfast = dict(zip(keys, blist))

#enter lunch totals
lunch_values = input("Enter lunch macros for fat protein & carbs seperated by a space: ")
llist  = (lunch_values.split())
llist = [int(i) for i in llist]
lunch = dict(zip(keys, llist))


#enter dinner totals
dinner_values = input("Enter dinner macros for fat protein & carbs seperated by a space: ")
dlist  = (dinner_values.split())
dlist = [int(i) for i in dlist]
dinner = dict(zip(keys, dlist))


#enter snack totals
snack_values = input("Enter snack macros for fat protein & carbs seperated by a space: ")
slist  = (snack_values.split())
slist = [int(i) for i in slist]
snacks = dict(zip(keys, slist))



#combine meals into one dataframe
today = pd.DataFrame(breakfast, index=["breakfast"])
today = today.append(pd.DataFrame(breakfast, index=['lunch']))
today = today.append(pd.DataFrame(lunch, index = ['snacks']))
today = today.append(pd.DataFrame(dinner, index = ['dinner']))
today =today.append(pd.DataFrame(macros, index=["totals"]))

#calculate your consumed macros
consumedtotal = (today.iloc[0:4,0].sum() * 9) + (today.iloc[0:4,1].sum() * 4)  +(today.iloc[0:4,2].sum() * 4)
print('fat: ', (today.iloc[0:4,0].sum() * 9)/consumedtotal * 100)
print('protein: ', (today.iloc[0:4,1].sum() * 4)/consumedtotal * 100)
print('carbs: ', (today.iloc[0:4,2].sum() * 4)/consumedtotal * 100)
totals = pd.DataFrame([(today.iloc[0:4,0] * 9), (today.iloc[0:4,1] * 4), (today.iloc[0:4,2] * 4)])
totalcalssofar = totals.sum()

#plot consumed macros
fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

recipe = ["fat",
         "protein",
         "carbs"]



totalcals = pd.DataFrame([totalcalssofar, totalcalssofar,totalcalssofar])
data = totals/totalcalssofar

data = data.sum(axis=1)

wedges, texts = ax.pie(data, wedgeprops=dict(width=0.5), startangle=-40)

bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
kw = dict(arrowprops=dict(arrowstyle="-"),
          bbox=bbox_props, zorder=0, va="center")

for i, p in enumerate(wedges):
    ang = (p.theta2 - p.theta1)/2. + p.theta1
    y = np.sin(np.deg2rad(ang))
    x = np.cos(np.deg2rad(ang))
    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    connectionstyle = "angle,angleA=0,angleB={}".format(ang)
    kw["arrowprops"].update({"connectionstyle": connectionstyle})
    ax.annotate(recipe[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
                horizontalalignment=horizontalalignment, **kw)

ax.set_title("Consumed Macros")

plt.show()
print("Remaining Cals = ", totalcal - consumedtotal)

#calculate target macros
tar_fat = (today.iloc[4,0] * 9)/totalcal *100 
print('fat:', tar_fat)
tar_protein = (today.iloc[4,1] * 4)/totalcal * 100
print('protein:', tar_protein)
tar_carbs = (today.iloc[4,2] * 4)/totalcal* 100 
print('carbs', tar_carbs)
tar_total = ((today.iloc[4,1] * 4)/totalcal) + ((today.iloc[4,0] * 9)/totalcal) +((today.iloc[4,2] * 4)/totalcal) 
print('total:', tar_total)
totals = pd.DataFrame([(today.iloc[4,0] * 9), (today.iloc[4,1] * 4), (today.iloc[4,2] * 4)])



#plot target macro percentages
fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

recipe = ["fat",
         "protein",
         "carbs"]
totalcals = pd.DataFrame([totalcal, totalcal,totalcal])
data1 = totals/totalcals 

data1 = data1.sum(axis=1)

wedges, texts = ax.pie(data1, wedgeprops=dict(width=0.5), startangle=-40)

bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
kw = dict(arrowprops=dict(arrowstyle="-"),
          bbox=bbox_props, zorder=0, va="center")

for i, p in enumerate(wedges):
    ang = (p.theta2 - p.theta1)/2. + p.theta1
    y = np.sin(np.deg2rad(ang))
    x = np.cos(np.deg2rad(ang))
    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    connectionstyle = "angle,angleA=0,angleB={}".format(ang)
    kw["arrowprops"].update({"connectionstyle": connectionstyle})
    ax.annotate(recipe[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
                horizontalalignment=horizontalalignment, **kw)

ax.set_title("Daily Macros")
