"""This file holds utility and helper functions used across many modules."""

from pathlib import Path
import csv

def load_csv_file(relative_file_path:Path):   
    data_dir = Path.cwd().parent / "data" / relative_file_path
    data = {}
    for data_file in data_dir.iterdir():
        with data_file.open(mode='r', encoding="utf-8") as file:
            reader = csv.reader(file)
            file_data = next(reader)
                
        data[f"{data_file.name}"[:-4]] = file_data
    
    return data
    

def save_to_abs_path(data: list, file_name: str, save_dir_path: Path = Path.cwd()):
    if save_dir_path.is_dir():
        with open(f"{file_name}.txt", "w") as file:
            file.writelines(data)
    else:
        print("The given path is not to a directory!")