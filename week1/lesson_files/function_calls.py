
#Initialize array
array1 = ['One', 'Two', 'Three', 'One', 'Four', 'Three', 'One', 'Two']

def analyze_list(list): 
	
	#Initialize dictionary
	counts_of_each_instance = {}
	
	for item in list:
		if item in counts_of_each_instance:
			counts_of_each_instance[item] = counts_of_each_instance[item] + 1;
		else:
			counts_of_each_instance[item] = 1
	
	return counts_of_each_instance
	
variable1 = analyze_list(array1)
print(variable1)
	