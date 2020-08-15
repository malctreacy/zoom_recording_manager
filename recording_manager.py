import pandas
import csv
csv_file = 'C:\\Users\\malco\\Desktop\\Recordings\\recording_totals.csv'
csv_columns = ['Host', 'Total']
dictData = dict()

recordings = pandas.read_csv('C:\\Users\\malco\\Desktop\\Recordings\\recording_list.csv')

for ind in recordings.index:
    if recordings['File Size (rounded MB)'][ind] != 'Processing Recording...':
        if recordings['Host'][ind] in dictData:
            dictData[recordings['Host'][ind]] += int(recordings['File Size (rounded MB)'][ind].replace(',',''))
        else:
            dictData[recordings['Host'][ind]] = int(recordings['File Size (rounded MB)'][ind].replace(',',''))
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = csv_columns )
        writer.writeheader()
        for key, value in dictData.items():
            writer.writerow({'Host': key, 'Total': value})
except IOError:
    print('Unknown Error')
