import logging
import os
from datetime import datetime

def get_datetime(file):
    try:
        modification_time = os.path.getmtime(file)
        datetime_object = datetime.fromtimestamp(modification_time)
        formatted_date = datetime_object.strftime("%Y-%m-%d %H:%M:%S")
        logging.info(f"Modification date: {formatted_date}")
        return formatted_date
    except OSError as e:
        logging.error(f"Error retrieving modification date: {e}")
        raise e

def give_datetime(file):
    modification_date = get_datetime(file)

    if modification_date is not None:
        print(modification_date)