import shutil
import os

file_name = input("Enter the file name: ")

def get_datetime(file):
    try:
        return os.path.getmtime(file)
    except OSError as e:
        print(f"Error retrieving modification date: {e}")
        return None

m_date = get_datetime(file_name)

if m_date is not None:
    print(m_date)