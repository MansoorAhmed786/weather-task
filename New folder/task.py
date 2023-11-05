import logging
from args_parser import CustomArgumentParser

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    custom_parser = CustomArgumentParser()
    args = custom_parser.parse_args()
    custom_parser.validate_args(args)

