import os
from datetime import datetime
from tkinter import messagebox

def get_datetime(file):
    try:
        modification_time = os.path.getmtime(file)
        datetime_object = datetime.fromtimestamp(modification_time)
        formatted_date = datetime_object.strftime("%Y-%m-%d %H:%M:%S")
        return formatted_date
    except OSError as e:
        print(f"Error retrieving modification date: {e}")
        return None

def give_datetime(file):
    file_name = input("Enter the file name: ")
    modification_date = get_datetime(file_name)

    if modification_date is not None:
        messagebox.showinfo("Information", modification_date)

give_datetime("C:\\Users\\User\\Desktop\\test.txt")