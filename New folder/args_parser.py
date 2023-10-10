import argparse
import os
from datetime import datetime
import pandas as pd
import logging
import csv

class CustomArgumentParser(argparse.ArgumentParser):
    def __init__(self):
        super(CustomArgumentParser, self).__init__()
        self.add_argument('--file', type=str, help='Enter File name')
        self.add_argument('--range', type=str, help='Enter range of date')
        self.add_argument('--format', type=str, help='Enter export file name')
        self.add_argument('--cleann', type=str, help='Enter File name to clean')
        self.add_argument('--state', nargs='*', help='State name(s)')

    def validate_args(self, args):
        if args.range and not validate_date_range(args.range):
            logging.info("Invalid date range format. Please provide a valid range.")

        if args.format and not validate_file_format(args.format, allowed_extensions=[".csv", ".txt"]):
            logging.info("Invalid file format. Please provide a valid format.")

        if args.file and not os.path.isfile(args.file):
            logging.info("File not found. Please provide a valid file.")

        if args.range and not validate_date_in_csv(args.file, args.range):
            logging.info("date not found")

        if args.range and not validate_date_range(args.range):
            logging.info("date can't be grater")

        if args.state==[]:
            print(find_state_with_maximum_occurrence(args.file))

    def validate_commands(self, command):
        valid_commands = ['--file', '--format', '--export']
        if command not in valid_commands:
            logging.info("Invalid command. Please choose from: {}".format(valid_commands))

    def validate_flags(args):
        allowed_flags = {'--file', '--range', '--format'}

        for arg in args:
            if arg not in allowed_flags:
                logging.info(f"Invalid flag '{arg}'. Allowed flags are {allowed_flags}")
        return args

def validate_date_range(date_range):
    date_format = '%Y-%m-%d'
    date_range = date_range.split(' to ')

    try:
        datetime.strptime(date_range[0], date_format)
        datetime.strptime(date_range[1], date_format)
    except ValueError:
        logging.info('Invalid date format. Please use YYYY-MM-DD.')
        return False
    return True


def validate_file_format(file_path, allowed_extensions=None):
    _, file_extension = os.path.splitext(file_path)
    if allowed_extensions and file_extension.lower() not in allowed_extensions:
        logging.info(f"Error: Invalid file extension. Allowed extensions are {allowed_extensions}. Detected extension: {file_extension}.")
        return False

    return True

def validate_date_in_csv(file_path, given_date):
    date_range = given_date.split(' to ')
    df = pd.read_csv(file_path)
    column_name = 'Date.Full'
    if date_range[0] not in df[column_name].values:
        logging.info(f"Date '{date_range[0]}' not found in the file '{file_path}'")

    if date_range[1] not in df[column_name].values:
        logging.info(f"Date '{date_range[1]}' not found in the file '{file_path}'")
        return False

    return True


def validate_date_range(date_given):
    date_range = date_given.split(' to ')
    start_date = date_range[0]
    end_date = date_range[1]

    if datetime.strptime(start_date, '%Y-%m-%d') > datetime.strptime(end_date, '%Y-%m-%d'):
        logging.info("Start date cannot be greater than end date.")
        return False

    return True


def clean_data_file(file_path):
    count = 0
    # try:
    print("try")
    with open(file_path, 'r+') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)

    for row in data:
        for key, value in row.items():
            if not value:
                if isinstance(row[key], str):
                    csvfile.write('0')
                else:
                    csvfile.write('0.0')

    data = [row for row in data if row.get('Date.Full') is not None]

    print(count)
    return data

def find_state_with_maximum_occurrence(file_path):
    df = pd.read_csv(file_path)
    state_counts = df['Station.State'].value_counts()

    max_occurrence_state = state_counts.idxmax()

    return max_occurrence_state
