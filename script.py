import csv
import yaml

#function to read csv file
def read_csv(file_path):
    with open(file_path, 'r') as csv_file:
        #use the csv.DictReader to read the csv file to a dictionary
        csv_reader = csv.DictReader(csv_file)
        records=[row for row in csv_reader]
    return records
            


def main():
    records = read_csv('input.csv')
    sorted_records = sorted(records, key=lambda x: (int(x['division']), -int(x['points'])))
    print(sorted_records)
    
    
    
if __name__ == '__main__':
    main()