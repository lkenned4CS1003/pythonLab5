#lkenned4CS1003  3715439
#Kaelen Derrah


import matplotlib.pyplot as plt
import csv
import math

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
    if row[0] == 'Item':
        continue
    else:
        headers = row[0]
        c1 = row[1]
        c2 = row[2]
        c3 = row[3]
        constant = row[4]
        items_list = [c1, c2, c3, constant]
        items[row[0]] = items_list



for key in items:
    c1 = float(items[key][0])
    c2 = float(items[key][1])
    c3 = float(items[key][2])
    constant = float(items[key][3])
    pieceSize = constant
    x = [0]
    y = [constant]
    timer = 0
    while pieceSize > 0:
        new_pieces = (c1 * (timer **3)) + (c2 * (timer **2)) + (c3 * timer) + constant
        pieceSize = new_pieces
        if pieceSize <= 0:
            pieceSize = 0
            y.append(pieceSize)
        else:
            y.append(pieceSize)
            pass
        timer += 0.1
        x.append(timer)

    items[key].append(x)
    items[key].append(y)


print(items)
print(items['Guitar Hero'][5][2])
choice = 0
while choice != 6:
    print('\n\nSelect an option:')
    print('\t1: Search Item’s Blend Time')
    print('\t2: Longest Blend Time')
    print('\t3: Shortest Blend Time')
    print('\t4: Compare Blend Times')
    print('\t5: Percentage of Blend Times')
    print('\t6: Exit')
    choice = int(input('choice>'))

    # Search Item’s Blend Time
    if choice == 1:
        # TODO 3
        item_name = input('item name>')
        if item_name in items:
            for key in items:
                if key == item_name:
                    print(to_zero(items, item_name))
                    choice = 1
                    break
                else:
                    pass
        else:
            print(item_name, 'Does not exist in the file')
            choice = 1

        # Delete this line and pass below, it is only here so the code runs


    # Find the item with the Longest Blend Time
    elif choice == 2:
        # assume that the longest blend time is the
        # smallest number possible (negative infinity)
        longest_time = math.inf * -1
        longest_item = ''

        # loop through all items
        for key in items:
            time_to_zero = to_zero(items, key)

            # if the item's time is longer than the current longest
            if time_to_zero > longest_time:
                #set new longest time and longest item name
                longest_item = key
                longest_time = time_to_zero

        print("%s takes approximately %gs to blend and is the item that takes the longest time" %(longest_item, longest_time))

    # Find the item with the Shortest Blend Time
    elif choice == 3:
        # you can borrow from the code for choice == 2
        # but change it from the longest to the shortest blend time
        # TODO 4
        shortest_time = math.inf
        shortest_item = ''
        for key in items:
            time_to_zero = to_zero(items, key)

            if time_to_zero < shortest_time:
                shortest_item =key
                shortest_time = time_to_zero
        # Delete this line and pass below, it is only here so the code runs
        print("%s takes approximately %gs to blend and is the item that takes the shortest time" %(shortest_item,shortest_time))

    elif choice == 4:
        graph1 = input("item 1>")
        graph2 = input("item 2>")
        graph3 = input("item 3>")
        colour1 = input("color for item 1>")
        colour2 = input("color for item 2>")
        colour3 = input("color for item 3>")

        # TODO 5
        # create the line graphs for the 3 items, using the 3 colors
        x1_points = [items[graph1][4]]
        y1_points = [items[graph1][5]]
        plt.plot(x1_points, y1_points, label=graph1, color=colour1)

        x2_points = [items[graph2][4]]
        y2_points = [items[graph2][5]]
        plt.plot(x2_points, y2_points, label=graph2, color2=colour2)

        x3_points = [items[graph3][4]]
        y3_points = [items[graph3][5]]
        plt.plot(x3_points,y3_points, label=graph3, color3=colour3)

        plt.title('User Comparison')
        plt.xlabel('Time')
        plt.ylabel('Size of Piece')
        plt.legend()
        plt.show()


    elif choice == 5:
        time_given = float(input("Time for pie chart>"))

        below_above = [0, 0]

        for key in items:
          time_to_zero = to_zero(items, key)

          if time_to_zero <= time_given:
            below_above[0] += 1

          else:
            below_above[1] += 1

        plt.pie(below_above, colors=['red','blue'], labels=['%gs or less' %time_given, 'Above %gs' %time_given],explode = (0.1, 0),autopct = '%1.1f%%')

        plt.legend()
        plt.show()


file.close()



