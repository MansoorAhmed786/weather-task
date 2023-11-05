import unittest
import logging
from args_parser import import_data, analyze_data, export_data, validate_date,validate_date_range, validate_file_format, validate_date_in_csv

class TestWeatherAnalyzer(unittest.TestCase):
    def setUp(self):
        logging.disable(logging.CRITICAL) 

    def tearDown(self):
        logging.disable(logging.NOTSET) 

    def test_import_data(self):
        file_path = 'weather_1.csv'
        data_list = import_data.import_dat(file_path)
        self.assertIsInstance(data_list, list)
        self.assertTrue(len(data_list) > 0)

    def test_analyze_data(self):
        file_path = 'weather_1.csv'
        data_list = import_data.import_dat(file_path)
        result = analyze_data.analyze_data('2016-03-06', '2016-01-03', data_list)
        self.assertIsNone(result)

    def test_analyze_data_invalid_date_format(self):
        file_path = 'weather_1.csv'
        data_list = import_data.import_dat(file_path)
        result = analyze_data.analyze_data('01-01-2022', '2022-01-03', data_list)
        self.assertIsNone(result)

    def test_export_data(self):
        file_path = 'weather_1.csv'
        data_list = import_data.import_dat(file_path)
        result = analyze_data.analyze_data('2016-01-03', '2016-01-03', data_list)
        val = export_data.write_to_csv('output.csv',result)
        self.assertTrue(val)

    def test_validate_date(self):
        date='2000-12-01 to 2016-12-01'
        result =validate_date(date)
        self.assertTrue(result)

    def test_validate_invalid_date(self):
        date='12-01 to 2016-12-01'
        result =validate_date(date)
        self.assertFalse(result)

    def test_validate_date_range(self):
        date='2000-12-01 to 2016-12-01'
        result =validate_date_range(date)
        self.assertTrue(result)
          
    def test_validate_invalid_date_range(self):
        date='2025-12-01 to 2016-12-01'
        result =validate_date_range(date)
        self.assertFalse(result)

    def test_validate_file_format(self):
        file = 'hello.txt'
        result = validate_file_format(file)
        self.assertTrue(result)

    def test_validate_invalid_file_format(self):
        file = 'hello.hello'
        result = validate_file_format(file)
        self.assertTrue(result)

    def test_validate_date_present(self):
        date = '2016-01-03 to 2016-01-03'
        self.assertTrue(validate_date_in_csv('weather_1.csv',date))

    def test_validate_invalid_date_present(self):
        date = '2222-10-10 to 2222-10-10'
        self.assertFalse(validate_date_in_csv('weather_1.csv',date))


if __name__ == '__main__':
    unittest.main()
