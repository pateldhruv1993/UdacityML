#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
	cleaned_data = []
	print "I'M IN"
	count = 0
	
	for prediction in predictions:
		residual_error = prediction - net_worths[count]
		cleaned_data.append((ages[count], net_worths[count], abs(residual_error)))
		count = count + 1
    
	
	cleaned_data.sort(key = lambda tup : tup[2])
	
	del cleaned_data[81:]
	
	return cleaned_data

