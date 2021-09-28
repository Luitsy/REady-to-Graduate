import csv

#can set headers to each column here
header = ['Column Title 1', 'Column Title 2', 'Column Title 3', 'Column Title 4']

#open the csv file you want to create - create a blank file called xxx.csv in the scripts folder first
with open('csv_test.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
        
    # write the header
    writer.writerow(header)

    #get your data from someother script or commands above this point.
    #each row is set using [ ], each cell is seperated by , to end a row you also need ,
    data = [
        ['data1', 'data1', 'data1', 'data1'],
        ['data2', 'data2', 'data2', 'data2'],
        ['data3', 'data3', 'data3', 'data3'],
        ['data4', 'data4', 'data4', 'data4']
            ]

    # write multiple rows
    writer.writerows(data)