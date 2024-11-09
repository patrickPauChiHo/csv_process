import csv
import yaml

#function to read csv file
def read_csv(file_path):
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            print(row)
            


def main():
    records = read_csv('input.csv')
    
    return records
    
if __name__ == '__main__':
    main()