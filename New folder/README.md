# Command Line Python Task

## Introduction

Added arguments of file, range, format, state, location, explain, analyzestate
It will check that given command exist or not
Wrote tests for all commands

## --inputFile
It will take a file path which we want to read and import its data


### Validaions
- File is present or not

```
 python task.py --inputFile hello.txt
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
python task.py --inputFile weather_1.csv --range "2017-01-03 to 2016-01-03" --output values.csv
```

Output:

INFO:root:Start date cannot be greater than end date.<br>
INFO:root:Invalid date range format. Please provide a valid range.

```
python task.py --inputFile weather_1.csv --range "2018-01-03 to 2019-01-03" --output values.csv
```

Output:

INFO:root:Date '2018-01-03' not found in the file 'weather_1.csv'<br>
INFO:root:date not found

## --output
 It will take argument of str that is a file name and store the analyzed data in the given file name argument

```
python task.py --inputFile weather_1.csv  --range "2016-01-03 to 2016-01-03" --output values.csv
```

Output:

  INFO:root:Imported data from weather_1.csv
<br>
  INFO:root:Data is validating
<br>
  INFO:root:Data successfully written to values.csv

 This command will read file __weather_1.csv__ , analyze the data tand store its average temprature, minimum temprature and maximum temprature, average minimum temprature, average maximum temprature, average wind speed and average wind direction to __values.csv__ file

### Validations
- It will check that the file format is either .txt or .csv

```
python task.py --output hello.hello
```

Output:

  INFO:root:Error: Invalid file extension. Allowed extensions are ['.csv', '.txt']. Detected extension: .hello.
<br>
  INFO:root:Invalid file format. Please provide a valid format.

## --max
 It will return maximum occuring column in the given file

```
python task.py --max 'Date.Full' --inputFile weather_1.csv  
```
Output:

INFO:root:Maximum is 2017-01-01

 This command will read the will __weather_1.csv__ and print the most occuring Date.Full from the file

## --averageData
 It will print Average (Max and Min) Temperature, Average Wind Direction, Average wind speed for given date range from a given file

```
python task.py --averageData --inputFile weather_1.csv --range '2016-01-03 to 2016-01-03' 
```
Output:

 INFO:root:Imported data from weather_1.csv
<br>
 INFO:root:Data is validating
<br>
 State is ['Key West, FL']
<br>
 Year is ['2016']
<br>
 Month is ['1']
<br>
 Day is ['2016-01-03']

 This command will read the file __weather_1.csv__ and print the state, Year, Month and Day which have maximum temprature from range '2016-01-03 to 2016-01-03'

## --getLocation
 It will print station, station_code , station_location and station_state of maximum average temprate from a given range of date  from a whole file

```
python task.py --getLocation weather_1.csv --range '2016-01-03 to 2016-01-03'
```
Output:
 INFO:root:Imported data from weather_1.csv
 ['Key West'] ['Key West, FL']

 This command will read weather_1.csv and print the station, station_code, station_location and station_state of maximum average temprature within givin range

## --getLocation
 It will print station, station_code , station_location and station_state of maximum average temprate from a given file

```
python task.py --getLocation weather_1.csv
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
<br>
Minimum date is 2016-01-03
<br>
Maximum date is 2017-01-01
<br>
Minimum average temprate is -27
<br>
Minimum max_temprate is -19
<br>
Minimum min temprate is -35
<br>
Minimum wind direction is 0
<br>
Minimum wind speed is 0.0
<br>
Max_temprate is 100
<br>
Maximum max temprate is 111
<br>
Maximum min temprature is 88\
<br>
Maximum wind direction is 36
<br>
Max wind speed is 61.1