import argparse
import logging
import csv
import argparse
from datetime import datetime
from args_parser import clean_data_file

logging.basicConfig(level=logging.INFO)


class import_data:
    def import_dat(file_path):
        data_list = [] 
        try:
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    data_entry = {
                        'perception': row['Data.Precipitation'],
                        'date_full': row['Date.Full'],
                        'date_month': row['Date.Month'],
                        'date_week': row['Date.Week of'],
                        'date_year': row['Date.Year'],
                        'station': row['Station.City'],
                        'station_code': row['Station.Code'],
                        'station_location': row['Station.Location'],
                        'station_state': row['Station.State'],
                        'avg_temp': row['Data.Temperature.Avg Temp'],
                        'max_temp': row['Data.Temperature.Max Temp'],
                        'min_temp': row['Data.Temperature.Min Temp'],
                        'wind_direction': row['Data.Wind.Direction'],
                        'wind_speed': row['Data.Wind.Speed']
                    }
                    data_list.append(data_entry)
            logging.info(f"Imported data from {file_path}")
        except Exception as e:
            logging.error(f"Error importing data: {str(e)}")
        return data_list
    

class analyze_data:
    def analyze_data(start, end,dataaa):
        try:
            start_Date = datetime.strptime(start, "%Y-%m-%d")
            end_Date = datetime.strptime(end, "%Y-%m-%d")
            filtered_data = [entry for entry in dataaa if start_Date <= datetime.strptime(entry.get('date_full'), "%Y-%m-%d") <= end_Date]
            list = ([entry.get('avg_temp') for entry in filtered_data])
            max_temp = ([entry.get('max_temp') for entry in filtered_data])
            min_temp = ([entry.get('min_temp') for entry in filtered_data])
            wind_direction = ([entry.get('wind_direction') for entry in filtered_data])
            wind_speed = ([entry.get('wind_speed') for entry in filtered_data])
            average_temperature = sum(int(num) for num in list)/len(list)
            average_max_temperature = sum(int(num) for num in max_temp)/len(max_temp)
            average_min_temperature = sum(int(num) for num in min_temp)/len(min_temp)
            average_wind_direction = sum(int(num) for num in wind_direction)/len(wind_direction)
            average_wind_speed = sum(float(num) for num in wind_speed)/len(wind_speed)
            min_temperature = min(int(num) for num in list)
            max_temperature = max(int(num) for num in list)
            print(max_temperature)

            state = ([entry.get('station_location','station_state') for entry in filtered_data if entry.get('avg_temp')==max_temperature])
            month = ([entry.get('date_month') for entry in filtered_data if max_temperature==entry.get('avg_temp')])
            year = ([entry.get('date_year') for entry in filtered_data if entry.get('avg_temp')==min_temperature])
            day = ([entry.get('date_full') for entry in filtered_data if entry.get('avg_temp')==min_temperature])

            print(state)
            print(month)
            print(year)
            print(day)
            logging.info("Data is validating")
            return average_temperature, min_temperature, max_temperature,average_max_temperature,average_min_temperature,average_wind_speed,average_wind_direction
            
        except Exception as e:
            logging.error(f"Error analyzing data: {str(e)}")
    
class export_data:
    def write_to_csv(file_name, data):
        try:
            with open(file_name, 'a', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(['Average Temprature is ' + str(data[0])])
                csv_writer.writerow(['Minimum Temprature is ' + str(data[1])])
                csv_writer.writerow(['Maximum temprature is ' + str(data[2])])
                csv_writer.writerow(['Average Maximum temprature is ' + str(data[3])])
                csv_writer.writerow(['Average Minimum temprature is ' + str(data[4])])
                csv_writer.writerow(['Avereage wind speed is ' + str(data[5])])
                csv_writer.writerow(['Average wind direction is ' + str(data[6])])
            logging.info(f'Data successfully written to {file_name}')
            return True
        except Exception as e:
            logging.info(f'Error writing to {file_name}: {e}')

def calc(args):
    data = import_data.import_dat(args.file)
    return data

def analyze(args):
    data = calc(args)
    date_range = args.range.split(' to ')
    result =analyze_data.analyze_data(date_range[0], date_range[1], data)
    return result


def export(args):
    values = analyze(args)
    if values == None:
        logging.error("Doesnot found any data")
        return
    export_data.write_to_csv(args.format, values)


from args_parser import CustomArgumentParser

if __name__ == '__main__':
    custom_parser = CustomArgumentParser()
    args = custom_parser.parse_args()
    export(args)



