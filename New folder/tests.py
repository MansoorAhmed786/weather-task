import unittest
import logging
from task import import_data, analyze_data, export_data

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


if __name__ == '__main__':
    unittest.main()
