# Python3 program to validate the time in 
# 24-hour format using Regular Expression. 
import re 

# Function to validate the time 
# in 24-hour format 
def isValidTime(time): 
	
	# Regex to check valid time in 24-hour format. 
	regex = "^([01]?[0-9]|2[0-3]):[0-5][0-9]$"; 

	# Compile the ReGex 
	p = re.compile(regex); 

	# If the time is empty 
	# return false 
	if (time == "") : 
		return False; 
		
	# Pattern class contains matcher() method 
	# to find matching between given time 
	# and regular expression. 
	m = re.search(p, time); 
	
	# Return True if the time 
	# matched the ReGex otherwise False 
	if m is None : 
		return False; 
	else : 
		return True
		
# Driver Code. 
if __name__ == "__main__" : 
	
	# Test Case 1: 
	str1 = "13:05"; 
	print(str1, ": ", isValidTime(str1)); 

	# Test Case 2: 
	str2 = "02:15"; 
	print(str2, ": ", isValidTime(str2)); 
	
	# Test Case 3: 
	str3 = "24:00"; 
	print(str3, ": ", isValidTime(str3)); 
	
	# Test Case 4: 
	str4 = "10:60"; 
	print(str4, ": ", isValidTime(str4)); 
	
	# Test Case 5: 
	str5 = "10:15 PM"; 
	print(str5, ": ", isValidTime(str5)); 

# This code is contributed by AnkitRai01 
