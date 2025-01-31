# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 14:09:59 2022

@author: maria alrammah

"""
#%%

##Question 1

discount = 21.95 * .75
can_count = 119
shipping_cost = 4

total_cost = (shipping_cost*discount)+(shipping_cost + 1 * discount*can_count)
print(total_cost)


#%%

##Question 2

coastline = 10524
globalaccess = 27800
legacy = 8500

##ask user input
supplier = input("Enter supplier name: ")
amount = float(input("Enter amount: "))
calculation = input("adding or subtracting?: ")

##if statements
if supplier == "coastline" and calculation == "adding":
    total = coastline+amount
    print(total)
if supplier == "coastline" and calculation == "subtracting":
    total = coastline-amount
    print(total)
if supplier == "globalaccess" and calculation == "adding":
    total = globalaccess+amount
    print(total)
if supplier == "globalaccess" and calculation == "subtracting":
    total = globalaccess-amount
    print(total)
if supplier == "legacy" and calculation == "adding":
    total = legacy+amount
    print(total)
if supplier == "legacy" and calculation == "subtracting":
    total = legacy-amount
    print(total)








#%%

##Question 3
location = input("Enter destination location: ")
nights = float(input("Enter number of nights you will stay at the hotel: "))
rental_days = float(input("Enter number of days you will rent a rental car: "))
spending_money = float(input("Enter the amount of spending money for the whole trip: "))

if location == "New York":
    flight_cost = 350
    print("Your flight cost will total to",flight_cost)
if location == "Los Angeles":
    flight_cost = 475
    print("Your flight cost will total to",flight_cost)
if location == "Chicago":
    flight_cost = 288
    print("Your flight cost will total to",flight_cost)
    
hotel_cost = nights * 150
print("Your hotel cost will total to",hotel_cost)

rental_cost = 50 
if rental_days > 7 :
    total_rental_cost = rental_days*rental_cost - 50
    print("Your car rental cost will total to",total_rental_cost)
if rental_days >= 3:
    total_rental_cost = rental_days*rental_cost - 20
    print("Your car rental cost will total to",total_rental_cost)
else:
    total_rental_cost = rental_days*rental_cost
    print("Your car rental cost will total to",rental_days*rental_cost)

total_cost = (flight_cost+hotel_cost+total_rental_cost+spending_money)
print("Your total cost for the whole trip will total to:",total_cost)




#%%

##Question 4

# This code calculates the number of average passengers per car and cars still available in the lot.
cars = 100 #The company has 100 cars available
space_in_car = 4 # each car has 4 passenger capacity
drivers = 30
passengers = 90

cars_not_driven = cars - drivers
cars_driven = drivers
average_passengers_per_car = passengers / cars_driven
print("The company has", cars, "cars available")
print("There are only",drivers,"drivers available")
print("There will be",cars_not_driven,"cars not driven today")
print("There are",passengers, "passengers to carpool today")
print("The average number of passengers per car is",passengers / drivers)





