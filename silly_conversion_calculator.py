# This function called to_metric takes as input a string respresenting a quantity
# in imperial volume units, such as "2 tablespoons" or "7.25 cups", and returns its
# conversion to milliliters. The function accounts for case sensitivity of the function
# argument, and always rounds the conversion to 2 decimal places.


def to_metric(a_string):
    
    a_string == a_string.lower()
    string_value = a_string.split()
    answer = 0
    
    if a_string.endswith("gallons"):
        answer = float(string_value[0]) * 4546.09
  
    elif a_string.endswith("quarts"):
        answer = float(string_value[0]) * 1136.52
    
    elif a_string.endswith("pints"):
        answer = float(string_value[0]) * 568.26
    
    elif a_string.endswith("cups"):
        answer = float(string_value[0]) * 236.59
    
    elif a_string.endswith("ounces"):
        answer = float(string_value[0]) * 28.41
    
    elif a_string.endswith("tablespoons"):
        answer = float(string_value[0])* 14.79
    
    elif a_string.endswith("teaspoons"):
        answer = float(string_value[0]) * 4.93
        
    return a_string + " converted to milliliters is " + str(round(answer, 2))

# testing the function

print(to_metric("7.25 cups"))
print(to_metric("2.0 tablespoons"))
print(to_metric("8.75 gallons"))
print(to_metric("16.5 teaspoons"))
