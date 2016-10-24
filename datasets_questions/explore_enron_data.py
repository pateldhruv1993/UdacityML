#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print "Number of People:",len(enron_data)
#print enron_data
print "Features for each person in the datatset:", len(enron_data['METTS MARK'])


count = 0
for person in enron_data.items():
	if person[1]['poi'] == True:
		count = count + 1
		
print "Total POI's:", count



print "James Prentice's total stocks:", enron_data['PRENTICE JAMES']['total_stock_value']

print "Number of emails from Wesley Colwell to POI's: ", enron_data['COLWELL WESLEY']['from_this_person_to_poi']

print "Value of stock options exercised by Jeffrey K Skilling: ", enron_data['SKILLING JEFFREY K']['exercised_stock_options']

print "Total payment of Lay: ", enron_data['LAY KENNETH L']['total_payments']

print "Total payment of Skilling: ", enron_data['SKILLING JEFFREY K']['total_payments']

print "Total payment of Fastow: ", enron_data['FASTOW ANDREW S']['total_payments']



count = 0
count2 = 0
for person in enron_data.items():
	if person[1]['salary'] != 'NaN':
		count = count + 1
	if person[1]['email_address'] != 'NaN':
		count2 = count2 + 1

print "Number of people with qunatified salary: ", count

print "Number of people with email address: ", count2



count = 0
count2 = 0
for person in enron_data.items():
	count2 = count2+1
	if person[1]['total_payments'] == 'NaN':
		count = count + 1

print count2, " b)", count
print "Percentage of people without total_payments: ", count/float(count2)

count = 0
count2 = 0
for person in enron_data.items():
	if person[1]['poi'] == True:
		if person[1]['total_payments'] == 'NaN':
			count2 = count2 + 1

print "POI's wihout total_payments", count2

print enron_data

max_stock = -1
min_stock = -1

for person in enron_data.items():
	temp = person[1]['salary']
	if temp != 'NaN':
		if max_stock == -1:
			max_stock = temp
			min_stock = max_stock
		else:
			if temp > max_stock:
				max_stock = temp
			if temp < min_stock:	
				min_stock = temp
print "Max stock:", max_stock
print "Min stock:", min_stock


import sys 
data_dict = enron_data
print data_dict[ max( data_dict, key=lambda x: None if
          data_dict[x]['exercised_stock_options']=='NaN' else
          float(data_dict[x]['exercised_stock_options']) ) ]['exercised_stock_options'] 
print data_dict[ min( data_dict, key=lambda x: sys.float_info.max if
          data_dict[x]['exercised_stock_options']=='NaN' else
          float(data_dict[x]['exercised_stock_options']) ) ]['exercised_stock_options']
