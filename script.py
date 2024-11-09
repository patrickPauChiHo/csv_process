import csv
import yaml

#function to read csv file
def read_csv(file_path):
    try:
    #add encoding="utf-8-sig" to remove the BOM character
        with open(file_path, 'r', encoding="utf-8-sig") as csv_file:
            #use the csv.DictReader to read the csv file to a dictionary
            csv_reader = csv.DictReader(csv_file)
            records=[row for row in csv_reader]
        return records
    #catch the FileNotFoundError exception
    except FileNotFoundError:
        print("File not found")
    #catch any other exception
    except Exception as e:
        print(e)

#function to convert to yaml_format
def convert_to_yaml(records):
    formatted_records = []
    for record in records:
        formatted_record = {
            'name': f"{record['firstname']} {record['lastname']}",
            'details': f"In division {record['division']} from {record['date']} performing {record['summary']}"
        }
        formatted_records.append(formatted_record)
    return yaml.dump({'records': formatted_records}, default_flow_style=False)
            


def main():
    records = read_csv('input.csv')
    #change the data type to integer for comparison
    #sort the records by division and points
    sorted_records = sorted(records, key=lambda x: (int(x['division']), -int(x['points'])))
    
    #get the top three records
    top_three_records=sorted_records[:3]
    
    #convert the top three records to yaml format
    yaml_records = convert_to_yaml(top_three_records)
    
    print (yaml_records)
    
    
    
if __name__ == '__main__':
    main()