# Command Line Python Task

## Introduction

Added arguments of file, range, format, state, location, explain, analyzestate
It will check that given command exist or not
Wrote tests for all commands

## --file
It will take a file path which we want to read and import its data


### Validaions
- File is present or not

```
python task.py --file hello.txt
```
Output:

  INFO:root:File not found. Please provide a valid file.

## --range
It will take the range of date in whcih we have to analyze data

### Validations
- It will check that date is in right format i.e 'YYYY-MM-DD to YYYY-MM-DD'
- It will check that given range is present in file or not
- It will check that start data ca't be greater than end date'

```
python task.py --file weather_1.csv  --range "2017-01-03 to 2016-01-03" --format values.csv
```

Output:

  INFO:root:Start date cannot be greater than end date.

  INFO:root:Invalid date range format. Please provide a valid range.

  INFO:root:Date '2017-01-03' not found in the file 'weather_1.csv'

  INFO:root:date not found

## --format
 It will take argument of str that is a file name and store the analyzed data in the given file name argument

```
python task.py --file weather_1.csv  --range "2016-01-03 to 2016-01-03" --format values.csv
```

Output:

  INFO:root:Imported data from weather_1.csv

  INFO:root:Data is validating

  INFO:root:Data successfully written to values.csv

 This command will read file __weather_1.csv__ , analyze the data tand store its average temprature, minimum temprature and maximum temprature, average minimum temprature, average maximum temprature, average wind speed and average wind direction to __values.csv__ file

### Validations
- It will check that the file format is either .txt or .csv

```
python task.py --format hello.hello
```

Output:

  INFO:root:Error: Invalid file extension. Allowed extensions are ['.csv', '.txt']. Detected extension: .hello.

  INFO:root:Invalid file format. Please provide a valid format.

## --state
 It will return maximum occuring state in the given file

```
python task.py --state --file weather_1.csv
```
Output:

Alaska

 This command will read the will __weather_1.csv__ and print the most occuring state from the file

## --analyzestate
 It will print Average (Max and Min) Temperature, Average Wind Direction, Average wind speed for given date range from a given file

```
python task.py --analyzestate --file weather_1.csv --range '2016-01-03 to 2016-01-03' 
```
Output:

 INFO:root:Imported data from weather_1.csv

 INFO:root:Data is validating

 State is ['Key West, FL']

 Year is ['2016']

 Month is ['1']

 Day is ['2016-01-03']

 This command will read the file __weather_1.csv__ and print the state, Year, Month and Day which have maximum temprature from range '2016-01-03 to 2016-01-03'

## --location
 It will print station, station_code , station_location and station_state of maximum average temprate from a given range of date  from a whole file

```
python task.py --location weather_1.csv --range "2016-01-03 to 2016-01-03"
```
Output:
 INFO:root:Imported data from weather_1.csv
 ['Key West'] ['Key West, FL']

 This command will read weather_1.csv and print the station, station_code, station_location and station_state of maximum average temprature within givin range

## --location
 It will print station, station_code , station_location and station_state of maximum average temprate from a given file

```
python task.py --location weather_1.csv
```

Output:
 INFO:root:Imported data from weather_1.csv
 ['Las Vegas'] ['Las Vegas, NV']

 This command will read weather_1.csv and print the station, station_code, station_location and station_state of maximum average temprature from whole file

 ## --explain

 ```
  python task.py --explain weather_1.csv
 ```

 Output:

Minimum date is 2016-01-03 00:00:00  

Maximum date is 2017-01-01 00:00:00

Minimum average temprate is -27

Minimum max_temprate is -19

Minimum min temprate is -35

Minimum wind direction is 0

Minimum wind speed is 0.0

Max_temprate is 100

Maximum max temprate is 111

Maximum min temprature is 88

Maximum wind direction is 36

Max wind speed is 61.1