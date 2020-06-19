import csv
csv_file = input('Enter the name of your input file: ')
csv_file1 = input('Enter the name of your output file ')
reader = csv.reader(open(csv_file, "rU"), delimiter=';')
writer = csv.writer(open(csv_file1, 'w'), delimiter=',')
writer.writerows(reader)

    


