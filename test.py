import csv


#This function takes the dictionary of items and a key and returns the amount of time it
#will take to blend
def to_zero(items_dict, key_name):
    blend_times = items_dict[key_name][4]
    time_to_zero = blend_times[len(blend_times) - 1]
    return time_to_zero

file = open('Items.csv')
reader = csv.reader(file, delimiter=',')
items = dict()

for row in reader:
    print(row)
